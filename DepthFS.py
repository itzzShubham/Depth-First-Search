from collections import defaultdict
class dfsgraph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, a, b):
        self.graph[a].append(b)
    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)
    def _dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)

g = dfsgraph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(3, 4)
g.add_edge(4, 4)
print("DFS Traversal: ")
g.dfs(1)