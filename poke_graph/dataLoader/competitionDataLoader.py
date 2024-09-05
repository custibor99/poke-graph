import json
from dataclasses import dataclass
from datetime import datetime
from poke_graph.models.base_models import Pokemon
import re


class CompetitionDataLoader:
    def __init__(self):
        pass

    def load(self, filepath:str):

        players = []
        teams = []
        rounds = []
        competition_prefix = filepath.split("/")[-1].split(",")[0].lower().replace(" ", "-")
        with open(filepath, "r") as file:
            data = json.load(file)
            #For player
            for el in data:
                name = el["name"]
                first_name = re.sub(r"[\W]", "", name.split(" ")[0].lower().replace(" ", "-"))
                last_name = re.sub(r"[\W]", "", "-".join(name.split(" ")[1:-1]).lower(),)
                country = name.split(" ")[-1][1:-1].lower().replace(" ", "-")
                player = Player(
                    first_name,
                    last_name,
                    country
                )
                players.append(player)
                player_id = f"{player.first_name}-{player.last_name}-{player.country}"
                
                #Team members
                members = []
                for pokemon in el["decklist"]:
                    member = TeamMember(
                        parse_pokemon_names(pokemon["name"]),
                        parse_moves(pokemon["badges"]),
                        pokemon["ability"].lower().replace(" ", "-"),
                        pokemon["item"].lower().replace(" ", "-"),
                        pokemon["teratype"].lower()
                    )
                    members.append(member)
                
                #Build team
                team = Team(
                    f"{player_id}-{competition_prefix}",
                    player,
                    members,
                    int(el["record"]["losses"]),
                    int(el["record"]["ties"]),
                    int(el["record"]["wins"]),
                    int(el["placing"]),
                )
                teams.append(team) 

                #Build rounds
                for _, round in el["rounds"].items():
                    name = round["name"]
                    player2 = Player(
                        name.split(" ")[0].lower().replace(" ", "-"),
                        "-".join(name.split(" ")[1:-1]).lower(),
                        name.split(" ")[-1][1:-1].lower().replace(" ", "-")
                    )
                    rounds.append(Round(
                        player1=player,
                        player2=player2,
                        result=round["result"]
                    ))
                           

        return Competition(
            competition_prefix,
            teams,
            rounds
        )


def parse_pokemon_names(name:str) -> str:
    name = name.lower()
    if "kyurem" in name and "black" in name:
        return "kyurem-black"
    if "kyurem" in name and "white" in name:
        return "kyurem-white"
    if "ogerpon" in name and "cornerstone" in name:
        return "ogerpon-cornerstone-mask"
    if "ogerpon" in name and "hearthflame" in name:
        return "ogerpon-hearthflame-mask"
    if "ogerpon" in name and "wellspring" in name:
        return "ogerpon-wellspring-mask"
    if "urshifu" in name and "single" in name:
        return "urshifu-single-strike"
    if "urshifu" in name and "rapid" in name:
        return "urshifu-rapid-strike"
    if "urshifu" in name and "rapid" in name:
        return "urshifu-rapid-strike"
    if "zamazenta" in name and "crowned" in name:
        return "zamazenta-crowned"
    if "zacian" in name and "crowned" in name:
        return "zacian-crowned"
    
    if "tornadus" in name and "incarnate" in name:
        return "tornadus-incarnate"
    if "tornadus" in name and "therian" in name:
        return "tornadus-therian"
    
    if "thundurus" in name and "incarnate" in name:
        return "thundurus-incarnate"
    if "thundurus" in name and "therian" in name:
        return "thundurus-therian"
    
    if "landorus" in name and "incarnate" in name:
        return "landorus-incarnate"
    if "landorus" in name and "therian" in name:
        return "landorus-therian"
    
    if "enamorus" in name and "incarnate" in name:
        return "enamorus-incarnate"
    if "enamorus" in name and "therian" in name:
        return "enamorus-therian"
    
    if "tauros" in name and "aqua" in name:
        return "tauros-paldea-aqua-breed"
    if "tauros" in name and "blaze" in name:
        return "tauros-paldea-blaze-breed"
    
    if "rotom" in name and "mow" in name:
        return "rotom-mow"
    if "rotom" in name and "fan" in name:
        return "rotom-fan"
    if "rotom" in name and "frost" in name:
        return "rotom-frost"
    if "rotom" in name and "wash" in name:
        return "rotom-wash"
    if "rotom" in name and "heat" in name:
        return "rotom-heat"
    
    if "calyrex" in name and "ice" in name:
        return "calyrex-ice"
    if "calyrex" in name and "shadow" in name:
        return "calyrex-shadow"
    
    if "ursaluna" in name and "bloodmoon" in name:
        return "ursaluna-bloodmoon"
    
    name = re.sub(r"\[.*?\]", "", name)
    name = re.sub("\s\s+" , " ", name)
    name = name.replace(" ", "-")
    return name

def parse_moves(moves:list[str]) -> list[str]:
    return [
        name.lower().replace(" ", "-")
        for name in moves
    ]


@dataclass
class Player:
    first_name:str
    last_name:str
    country:str

    def __str__(self):
        fn = self.first_name.replace("<", "").replace(">", "").replace('"',"")
        ln = self.last_name.replace("<", "").replace(">", "").replace('"',"")
        return f"{fn}-{ln}-{self.country}"

@dataclass
class TeamMember:
    pokemon: str
    moves: list[str]
    ability: str
    item: str
    tera_type: str

@dataclass
class Team:
    id: str
    player:Player
    teamMember: list[TeamMember]
    losses: int
    ties: int
    wins: int
    placing: int


@dataclass
class Round:
    player1: Player
    player2: Player
    result: str

@dataclass
class Competition:
    title:str
    teams: list[Team]
    rounds: list[Round]




