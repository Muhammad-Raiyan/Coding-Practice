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


my_graph = Graph()

my_graph.add_vertex(5)
my_graph.add_vertex(2)

my_graph.print_graph()

my_graph.add_edge(2, 5)
my_graph.print_graph()