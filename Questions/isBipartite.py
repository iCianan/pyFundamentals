# Given an undirected graph, return true if and only if it is bipartite.
# Recall that a graph is bipartite if we can split it's set of nodes into two 
# independent subsets A and B such that every edge in the graph has one node in A and another node in B.
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  
# Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] 
# does not contain i, and it doesn't contain any element twice.
#  Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true


def isBipartite(graph) -> bool:
    color = {}
    def dfs(pos):
        for edge in graph[pos]:
            if edge in color:
                if color[edge] == color[pos]:
                    return False
            else:
                 color[edge] = 1- color[pos]
                 if not dfs(edge):
                     return False
        return True
    for edge in range(len(graph)):
        if edge not in color:
            color[edge] = 0
            if not dfs(edge):
                return False
    return True

def main():
    input = [[1,3], [0,2], [1,3], [0,2]]
    print(isBipartite(input))
    
if __name__ == "__main__":
    main()