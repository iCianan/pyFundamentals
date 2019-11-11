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
    
    def DFS(self, start, results = [], visited = {}):
        if self.adjacencyList[start] is None:
            return
        results.append(start)
        visited[start] = True
        for neighbor in self.adjacencyList[start]:
            if neighbor not in visited:
                self.DFS(neighbor, results, visited)
        return results




def main():
    graph = Graph()
    graph.addVertex('Bitcoin')
    graph.addVertex('0x')
    graph.addVertex('Cardano')
    graph.addVertex('Horizen')
    graph.addVertex('Ethereum')
    graph.addVertex('Monero')
    graph.addEdges('Bitcoin', 'Ethereum')
    graph.addEdges('Bitcoin', 'Horizen')
    graph.addEdges('Bitcoin', 'Cardano')
    graph.addEdges('Bitcoin', 'Monero')
    graph.addEdges('Cardano', 'Horizen')
    graph.addEdges('Cardano', 'Ethereum')    
    graph.addEdges('Ethereum', '0x')
    graph.addEdges('Monero', 'Horizen')
    print(graph.BFS('Monero'))
    print(graph.DFS('Monero'))


if __name__ == "__main__":
    main()
