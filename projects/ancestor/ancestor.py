import copy
from util import Stack, Queue  # These may come in handy

# run a standard DFT, but recurse with distance to track the earliest ancestor found
# iterate over the pairs of nodes
# find those that are direct parents


def add_vertex(vertices, vertex_id):
    """
    Add a vertex to the graph.
    """
    if vertices.get(vertex_id) is None:
        vertices[vertex_id] = set()


def add_edge(vertices, v1, v2):
    """
    Add a directed edge to the graph.
    """
    if v1 and v2 in vertices:
        vertices[v1].add(v2)
    else:
        raise IndexError("vertex does not exist")


def get_neighbors(vertices, vertex_id):
    """
    Get all neighbors (edges) of a vertex.
    """
    return vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node, distance=0):
    # # call BFT or DFT
    # dft(ancestors, starting_node)
    # # if the earliest ancestor returned is the same as the starting node, return -1

    # Set up graph
    vertices = {}
    # Create a stack
    stack = Stack()

    for pair in ancestors:
        add_vertex(vertices, pair[0])
        add_vertex(vertices, pair[1])
        add_edge(vertices, pair[1], pair[0])

    # push path to the starting node
    path = [starting_node]
    stack.push(path)

    # Create a set to store vertices
    visited = set()

    # Create a list to store path to earliest ancestor
    longest_path = []

    while stack.size() > 0:
        old_path = stack.pop()

        last = old_path[-1]

        if len(longest_path) == len(old_path) and last < longest_path[-1]:
            longest_path = old_path

        # Find longest path
        if len(longest_path) < len(old_path):
            longest_path = old_path

        # If vertex is not visited
        # Mark as visited
        if last not in visited:
            visited.add(last)

            for neighbor in get_neighbors(vertices, last):
                path = copy.copy(old_path)

                path.append(neighbor)

                stack.push(path)

    if len(longest_path) == 1:
        return -1

    else:
        return longest_path[-1]
