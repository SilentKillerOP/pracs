class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def dfs(self, u, t, visited, parent):
        visited[u] = True
        if u == t:
            return True, parent
        for ind, val in enumerate(self.graph[u]):
            if not visited[ind] and val > 0:
                parent[ind] = u
                found_path, parent = self.dfs(ind, t, visited, parent)
                if found_path:
                    return True, parent
        return False, parent


    def ford_fulkerson(self, source, sink):
        max_flow = 0
        parent = [-1] * self.ROW
        while True:
            visited = [False] * self.ROW
            found_path, parent = self.dfs(source, sink, visited, parent)
            if not found_path:
                break
            path_flow = float("Inf")
            s = sink
            path = [sink]
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
                path.insert(0, s)

            max_flow += path_flow

            print("Augmented path: ", " -> ".join(str(x) for x in path), " Minimum value: ", path_flow)

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow   
                v = u
        return max_flow



graph = [[0, 16, 0, 13, 0, 0],
         [0, 0, 12, 0, 0, 0],
         [0, 0, 0, 9, 0, 20],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 7, 0, 0, 4],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Max Flow: %d " % g.ford_fulkerson(source, sink))
