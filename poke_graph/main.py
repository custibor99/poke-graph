from poke_graph.clients.pokemonapi_client import PokemonApiClient
from poke_graph.models.base_models import Type
from poke_graph.tripletWritters.turtleWritter import TurtleWriter

import os

TTL_TYPES_FILE = "data/types.ttl"
TTL_MOVES_FILE = "data/moves.ttl"
TTL_POKEMON_FILE = "data/pokemon.ttl"
TTL_ITEM_FILE = "data/item.ttl"




def remove_ttl_files():
    ttl_files = [TTL_TYPES_FILE, TTL_MOVES_FILE, TTL_POKEMON_FILE, TTL_ITEM_FILE]
    for file in ttl_files:
        if os.path.exists(file):
            os.remove(file)
def write_ttl_to_file(ttl: str, filepath:str):
    with open(filepath, "w") as file:
        file.write(ttl)



def main():
    client = PokemonApiClient()
    writer = TurtleWriter("http://webprotege.stanford.edu")

    
    """
    #moves
    moves = client.getAllMoves()
    moves_ttl = "\n".join([
        writer.write_move_triplets(move)
        for move in moves
    ])
    write_ttl_to_file(moves_ttl, TTL_MOVES_FILE)

    #types
    types = client.getAllTypes()
    types_ttl = "\n".join([
        writer.write_type_triplets(t)
        for t in types
    ])
    write_ttl_to_file(types_ttl, TTL_TYPES_FILE)
    
    #pokemon and abilities
    pokemon = client.getAllPokemon()
    pokemon_ttl = "\n".join([
        writer.writte_pokemon_triplets(p)
        for p in pokemon
    ])
    write_ttl_to_file(pokemon_ttl, TTL_POKEMON_FILE)
    """

    #items
    items = client.getAllItems()
    items_ttl = "\n".join([
        writer.write_item_triplets(p)
        for p in items
    ])
    write_ttl_to_file(items_ttl, TTL_ITEM_FILE, )
    
if __name__ == "__main__":
    main()



# TODO
# - remove hierarhical structure in ontologies
# - add descriptions to moves, abilities
# - add name or label field to all entities
