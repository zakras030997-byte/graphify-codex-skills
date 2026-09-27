---
name: graphify-memory-map
description: Build or refresh an interactive, sampled map of the projects in a local Graphify code index. Use when the user asks to see the code graph or its project composition; use graphify-code-search for a specific code question.
---

# Project code map with Graphify

The graph is a searchable snapshot of code relationships, not a complete memory of decisions or a verified dependency diagram. Keep approved decisions and work status in the user's chosen source of truth.

## Prepare

- Locate the intended `graph.json` with `graphify global path`, `graphify global list`, or a user-supplied path. Confirm which projects it contains and when it was last updated.
- Do not index an entire computer or add private documents, secrets, client data, logs, or old builds just to draw a larger map. New sources, background scheduling, and API-based semantic extraction require separate scope and permission.
- If the user explicitly asks to refresh the graph, use the already configured project-specific refresh process, when available, and verify its result. Do not replace or alter that process as a side effect of viewing the graph.

## Render and report

Run `scripts/render.py` with a Python interpreter that can import Graphify and NetworkX:

`python scripts/render.py --graph <graph.json> --output <allowed-output-dir>/graph.html`

The script leaves the full input graph unchanged, selects a bounded set of well-connected nodes from each project, and keeps only within-project edges in the display. Cross-project edges can be false matches and should be verified in source before they are visualized as real dependencies. Report the number of projects, full nodes and edges, displayed nodes and edges, source age, and exclusions. Never call a sampled view the complete node-level graph.

If the available browser refuses to open a local HTML file, do not bypass its security restrictions. Provide the local artifact and state that visual rendering was not verified.
