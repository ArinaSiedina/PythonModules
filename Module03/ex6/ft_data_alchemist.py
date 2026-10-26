import random

print("=== Game Data Alchemist ===\n")

players_names: list[str] =['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
print(f"Initial list of players: {players_names}")

players_names_capitalized = [name.capitalize() for name in players_names]
print(f"New list with all names capitalized: {players_names_capitalized}")

players_names_capitalized_only = [name for name in players_names if name.istitle()]
print(f"New list of capitalized names only: {players_names_capitalized_only}\n")

score_table: dict[str,int] = {}
for name in players_names_capitalized:
    score = random.randint(1,1000)
    score_table[name] = score

print(f"Score dict: {score_table}")
avarage_score = round((sum(score_table.values())/len(players_names)),2)
print(f"Score average is {avarage_score}")
print("High scores:", {name: score for name, score in score_table.items() if score > avarage_score})

