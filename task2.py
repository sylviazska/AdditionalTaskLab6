from task1 import organisms

REQUIRED = [
    "name", "group", "lives", "communication", "cooperation",
    "movement", "navigation_cue", "food_strategy", "defense", "source"
] # all fields are required

def check_organism(o):
    for key in REQUIRED:
        if key not in o or o[key] is None or str(o[key]).strip() == "":
            raise ValueError(f"{key} is missing")

report = {}
for o in organisms:
    try:
        check_organism(o)
    except ValueError as e:
        message = str(e)
        report[message] = report.get(message, 0) + 1

print("Report:", report)