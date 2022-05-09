from re import search


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and bool(search(r'\d', password)) and bool(search(r'\D', password))


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
