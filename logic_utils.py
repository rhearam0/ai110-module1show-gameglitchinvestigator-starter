def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # normalize secret to an int if it's a string or float
    if isinstance(secret, str):
        try:
            secret = int(float(secret)) if "." in secret else int(secret)
        except Exception:
            raise ValueError("Secret value is not numeric.")
    if isinstance(secret, float):
        secret = int(secret)

    # normalize guess to an int if it's a string or float
    if isinstance(guess, str):
        try:
            guess = int(float(guess)) if "." in guess else int(guess)
        except Exception:
            raise ValueError("Guess value is not numeric.")
    if isinstance(guess, float):
        guess = int(guess)

    if guess == secret:
        return "Win", "🎉 Correct!"

    # If the guess is greater than the secret, prompt the user to guess lower.
    if guess > secret:
        return "Too High", "guess lower"

    # Otherwise the guess is lower than the secret; prompt to guess higher.
    return "Too Low", "guess higher"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
