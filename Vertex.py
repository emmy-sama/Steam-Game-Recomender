class Vertex:
    def __init__(self, value: any):
        self.value = value
        self.edges = {}

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
