# Graphify skills for Codex

Two small Codex skills for navigating a local Graphify code index and rendering a project-level graph view.

| Skill | Use |
| --- | --- |
| `graphify-code-search` | Find symbols, inspect nearby code relationships, and identify likely impact. |
| `graphify-memory-map` | Render a navigable, sampled view of all projects in a Graphify graph. |

The graph is a **code index**, not an agent's permanent memory, a decision log, or proof that a runtime path works. Verify important findings in the current source and tests. Obsidian or any other project record can remain the source of approved decisions and status.

## Requirements

- Codex with local skill support.
- A locally installed `graphify` command and a Graphify `graph.json`. For the optional renderer, use a Python environment with the `graphifyy` and `networkx` packages.

## Install

Copy both directories under `skills/` to your Codex skills directory (typically `~/.codex/skills/`). The skills are available for automatic selection by default; no invocation policy needs changing.

Point the skills to your own index: run `graphify global path` for a merged graph, or provide the path to a specific project's `graph.json`. Do not copy a private graph into this repository.

## Render a graph view

From this repository, using Python with Graphify available:

```bash
python skills/graphify-memory-map/scripts/render.py \
  --graph /absolute/path/to/graph.json \
  --output /absolute/path/to/graph.html
```

The viewer selects up to 180 highly connected nodes per project by default. It preserves actual within-project graph edges but omits cross-project edges, because matching symbol names can produce false dependencies. The output reports both full-index and visible counts. A rendered HTML file is a local artifact; it is not included in this repository.

## Privacy and limitations

- Both skills use local Graphify commands. They do not require uploading source code or documents to an LLM API.
- Select index sources deliberately. Exclude credentials, personal data, private logs, and stale copies unless you have a specific reason and permission to include them.
- Graphify can miss recently edited files until its index is refreshed. It can also reverse or infer an edge incorrectly. Confirm imports, calls, and behavior in live source and tests before relying on them.
- The viewer may load its visualization library from a public CDN when opened. If that is not acceptable in your environment, use an approved offline renderer.

## License

MIT. See [LICENSE](LICENSE).
