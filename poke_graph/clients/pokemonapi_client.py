import requests
import functools
from dataclasses import dataclass

from typing import Optional



class PokemonApiClient:
    def __init__(self, base_url:str = "https://pokeapi.co/api/v2/"):
        self.base_url = base_url
        self.pokemon_endpoint_url = f"{self.base_url}pokemon/"
        
    @functools.cache
    def getPokemonByName(self, name:str) -> Optional[dict]:
        response = requests.get(self.pokemon_endpoint_url+name)
        if response.status_code != 200:
            return None
        return Pokemon.from_dict(response.json())

@dataclass
class Stats:
    hp: int
    attack: int
    defense: int
    speed: int
    sp_attack: int
    sp_defense: int

    @classmethod
    def from_dict(cls, data):
        hp = 0
        attack = 0
        defense = 0
        speed = 0
        sp_attack = 0
        sp_defense = 0
        
        for el in data:
            if el["stat"]["name"] == "hp":
                hp = el["base_stat"]
            if el["stat"]["name"] == "attack":
                attack = el["base_stat"]
            if el["stat"]["name"] == "defense":
                defense = el["base_stat"]
            if el["stat"]["name"] == "special-attack":
                sp_attack = el["base_stat"]
            if el["stat"]["name"] == "special-defense":
                sp_defense = el["base_stat"]
            if el["stat"]["name"] == "speed":
                speed = el["base_stat"]

        return Stats(hp, attack, defense, speed, sp_attack, sp_defense)

    def stats_total(self) -> int:
        return self.hp + self.attack + self.sp_attack + self.defense + self.sp_defense + self.speed

@dataclass
class Pokemon:
    name: str
    abilities: list[str]
    moves: list[str]
    types: list[str]
    weight: int
    stats: Stats

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        abilities = [ el["ability"]["name"] for el in data["abilities"]]
        moves = [ el["move"]["name"] for el in data["moves"]]
        types = [ el["type"]["name"] for el in data["types"]]
        weight = data["weight"]
        stats = Stats.from_dict(data["stats"])
        return Pokemon(name, abilities, moves, types, weight, stats)



def main():
    client = PokemonApiClient()
    res = client.getPokemonByName("magnemite")
    print(res)



if __name__=="__main__":
    main()