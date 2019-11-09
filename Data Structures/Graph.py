from collections import deque

class Graph:
    def __init__(self):
        self.adjacencyList = {}
        self.length = 0

    def addVertex(self, node):
        if node not in self.adjacencyList:
            self.adjacencyList[node] = []
            self.length += 1

    def addEdges(self, u, v):
        if u in self.adjacencyList and v in self.adjacencyList:
            self.adjacencyList[u].append(v)
            self.adjacencyList[v].append(u)

    def BFS(self, vertex):
        queue = deque()
        visited = []
        queue.append(vertex)
        while len(queue):
            current = queue.popleft()
            if current not in visited:
                visited.append(current)
                neighbors = self.adjacencyList[current]
                for neighbor in neighbors:
                    queue.append(neighbor)
        return visited




def main():
    graph = Graph()
    graph.addVertex('Bitcoin')
    graph.addVertex('Litecoin')
    graph.addVertex('ZCash')
    graph.addVertex('Horizen')
    graph.addVertex('Ethereum')
    graph.addEdges('Bitcoin', 'Litecoin')
    graph.addEdges('Litecoin', 'ZCash')
    graph.addEdges('ZCash', 'Horizen')
    graph.addEdges('Ethereum', 'Horizen')
    print(graph.BFS('ZCash'))


if __name__ == "__main__":
    main()
