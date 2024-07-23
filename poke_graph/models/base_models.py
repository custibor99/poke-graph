from dataclasses import dataclass, field
from enum import Enum

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
    

@dataclass
class Type:
    name: str
    double_damage_to: list[str]
    half_damage_to: list[str]
    no_damage_to: list[str]

    @classmethod
    def from_dict(cls, data):
        relations = data["damage_relations"]
        return Type(
            name=data["name"],
            half_damage_to= [type["name"] for type in relations["half_damage_to"]],
            double_damage_to= [type["name"] for type in relations["double_damage_to"]],
            no_damage_to= [type["name"] for type in relations["no_damage_to"]],
        )

@dataclass
class Move:
    name: str
    move_type: str
    pp: int
    accuracy: int
    damage_class: str
    power: int = 0
    priority: int = 0
    effect_chance: int = 0
    drain: int = 0
    crit_rate: int = 0
    flinch_chance: int = 0
    healing: int = 0
    stat_changes: dict = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data):
        stat_changes = {
            el["stat"]["name"]:el["change"]
            for el in data["stat_changes"]
        }
        try:
            return Move(
            name = data["name"],
            move_type = data["type"]["name"],
            pp = data["pp"],
            accuracy = data["accuracy"] if data["accuracy"] is not None else 100,
            priority = data["priority"],
            damage_class = data["damage_class"]["name"],
            power = data["power"] if data["power"] != None else 0,
            crit_rate=data["meta"].get("crit_rate", 0),
            drain = data["meta"]["drain"],
            flinch_chance=data["meta"]["flinch_chance"],
            healing = data["meta"]["healing"],
            stat_changes=stat_changes,
        )
        except:
            print(data["name"]) #example pounce
     


    
