class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return False
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return False
        if v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)

        return True

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            return False
        edge_list = self.adj_list[vertex]

        for edge in edge_list:
            self.adj_list[edge].remove(vertex)

        self.adj_list[vertex] = []


my_graph = Graph()

my_graph.add_vertex(5)
my_graph.add_vertex(2)
my_graph.add_vertex(1)

my_graph.print_graph()

my_graph.add_edge(2, 5)

my_graph.add_edge(2, 1)
my_graph.print_graph()

print("removing vertex")
my_graph.remove_vertex(1)
my_graph.print_graph()
