from queue import Queue
from typing import List

class Solution:
    def adj_ls(self, edges: List[List[int]], V: int) -> List[List[int]]:
        ls = [[] for _ in range(V)]
        for edge in edges:
            a, b = edge
            ls[a].append(b)
            ls[b].append(a)
        return ls

    def bfs_traverse(self, V: int, adj: List[List[int]], start_node: int, visited: List[int]) -> List[int]:
        q = Queue(maxsize=V)
        q.put(start_node)
        visited[start_node] = 1
        bfs = []

        while not q.empty():
            front_node = q.get()
            bfs.append(front_node)

            for node in adj[front_node]:
                if visited[node] == 0:
                    visited[node] = 1
                    q.put(node)
        
        return bfs

    def is_complete_component(self, nodes: List[int], adj: List[List[int]]) -> bool:
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                if nodes[j] not in adj[nodes[i]]:
                    return False
        return True

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        component_count = 0
        visited = [0] * n
        adj = self.adj_ls(edges, n)

        for node in range(n):
            if visited[node] == 0:
                component_nodes = self.bfs_traverse(n, adj, node, visited)
                if self.is_complete_component(component_nodes, adj):
                    component_count += 1
        
        return component_count
