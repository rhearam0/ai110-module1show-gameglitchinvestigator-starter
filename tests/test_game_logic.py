from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "guess lower")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "guess higher")

def test_guess_with_string_secret_is_numeric():
    # Secret values stored as strings should still compare numerically
    result = check_guess(60, "50")
    assert result == ("Too High", "guess lower")


def test_update_score_too_high_always_penalizes():
    assert update_score(0, "Too High", 1) == -5
    assert update_score(-5, "Too High", 2) == -10


def test_update_score_too_low_always_penalizes():
    assert update_score(0, "Too Low", 1) == -5
    assert update_score(-5, "Too Low", 2) == -10
