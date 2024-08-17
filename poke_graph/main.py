from poke_graph.clients.pokemonapi_client import PokemonApiClient
from poke_graph.models.base_models import Type
from poke_graph.turtlewritter.writers import TypeWritter, MoveWritter

import os

TTL_TYPES_FILE = "data/types.ttl"
TTL_MOVES_FILE = "data/moves.ttl"


def remove_ttl_files():
    ttl_files = [TTL_TYPES_FILE, TTL_MOVES_FILE]
    for file in ttl_files:
        if os.path.exists(file):
            os.remove(file)


def write_ttl_moves_file(client:PokemonApiClient):
    typeWritter = MoveWritter("http://webprotege.stanford.edu")
    moves = client.getAllMoves()
    ttls = ""

    for el in moves:
        ttls += typeWritter.write_move_triplets(el)

    with open(TTL_MOVES_FILE, "w") as file:
        file.write(ttls)


def write_ttl_types_file(client:PokemonApiClient):
    typeWritter = TypeWritter("http://webprotege.stanford.edu")
    all_types = client.getAllTypes()
    types_ttl = ""

    for type in all_types:
        types_ttl += typeWritter.write_type_triplets(type)

    with open(TTL_TYPES_FILE, "w") as file:
        file.write(types_ttl)



def main():
    client = PokemonApiClient()
    #write_ttl_types_file(client)
    write_ttl_moves_file(client)
if __name__ == "__main__":
    main()



# TODO
# - remove hierarhical structure in ontologies
# - add descriptions to moves, abilities
# - add name or label field to all entities
