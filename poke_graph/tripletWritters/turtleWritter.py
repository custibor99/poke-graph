from poke_graph.models.base_models import Type, Move, Pokemon

class TurtleWriter:
    def __init__(self, prefix):
        self.prefix = prefix

    def write_triplet(self, subject:str, relation:str, object:str) -> str:
        return f"{subject} {relation} {object} . \n"
    
    def write_type_triplets(self, type:Type) -> str:
        subject = f"<{self.prefix}/{type.name}>"
        res = ""
        res += self.write_triplet(subject, "rdf:type", "owl:NamedIndividual")
        res += self.write_triplet(subject, "rdf:type", f"<{self.prefix}/Type>")

        for name in type.double_damage_to:
            res += self.write_triplet(subject, f"<{self.prefix}/double_damage>", f"<{self.prefix}/{name}>")

        for name in type.half_damage_to:
            res += self.write_triplet(subject, f"<{self.prefix}/half_damage>", f"<{self.prefix}/{name}>")

        for name in type.no_damage_to:
            res += self.write_triplet(subject, f"<{self.prefix}/no_damage>", f"<{self.prefix}/{name}>")
        return res
    
    def write_move_triplets(self, move:Move):
        move_name = move.name.lower().replace(" ","-")
        move_type =move.move_type.lower()
        subject = f"<{self.prefix}/{move_name}>"

        res = ""
        res += self.write_triplet(subject, "rdf:type", "owl:NamedIndividual")
        res += self.write_triplet(subject, f"<{self.prefix}/of_type>", f"<{self.prefix}/{move_type}>")
        
        damage_type = f"<{self.prefix}/StatusMove>"
        if move.damage_class == "physical":
            damage_type = f"<{self.prefix}/PhysicalMove>"
        elif move.damage_class == "special":
            damage_type = f"<{self.prefix}/SpecialMove>"
        res += self.write_triplet(subject, f"rdf:type", damage_type)

        res += self.write_triplet(subject, f"<{self.prefix}/pp>", f"{move.pp}")
        res += self.write_triplet(subject, f"<{self.prefix}/power>", f"{move.power}")
        res += self.write_triplet(subject, f"<{self.prefix}/priority>", f"{move.priority}")
        res += self.write_triplet(subject, f"<{self.prefix}/accuracy>", f"{move.accuracy}")
        res += self.write_triplet(subject, f"<{self.prefix}/flinch_chance>", f"{move.flinch_chance}")
        res += self.write_triplet(subject, f"<{self.prefix}/effect_chance>", f"{move.effect_chance}")
        res += self.write_triplet(subject, f"<{self.prefix}/drain>", f"{move.drain}")
        res += self.write_triplet(subject, f"<{self.prefix}/healing>", f"{move.healing}")

        return res
    
    def writte_pokemon_triplets(self, pokemon:Pokemon) -> str:
        pokemon_name = pokemon.name.lower().replace(" ", "-")
        subject = f"<{self.prefix}/{pokemon_name}>"

        res = ""
        res += self.write_triplet(subject, "rdf:type", "owl:NamedIndividual")
        res += self.write_triplet(subject, "rdf:type", f"<{self.prefix}/Pokemon>")







    


