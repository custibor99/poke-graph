import requests
import functools

from poke_graph.models.base_models import Pokemon, Type, Move, Item
from tqdm import tqdm
import cattrs
import json

class PokemonApiClient:
    def __init__(self, base_url:str = "https://pokeapi.co/api/v2/"):
        self.base_url = base_url
        
    @functools.cache
    def getPokemonByName(self, name:str) -> Pokemon | None:
        response = requests.get(f"{self.base_url}/pokemon/{name}")
        if response.status_code != 200:
            return None
        return Pokemon.from_api_dict(response.json())
    
    
    def getAllPokemon(self) -> list[Pokemon]:
        response = requests.get(self.base_url+"pokemon?limit=3000&offset=0")
        result = []
        if response.status_code != 200:
            return result
        
        for el in tqdm(response.json()["results"], desc="FETCH POKEMON: "):
            result.append(self.getPokemonByName(el["name"]))
        return result
    
    @functools.cache
    def getTypeByName(self, name:str) -> Type | None:
        response = requests.get(f"{self.base_url}/type/{name}")
        if response.status_code != 200:
            return None
        return Type.from_api_dict(response.json())

    def getAllTypes(self) -> list[Type]:
        response = requests.get(self.base_url+"type?limit=30&offset=0")
        result = []
        if response.status_code != 200:
            return result
        for el in tqdm(response.json()["results"], desc="FETCH TYPES: "):
            result.append(self.getTypeByName(el["name"]))
        return result
    
    @functools.cache
    def getMoveByName(self, name: str) -> Move | None:
        response = requests.get(f"{self.base_url}/move/{name}")
        if response.status_code != 200:
            return None
        return Move.from_api_dict(response.json())
    
    def getAllMoves(self) -> list[Move]:
        response = requests.get(f"{self.base_url}/move?limit=3000&offset=0")
        result = []
        if response.status_code != 200:
            return result
        for el in tqdm(response.json()["results"], desc="FETCHING MOVES: "):
            result.append(self.getMoveByName(el["name"]))
        return result
    
    @functools.cache
    def getItemByName(self, name) -> Item | None:
        response = requests.get(f"{self.base_url}/item/{name}")
        if response.status_code != 200:
            return None
        return Item.from_api_dict(response.json())
    

    def getAllItems(self) -> list[Item]:
        response = requests.get(f"{self.base_url}/item?limit=3000&offset=0")
        result = []
        if response.status_code != 200:
            return result
        for el in tqdm(response.json()["results"], desc="FETCHING ITEMS: "):
            result.append(self.getItemByName(el["name"]))
        return result


def main():
    client = PokemonApiClient()
    #Get pokemon
    entity = client.getPokemonByName("magnemite")
    print(entity.to_json_string())

    #Get move
    entity = client.getMoveByName("pound")
    print(entity.to_json_string())

    #Get move
    entity = client.getItemByName("nugget")
    print(entity.to_json_string())

    #Get ability
    entity = client.getTypeByName("fire")
    print(entity.to_json_string())

if __name__=="__main__":
    main()