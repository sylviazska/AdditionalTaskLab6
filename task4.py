from task1 import organisms
from statistics import mean, median


def count_by(rows, key):
    counts = {}
    for r in rows:
        value = r[key]
        if value not in counts:
            counts[value] = 0
        counts[value] = counts.get(value, 0) + 1
    return counts


def group_stat(rows, group, value, how="mean"):
    groups = {}

    for r in rows:
        v = r[value]
        if v is None:
            continue

        g = r[group]
        if g not in groups:
            groups[g] = []
        groups[g].append(v)

    def one_number(values):
        if how == "mean":
            return mean(values)
        elif how == "median":
            return median(values)
        elif how == "count":
            return len(values)
        elif how == "max":
            return max(values)
        else:
            raise ValueError(f"Unknown 'how' value: {how}")

    return {g: one_number(v) for g, v in groups.items()}


def organisms_using(cue):
    for organism in organisms:
        if organism["navigation_cue"] == cue:
            yield organism


print("Counts by lives: ", count_by(organisms, "lives"))
print("\nCounts by movements: ", count_by(organisms, "movement"))

cue_counts = group_stat(organisms, "navigation_cue", "name", how="count")
print("\nCounts by navigation cue: ", cue_counts)

print("\nOrganisms that use touch:")
for organism in organisms_using("touch"):
    print("-", organism["name"])
