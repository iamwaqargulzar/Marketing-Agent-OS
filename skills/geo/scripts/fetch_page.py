#!/usr/bin/env python3
"""Fetch public HTTP(S) pages with bounded reads and basic metadata extraction."""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
import socket
import urllib.parse
import urllib.request
from html import unescape


def validate_url(url: str, allow_private: bool) -> None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("URL must use http:// or https:// and include a hostname")
    if parsed.username or parsed.password:
        raise ValueError("URLs containing credentials are not accepted")
    if allow_private:
        return
    for result in socket.getaddrinfo(parsed.hostname, parsed.port or 443, type=socket.SOCK_STREAM):
        address = ipaddress.ip_address(result[4][0])
        if not address.is_global:
            raise ValueError(f"private, loopback, link-local, or reserved address blocked: {address}")


class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def __init__(self, allow_private: bool):
        super().__init__()
        self.allow_private = allow_private

    def redirect_request(self, request, fp, code, msg, headers, newurl):
        validate_url(newurl, self.allow_private)
        return super().redirect_request(request, fp, code, msg, headers, newurl)


def first_text(html: str, pattern: str) -> str | None:
    match = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    return unescape(re.sub(r"<[^>]+>", " ", match.group(1))).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument("--max-bytes", type=int, default=5_000_000)
    parser.add_argument("--allow-private", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.timeout <= 0 or args.max_bytes <= 0:
        parser.error("--timeout and --max-bytes must be positive")

    validate_url(args.url, args.allow_private)
    request = urllib.request.Request(
        args.url,
        headers={"User-Agent": "MarketingAgentOS/1.1 (+read-only audit)"},
    )
    opener = urllib.request.build_opener(SafeRedirect(args.allow_private))
    with opener.open(request, timeout=args.timeout) as response:
        raw = response.read(args.max_bytes + 1)
        if len(raw) > args.max_bytes:
            raise SystemExit(f"Response exceeds --max-bytes ({args.max_bytes})")
        charset = response.headers.get_content_charset() or "utf-8"
        html = raw.decode(charset, "replace")
        final = response.geturl()
        validate_url(final, args.allow_private)
        status = getattr(response, "status", 200)

    output = {
        "requested_url": args.url,
        "final_url": final,
        "status": status,
        "bytes": len(raw),
        "title": first_text(html, r"<title[^>]*>(.*?)</title>"),
        "meta_description": None,
        "canonical": None,
        "robots_meta": None,
        "h1_count": len(re.findall(r"<h1\b", html, re.IGNORECASE)),
    }
    match = re.search(
        r"<meta[^>]+name=[\"']description[\"'][^>]+content=[\"'](.*?)[\"']",
        html,
        re.IGNORECASE | re.DOTALL,
    ) or re.search(
        r"<meta[^>]+content=[\"'](.*?)[\"'][^>]+name=[\"']description[\"']",
        html,
        re.IGNORECASE | re.DOTALL,
    )
    output["meta_description"] = unescape(match.group(1)).strip() if match else None
    match = re.search(
        r"<link[^>]+rel=[\"'][^\"']*canonical[^\"']*[\"'][^>]+href=[\"'](.*?)[\"']",
        html,
        re.IGNORECASE | re.DOTALL,
    )
    output["canonical"] = urllib.parse.urljoin(final, match.group(1).strip()) if match else None
    match = re.search(
        r"<meta[^>]+name=[\"']robots[\"'][^>]+content=[\"'](.*?)[\"']",
        html,
        re.IGNORECASE | re.DOTALL,
    )
    output["robots_meta"] = match.group(1).strip() if match else None
    print(
        json.dumps(output, indent=2, ensure_ascii=False)
        if args.json
        else "\n".join(f"{key}: {value}" for key, value in output.items())
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
