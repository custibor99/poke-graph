import requests
import functools

from typing import Optional
from poke_graph.models.base_models import Pokemon, Type, Move
from tqdm import tqdm

class PokemonApiClient:
    def __init__(self, base_url:str = "https://pokeapi.co/api/v2/"):
        self.base_url = base_url
        self.pokemon_endpoint_url = f"{self.base_url}pokemon/"
        
    @functools.cache
    def getPokemonByName(self, name:str) -> Pokemon | None:
        response = requests.get(self.pokemon_endpoint_url+name)
        if response.status_code != 200:
            return None
        return Pokemon.from_dict(response.json())
    
    
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
        return Type.from_dict(response.json())

    def getAllTypes(self):
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
        return Move.from_dict(response.json())
    
    def getAllMoves(self) -> Move | None:
        response = requests.get(f"{self.base_url}/move?limit=3000&offset=0")
        result = []
        if response.status_code != 200:
            return result
        for el in tqdm(response.json()["results"], desc="FETCHING MOVES: "):
            result.append(self.getMoveByName(el["name"]))
        return result



def main():
    client = PokemonApiClient()
    res = client.getAllMoves()
    print(res)
if __name__=="__main__":
    main()