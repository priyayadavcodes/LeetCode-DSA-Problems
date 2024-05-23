from queue import Queue
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        mat = isConnected
        def adj_ls(elf,mat:List[List[int]]):

            ls = [[] for j in range(len(isConnected))]
            for i in range(len(isConnected)):
                for j in range(len(isConnected)):
                    if i != j:
                        if isConnected[i][j] == 1:
                            ls[i].append(j)
            return ls
        

        def bfs_traverse(self, V:int,adj: List,start_node:int, visited:int):
            q = Queue(maxsize = V)
            q.put(start_node)
            visited[start_node] = 1
            bfs = []
       
            while (q.empty() == False):
                front_node = q.get()
                bfs.append(front_node)

                for node in adj[front_node]:
                    if visited[node] == 0:
                        visited[node] = 1
                        q.put(node)
            return bfs,visited

        component_count = 0
        adj = adj_ls(self,mat)
        n = len(adj)
        V = n
        visited = [0 for i in range(V)]

        for node in range(V):
            if visited[node]==0:
                component_count = component_count + 1
                _,visited = bfs_traverse(self,V,adj,node,visited)
        return (component_count)
        


            


     
        
        