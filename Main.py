import json
import os
from Graph import Graph
from Vertex import Vertex

game_graph = Graph(True)

with open("Game_Data.json") as game_data_json:
    game_data = json.load(game_data_json)
game_vertexs = [Vertex(game) for game in game_data]
for game in game_vertexs:
    game_graph.add_vertex(game)

top_level_genres = ["Action", "RPG", "Strategy", "Adventure", "Simulation", "Sports and Racing"]
for g in top_level_genres:
    genre_vertex = Vertex(g)
    game_graph.add_vertex(genre_vertex)
    for game in game_vertexs:
        if g in game.value.get("Genres"):
            game_graph.add_edge(genre_vertex, game)

sub_genres = []
for game in game_data:
    for s_g in game.get("Sub-Genres"):
        if s_g in sub_genres:
            continue
        else:
            sub_genres.append(s_g)
sub_genres.sort()


def main_function():
    print_title()
    genre = get_top_level_genre()
    working_list = game_graph.filter_by_top_genre(genre)
    print_title()
    price_limit = get_price_limit()
    if price_limit != 0:
        filter_by_price(price_limit, working_list)
    print_title()
    include_yes = yes_no("Would you like to specify any sub-genres that a game must be to be included? (1) Yes (2) No: ")
    if include_yes:
        include_list = sub_genre_include()
        filter_by_include(include_list, working_list)
    print_title()
    exclude_yes = yes_no("Would you like to specify any sub-genres that will be used to exclude games? (1) Yes (2) No: ")
    if exclude_yes:
        exclude_list = sub_genre_exclude()
        filter_by_exclude(exclude_list, working_list)
    print_title()
    print_game_list(working_list)
    run_again()


def print_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
     _____ _                         _____                              
    /  ___| |                       |  __ \                             
    \ `--.| |_ ___  __ _ _ __ ___   | |  \/ __ _ _ __ ___   ___         
     `--. \ __/ _ \/ _` | '_ ` _ \  | | __ / _` | '_ ` _ \ / _ \        
    /\__/ / ||  __/ (_| | | | | | | | |_\ \ (_| | | | | | |  __/        
    \____/ \__\___|\__,_|_| |_| |_|  \____/\__,_|_| |_| |_|\___|                                                                                                              
    ______                                                  _           
    | ___ \                                                | |          
    | |_/ /___  ___ ___  _ __ ___  _ __ ___   ___ _ __   __| | ___ _ __ 
    |    // _ \/ __/ _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \ / _` |/ _ \ '__|
    | |\ \  __/ (_| (_) | | | | | | | | | | |  __/ | | | (_| |  __/ |   
    \_| \_\___|\___\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__,_|\___|_|   
    """)


def get_top_level_genre() -> str:
    print("(1) Action (2) Role-Playing-Game\n"
          "(3) Strategy (4) Adventure \n"
          "(5) Simulation (6) Sports and Racing\n")
    top_level_choice = input("What genre of game would you like to play? ")
    if top_level_choice in ["1", "2", "3", "4", "5", "6"]:
        return top_level_genres[int(top_level_choice) - 1]
    else:
        print("Please try again")
        return get_top_level_genre()


def get_price_limit() -> float:
    try:
        print("Do you have a price limit?")
        price_limit = float(input("Enter 0 for no limit or enter a number $0.01-$100.00: $"))
    except ValueError:
        print("Please try again")
        return get_price_limit()
    if price_limit > 100 or price_limit < 0:
        print("Please try again")
        return get_price_limit()
    return price_limit


def sub_genre_include(include_list=None, finished=False) -> list:
    if include_list is None:
        include_list = []
    if finished is True:
        return include_list
    count = 1
    for item in sub_genres:
        print(f"{count}: {item}")
        count += 1
    try:
        index = int(input("Sub-genre to add to included-list? "))
        include_list.append(sub_genres[index - 1])
    except ValueError or IndexError:
        print("Not a valid input")
    finished = get_finished()
    return sub_genre_include(include_list, finished)


def sub_genre_exclude(exclude_list=None, finished=False) -> list:
    if exclude_list is None:
        exclude_list = []
    if finished is True:
        return exclude_list
    count = 1
    for item in sub_genres:
        print(f"{count}: {item}")
        count += 1
    try:
        index = int(input("Sub-genres to add exclude-list? "))
        exclude_list.append((sub_genres[index - 1]))
    except ValueError or IndexError:
        print("Not a valid input")
    finished = get_finished()
    return sub_genre_exclude(exclude_list, finished)


def get_finished() -> bool:
    y_n = input("Add another sub-genre? (1) Yes (2) No: ")
    if y_n == "1":
        return False
    elif y_n == "2":
        return True
    else:
        print("Please try again")
        return get_finished()


def yes_no(text_input: str) -> bool:
    y_n = input(text_input)
    if y_n == "1":
        return True
    elif y_n == "2":
        return False
    else:
        print("Please try again")
        return yes_no(text_input)


def filter_by_price(limit: float, games: list):
    games[:] = [game for game in games if game.value.get("Price") <= limit]


def filter_by_include(include_list: list, games: list):
    games_to_check = games.copy()
    for genre in include_list:
        games_to_check[:] = [game for game in games_to_check if genre not in game.value.get("Sub-Genres")]
    for game in games_to_check:
        games.remove(game)


def filter_by_exclude(exclude_list: list, games: list):
    for genre in exclude_list:
        games[:] = [game for game in games if genre not in game.value.get("Sub-Genres")]


def print_game_list(games):
    for game in games:
        game.print_self()


def run_again():
    again = input("Would you like to get another game? (1) Yes (2) No: ")
    if again == "1":
        main_function()
    elif again == "2":
        print("Goodbye!")
    else:
        print("Please try again")
        run_again()


main_function()
