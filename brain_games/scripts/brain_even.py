import random

import prompt


def greeting() -> None:
    print("Welcome to the Brain Games!")


def start_even_numbers() -> None:
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    all_answers_coorect = True
    for _ in range(3):
        random_number = random.randint(0, 100)
        print(f"Question: {random_number}")

        answer = prompt.string("Your answer: ")
        if is_even(random_number) and answer.lower() == "yes":
            result = "Correct!"
        elif not is_even(random_number) and answer.lower() == "no":
            result = "Correct!"
        else:
            result = "Incorrect!"
            all_answers_coorect = False
        print(result)

    if all_answers_coorect:
        print(f"Congratulations, {name}!")
    else:
        print(f"Try again, {name}")


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


def main() -> None:
    greeting()
    start_even_numbers()


if __name__ == "__main__":
    main()