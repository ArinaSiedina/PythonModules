import random


def gen_player_achievements() -> set[str]:
    achievements = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Dragon Tamer",
        "Puzzle Master",
        "Legendary Hero",
        "Team Player",
        "Secret Keeper",
        "Master Builder",
        "Perfect Victory",
    ]

    count = random.randint(1, len(achievements))
    return set(random.sample(achievements, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for player, achievements in players.items():
        print(f"Player{player}: {achievements}")

    all_achivements = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_achivements}")
    print(f"\nCommon achievements: {set.intersection(*players.values())}\n")
    for player, achievements in players.items():
        others = set().union(
            *(
                other_achievements
                for name, other_achievements in players.items()
                if name != player
            )
        )
        print(f"Only {player} has: {achievements.difference(others)}")

    print()
    for player, achievements in players.items():
        print(f"{player} is missing: {set.difference(all_achivements, achievements)}")
