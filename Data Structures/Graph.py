class Graph:
    def __init__(self):
        self.adjacencyList = {}
        self.length = 0

    def addVertex(self, node):
        if node not in self.adjacencyList:
            self.adjacencyList[node] = []
            self.length += 1

    def addEdges(self, node1, node2):
        if node1 in self.adjacencyList and node2 in self.adjacencyList:
            self.adjacencyList[node1].append(node2)
            self.adjacencyList[node2].append(node1)


def main():
    graph = Graph()
    graph.addVertex('Bitcoin')
    graph.addVertex('Litcoin')
    graph.addVertex('ZCash')
    graph.addVertex('Horizen')
    graph.addVertex('Ethereum')
    graph.addEdges('Bitcoin', 'Litecoin')
    print(graph.length)


if __name__ == "__main__":
    main()
