"""Render a navigable Graphify view with representative nodes from each repo.

Run with a Python environment containing graphifyy and networkx. The input
graph is read-only. Cross-repo edges are omitted because matching symbol names
alone do not establish a real dependency.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from networkx.readwrite import json_graph

from graphify.exporters.html import to_html


def project_of(node: str, attrs: dict) -> str:
    return str(attrs.get("repo") or str(node).split("::", 1)[0])


def render(source: Path, output: Path, per_project: int) -> tuple[int, int, int, int, int]:
    raw = json.loads(source.read_text(encoding="utf-8"))
    graph = json_graph.node_link_graph(raw, edges="links")
    projects: dict[str, list[str]] = defaultdict(list)
    for node, attrs in graph.nodes(data=True):
        projects[project_of(node, attrs)].append(node)

    selected: set[str] = set()
    for nodes in projects.values():
        nodes.sort(key=lambda node: (-graph.degree(node), str(node)))
        selected.update(nodes[:per_project])

    view = graph.subgraph(selected).copy()
    for start, end in list(view.edges()):
        if project_of(start, view.nodes[start]) != project_of(end, view.nodes[end]):
            view.remove_edge(start, end)

    names = sorted(projects)
    communities = {
        index: [node for node in view if project_of(node, view.nodes[node]) == name]
        for index, name in enumerate(names)
    }
    labels = dict(enumerate(names))
    output.parent.mkdir(parents=True, exist_ok=True)
    if not to_html(view, communities, str(output), community_labels=labels, node_limit=5000):
        raise RuntimeError("Graphify did not write the interactive view")
    return len(names), graph.number_of_nodes(), graph.number_of_edges(), view.number_of_nodes(), view.number_of_edges()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, required=True, help="Full Graphify graph.json")
    parser.add_argument("--output", type=Path, required=True, help="Destination HTML file")
    parser.add_argument("--per-project", type=int, default=180, help="Maximum visible nodes per project")
    args = parser.parse_args()
    if args.per_project < 1:
        parser.error("--per-project must be positive")
    counts = render(args.graph, args.output, args.per_project)
    print(
        f"projects={counts[0]} full_nodes={counts[1]} full_edges={counts[2]} "
        f"view_nodes={counts[3]} view_edges={counts[4]} output={args.output}"
    )


if __name__ == "__main__":
    main()
