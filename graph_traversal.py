from collections import defaultdict, deque
import time


class Graph:
    def __init__(self):
        # Dictionary to store the adjacency list
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        """Adds a vertex if it does not already exist."""
        _ = self.graph[vertex]

    def add_edge(self, u, v, directed=True):
        """Adds an edge to the graph."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        if not directed:
            # If the graph is undirected, add the reverse edge
            self.graph[v].append(u)

    def vertices(self):
        """Returns all vertices in the graph."""
        return list(self.graph.keys())

    def edges(self):
        """Returns all directed edges as (u, v) pairs."""
        result = []
        for u in self.graph:
            for v in self.graph[u]:
                result.append((u, v))
        return result

    def dfs(self, start_vertex):
        """
        Depth-First Search (DFS)
        Time Complexity: O(V + E)
        """
        if start_vertex not in self.graph:
            return []

        visited = set()
        traversal_path = []

        def dfs_recursive(vertex):
            # Mark the current node as visited and add to path
            visited.add(vertex)
            traversal_path.append(vertex)

            # Recur for all the vertices adjacent to this vertex
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)
        return traversal_path

    def dfs_stack(self, start_vertex):
        """
        Depth-First Search (DFS) using an explicit stack.
        Time Complexity: O(V + E)
        """
        if start_vertex not in self.graph:
            return []

        visited = set()
        stack = [start_vertex]
        traversal_path = []

        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue

            visited.add(vertex)
            traversal_path.append(vertex)

            # Reverse push keeps traversal order deterministic for demo output.
            for neighbor in reversed(self.graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

        return traversal_path

    def bfs(self, start_vertex):
        """
        Breadth-First Search (BFS)
        Time Complexity: O(V + E)
        """
        if start_vertex not in self.graph:
            return []

        visited = set()
        queue = deque([start_vertex])

        # Mark the source node as visited
        visited.add(start_vertex)
        traversal_path = []

        while queue:
            # Dequeue a vertex from queue
            vertex = queue.popleft()
            traversal_path.append(vertex)

            # Get all adjacent vertices. If an adjacent vertex hasn't
            # been visited, mark it visited and enqueue it.
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_path

    def shortest_path(self, start_vertex, target_vertex):
        """
        Returns the shortest path in an unweighted graph using BFS.
        If unreachable, returns an empty list.
        """
        if start_vertex not in self.graph or target_vertex not in self.graph:
            return []

        queue = deque([start_vertex])
        visited = {start_vertex}
        parent = {start_vertex: None}

        while queue:
            current = queue.popleft()
            if current == target_vertex:
                break

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        if target_vertex not in parent:
            return []

        # Reconstruct path from target to start.
        path = []
        cur = target_vertex
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        return path


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a value into the BST."""
        if self.root is None:
            self.root = TreeNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right
            else:
                return

    def build_from_list(self, values):
        for value in values:
            self.insert(value)

    def search(self, target):
        """Returns True if target exists in the BST."""
        current = self.root
        while current is not None:
            if target < current.value:
                current = current.left
            elif target > current.value:
                current = current.right
            else:
                return True
        return False

    def inorder_traversal(self):
        """Left -> Root -> Right"""
        result = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            result.append(node.value)
            inorder(node.right)

        inorder(self.root)
        return result

    def preorder_traversal(self):
        """Root -> Left -> Right"""
        result = []

        def preorder(node):
            if node is None:
                return
            result.append(node.value)
            preorder(node.left)
            preorder(node.right)

        preorder(self.root)
        return result

    def postorder_traversal(self):
        """Left -> Right -> Root"""
        result = []

        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.value)

        postorder(self.root)
        return result

    def level_order_traversal(self):
        """BFS traversal on tree levels."""
        if self.root is None:
            return []

        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result

    def height(self):
        """Returns tree height, where empty tree is -1."""

        def get_height(node):
            if node is None:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))

        return get_height(self.root)


def _format_path(path):
    return " ".join(str(node) for node in path)


def run_assignment5_demo():
    print("=" * 62)
    print("作業 5：圖與樹走訪（DFS vs BFS）")
    print("時間複雜度：O(V + E)")
    print("=" * 62)
    print()
    print("        [A]")
    print("       /   \\")
    print("     [B]   [C]")
    print("    / \\    / \\")
    print("  [D] [E] [F] [G]")
    print()

    # Use a directed graph to model parent -> children tree relationships.
    demo_graph = Graph()
    demo_graph.add_edge("A", "B")
    demo_graph.add_edge("A", "C")
    demo_graph.add_edge("B", "D")
    demo_graph.add_edge("B", "E")
    demo_graph.add_edge("C", "F")
    demo_graph.add_edge("C", "G")

    start_ns = time.perf_counter_ns()
    dfs_path = demo_graph.dfs_stack("A")
    dfs_elapsed_ns = time.perf_counter_ns() - start_ns

    print("--- 1. 深度優先搜尋（DFS）- 使用堆疊 ---")
    print(f"走訪路徑：{_format_path(dfs_path)}")
    print(f"[耗時 (O(V+E))：{dfs_elapsed_ns} ns]")
    print()

    start_ns = time.perf_counter_ns()
    bfs_path = demo_graph.bfs("A")
    bfs_elapsed_ns = time.perf_counter_ns() - start_ns

    print("--- 2. 廣度優先搜尋（BFS）- 使用佇列 ---")
    print(f"走訪路徑：{_format_path(bfs_path)}")
    print(f"[耗時 (O(V+E))：{bfs_elapsed_ns} ns]")


def run_extended_demo():
    print("\n" + "=" * 62)
    print("進階示範：Graph + 二元搜尋樹")
    print("=" * 62)

    print("\n[圖結構功能]")
    g = Graph()

    # Adding edges to form a sample graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(f"DFS（遞迴）起點 2：{g.dfs(2)}")
    print(f"DFS（堆疊）起點 2：{g.dfs_stack(2)}")
    print(f"BFS 起點 2：{g.bfs(2)}")
    print(f"頂點：{g.vertices()}")
    print(f"邊：{g.edges()}")
    print(f"從 2 到 1 的最短路徑：{g.shortest_path(2, 1)}")

    print("\n[BST 樹結構功能]")
    bst = BinarySearchTree()
    bst.build_from_list([10, 5, 15, 2, 7, 12, 20])

    print(f"查找 12：{bst.search(12)}")
    print(f"查找 99：{bst.search(99)}")
    print(f"中序：{bst.inorder_traversal()}")
    print(f"前序：{bst.preorder_traversal()}")
    print(f"後序：{bst.postorder_traversal()}")
    print(f"層序：{bst.level_order_traversal()}")
    print(f"樹高：{bst.height()}")


# --- Example Usage ---
if __name__ == "__main__":
    run_assignment5_demo()
    run_extended_demo()
