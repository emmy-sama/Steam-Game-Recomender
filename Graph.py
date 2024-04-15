class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if isinstance(vertex.value, dict):
            self.graph_dict[vertex.value.get("Name")] = vertex
        else:
            self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict.get(from_vertex.value).add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict.get(to_vertex.value).add_edge(from_vertex.value, weight)

    def print_top_level_genre(self):
        for key, value in self.graph_dict.items():
            if key in ["Action", "RPG", "Strategy", "Adventure", "Simulation", "Sports and Racing"]:
                print(key)
                print(value.get_edges())

    def filter_by_top_genre(self, genre):
        genre_vertex = self.graph_dict.get(genre)
        games = genre_vertex.get_edges()
        return_list = []
        for game in games:
            return_list.append(self.graph_dict.get(game))
        return return_list
