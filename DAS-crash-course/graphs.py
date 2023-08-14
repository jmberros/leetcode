from collections import defaultdict


def build_graph(
    edges: list[tuple[int, int]],
    directed: bool = False
) -> dict[int: list[int]]:
    """Builds a graph as a HashMap of node -> neighbors.

    Args:
        edges: A list of tuples (int, int), which represent connections between nodes.
        directed: Whether this is directed graph
    Returns:
        A dictionary of neighborhood relations.
    """
    neighbors = defaultdict(list)
    for a, b in edges:
        neighbors[a].append(b)
        if not directed:
            neighbors[b].append(a)
    return dict(neighbors)


if __name__ == "__main__":
    edges = [(1, 2), (2, 3), (2, 4), (2, 5), (1, -1), (-1, -2)]
    graph = build_graph(edges)
    print(graph)
    adjs = [[2], [3, 4, 5]]
    print(adjs)
