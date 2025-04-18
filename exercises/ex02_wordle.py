"""Program designed to be similar to Wordle."""

__author__: str = "730811928"


def contains_char(search_string: str, char_string: str) -> bool:
    """Checks if the character is found in the string."""
    assert len(char_string) == 1, f"len('{char_string}') is not 1"
    i = 0
    while i < len(search_string):
        if search_string[i] == char_string:
            return True
        i += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Given a guess and a secret word of equal length, returns a string of emojis whose color indicates correctness."""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_color = ""
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_color += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_color += YELLOW_BOX
        else:
            emoji_color += WHITE_BOX

        i += 1
    return emoji_color


def input_guess(expected_len: int) -> str:
    """Prompts the user for a guess until the guess until they provide a guess of the expected length."""
    guess = input(f"Enter a {expected_len} character word: ")
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    total_turns = 6
    won = False
    while turn <= total_turns and won != True:
        print(f"=== Turn {turn}/{total_turns} ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            won = True
        else:
            turn += 1
    if won:
        print(f"You won in {turn}/{total_turns} turns!")
    else:
        print(f"X/{total_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
