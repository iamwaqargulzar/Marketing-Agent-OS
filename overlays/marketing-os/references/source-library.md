# Complete source library

Each archive under `assets/` in the installed `marketing-os` folder contains the complete tracked tree of one pinned repository. This includes the original skills, commands, agents, helpers, registries, dashboards, hooks, tests, templates, licenses, and host configuration wherever provided by that source. Relative paths in the original workflows start at their extracted source root.

| Archive | Workflows |
|---|---|
| `source-a.tar.bz2` | Marketing operations, registries, scoring, connectors and dashboards |
| `source-b.tar.bz2` | SEO, analytics, audits, extensions and specialist agents |
| `source-c.tar.bz2` | GEO, AI visibility, reports and specialist agents |
| `source-d.tar.bz2` | Product marketing, growth, copywriting, lifecycle and provider CLIs |

From the installed router folder, list the contents with `python3 -m tarfile -l assets/source-a.tar.bz2`. To use an original workflow, extract its archive into a **new empty directory** outside the host's skill discovery directories. For example:

```sh
python3 -m tarfile -e assets/source-a.tar.bz2 /path/to/new/source-a
```

On Windows, use `py -3` in place of `python3`. Read the source's README and the workflow at the path given by the specialist. Run original commands from the extracted directory using the source's declared dependencies. The original sources may use different host conventions. Installing dependencies, enabling hooks, setting credentials, making paid calls, sending, and writing business data require authorization for the specific action. Extraction alone does none of those things.

The portable agent definitions are also available directly in `references/agents/` in this skill. On hosts without named agents, read the relevant definitions and perform their analyses inline.
