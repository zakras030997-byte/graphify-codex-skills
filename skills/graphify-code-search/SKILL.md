---
name: graphify-code-search
description: Automatically use for codebase and architecture questions when a local Graphify index can help locate an implementation, trace symbols, or estimate change impact. Navigate with Graphify, then verify in current source; skip it for simple exact-text searches or project-status questions.
---

# Fast code navigation with Graphify

Graphify is a local navigation index, not proof that a call path runs. Locate the appropriate graph with `graphify global path`, a project-local `graphify-out/graph.json`, or a graph path provided by the user. Do not assume every current project is indexed or that an index is fresh.

## Use it when

- The user asks where behavior is implemented, how components relate, or what a change may affect.
- Start with `rg` instead when the user already knows an exact string or filename. Do not use the graph as the source of approved decisions, payment state, deployment state, or runtime health.

## Focused search

1. Search a distinctive symbol or short behavior label: `graphify query "<term>" --graph <graph.json> --budget 1200`. Natural-language phrases may miss symbols; try an exact class, function, module, or API name when needed.
2. For one known node use `graphify explain "<node>" --graph <graph.json>`. For likely change impact use `graphify affected "<node>" --depth 2 --graph <graph.json>`. Use `graphify path "<A>" "<B>" --graph <graph.json>` only after disambiguating both nodes. Avoid running every command by default.
3. Read the current source with `rg` and focused file inspection before reporting a dependency. Treat edge direction, especially extracted `calls` and `imports` edges, as a hint: it can be reversed. Treat generic cross-project symbol matches as unverified.
4. In the answer distinguish **found in the graph**, **confirmed in current source**, and **verified by execution or tests**. If the graph is missing or stale, fall back to source search rather than rebuilding it as a side effect.

Queries are local. Do not enable semantic extraction or send private files to a model provider without an explicit, scoped request.

For building or refreshing a visual graph, use `graphify-memory-map` instead.
