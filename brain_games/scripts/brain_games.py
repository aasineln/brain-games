from brain_games.cli import welcome_user


def greeting() -> None:
    print("Welcome to the Brain Games!")


def main() -> None:
    greeting()
    welcome_user()


if __name__ == "__main__":
    main()