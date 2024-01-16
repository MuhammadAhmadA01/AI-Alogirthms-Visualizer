class Graph_dls:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def depth_limited_search(self, start_node, goal_node, depth_limit=5):
        visited = set()
        path = []
        
        if self.graphType == "Undirected Graph":
            return self.dls_recursive_undirected(start_node, goal_node, depth_limit, visited, path)
        else:
            return self.dls_recursive_directed(start_node, goal_node, depth_limit, visited, path)

    def dls_recursive_undirected(self, current_node, goal_node, visited, path,depth_limit =5):
        if current_node == goal_node:
            path.append(current_node)
            return path

        if depth_limit == 0:
            return []

        visited.add(current_node)
        path.append(current_node)

        if current_node not in self.graph:
            return []

        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                result = self.dls_recursive_undirected(neighbor, goal_node,  visited, path,depth_limit - 1)
                if result:
                    return result

        path.pop()
        visited.remove(current_node)

        return []

    def dls_recursive_directed(self, current_node, goal_node,  visited, path,depth_limit=5):
        if current_node == goal_node:
            path.append(current_node)
            return path

        if depth_limit == 0:
            return []

        visited.add(current_node)
        path.append(current_node)

        if current_node not in self.graph:
            return []

        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                result = self.dls_recursive_directed(neighbor, goal_node,  visited, path,depth_limit - 1)
                if result:
                    return result

        path.pop()
        visited.remove(current_node)

        return []
