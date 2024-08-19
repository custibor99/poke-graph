from poke_graph.clients.pokemonapi_client import PokemonApiClient
from poke_graph.models.base_models import Type
from poke_graph.tripletWritters.turtleWritter import TurtleWriter

import os

TTL_TYPES_FILE = "data/types.ttl"
TTL_MOVES_FILE = "data/moves.ttl"


def remove_ttl_files():
    ttl_files = [TTL_TYPES_FILE, TTL_MOVES_FILE]
    for file in ttl_files:
        if os.path.exists(file):
            os.remove(file)
def write_ttl_to_file(ttl: str, filepath:str):
    with open(filepath, "w") as file:
        file.write(ttl)



def main():
    client = PokemonApiClient()
    writer = TurtleWriter("http://webprotege.stanford.edu")

    

    moves = client.getAllMoves()
    moves_ttl = "\n".join([
        writer.write_move_triplets(move)
        for move in moves
    ])
    write_ttl_to_file(moves_ttl, TTL_MOVES_FILE)

    types = client.getAllTypes()
    types_ttl = "\n".join([
        writer.write_type_triplets(t)
        for t in types
    ])
    write_ttl_to_file(types_ttl, TTL_TYPES_FILE)


    
if __name__ == "__main__":
    main()



# TODO
# - remove hierarhical structure in ontologies
# - add descriptions to moves, abilities
# - add name or label field to all entities
