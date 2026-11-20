from task1 import organisms


class Organism:
    def __init__(self, row):
        self.name = row["name"]
        self.group = row["group"]
        self.lives = row["lives"]
        self.movement = row["movement"]
        self.cue = row["navigation_cue"]
        self.food = row["food_strategy"]
        self.cooperation = row["cooperation"]
        self.defense = row["defense"]

    def describe(self):
        return f"The {self.name} is a {self.group} that gets around by {self.movement}"


class Loner(Organism):
    def describe(self):
        return f"The {self.name} is a {self.group} that survives on its own and gets around by {self.movement}"


class GroupMember(Organism):
    def describe(self):
        return f"The {self.name} is a {self.group} that lives in groups or pairs and gets around by {self.movement}"


class ColonyMember(Organism):
    def describe(self):
        return f"The {self.name} is a {self.group} that lives in big colonies and gets around by {self.movement}"


def make_any(row):
    if row["lives"] == "solitary":
        return Loner(row)
    if row["lives"] == "colony":
        return ColonyMember(row)
    return GroupMember(row)


zoo = [make_any(row) for row in organisms]

# 1 loop, no if
for o in zoo:
    print(o.describe())