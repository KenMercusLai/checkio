from re import search


def is_acceptable_password(password: str) -> bool:
    if len(password) < 6:
        return False
    elif len(password) > 9:
        return True
    elif len(password) > 6:
        return bool(search(r'\d', password)) and bool(search(r'\D', password))
    return False


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
