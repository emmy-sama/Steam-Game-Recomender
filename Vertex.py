class Vertex:
    def __init__(self, value: any):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex_value: any, weight=0):
        if isinstance(vertex_value, dict):
            self.edges[vertex_value.get("Name")] = weight
        else:
            self.edges[vertex_value] = weight

    def get_edges(self) -> list:
        return list(self.edges.keys())

    def print_self(self) -> None:
        if isinstance(self.value, dict):
            data = self.value
            print("--------------------------------------------------")
            for key, value in data.items():
                if key == "Rating":
                    print(f"{key}: {value}%")
                elif key == "Genres" or key == "Sub-Genres":
                    print(f"{key}: {", ".join(value)}")
                elif key == "Price":
                    if value > 0:
                        print(f"{key}: ${value}")
                    else:
                        print(f"{key}: Free-To-Play")
                else:
                    print(f"{key}: {value}")
        else:
            return
