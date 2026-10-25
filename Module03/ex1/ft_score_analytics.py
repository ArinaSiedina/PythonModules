import sys


def check_arguments(arguments: list[str]) -> list[int] | None:
    valid_args_list: list[int] = []
    all_args_valid = True
    if not arguments:
        return 

    for argument in arguments:
        try:
            number = int(argument)
        except ValueError:
            print(f"Invalid parameter: '{argument}'")
            all_args_valid = False
        else:
            valid_args_list.append(number)

    if all_args_valid:
        return valid_args_list
    else:
        return


def main() -> None:
    print("=== Player Score Analytics ===")

    if not sys.argv[1:]:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    arguments = check_arguments(sys.argv[1:])
    if arguments is None:
        return

    total_players = len(arguments)
    total_score = sum(arguments)
    high_score = max(arguments)
    low_score = min(arguments)

    print(f"Scores processed: {arguments}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score / total_players:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()