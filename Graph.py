from Vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex: Vertex):
        if isinstance(vertex.value, dict):
            self.graph_dict[vertex.value.get("Name")] = vertex
        else:
            self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight=0):
        self.graph_dict.get(from_vertex.value).add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict.get(to_vertex.value).add_edge(from_vertex.value, weight)

    def filter_by_top_genre(self, genre: str) -> list:
        genre_vertex = self.graph_dict.get(genre)
        games = genre_vertex.get_edges()
        return_list = []
        for game in games:
            return_list.append(self.graph_dict.get(game))
        return return_list
