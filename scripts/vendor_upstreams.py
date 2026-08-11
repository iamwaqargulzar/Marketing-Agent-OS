#!/usr/bin/env python3
"""Compatibility entry point for the Marketing Agent OS upstream updater."""

from __future__ import annotations

import sys

from update_upstreams import main


if __name__ == "__main__":
    print(
        "Note: vendor_upstreams.py is retained as an alias; "
        "use update_upstreams.py for new automation.",
        file=sys.stderr,
    )
    sys.exit(main())
