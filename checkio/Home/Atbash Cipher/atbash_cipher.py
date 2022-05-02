PLAINTEXT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
CIPHERTEXT = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'


def translate(char: str) -> str:
    match char in PLAINTEXT:
        case True:
            return CIPHERTEXT[PLAINTEXT.index(char)]
        case False:
            return char


def atbash(plaintext: str) -> str:
    return ''.join(map(translate, plaintext))


if __name__ == "__main__":
    print("Example:\nplaintext: testing")
    print(atbash("testing"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert atbash("testing") == "gvhgrmt"
    assert atbash("attack at dawn") == "zggzxp zg wzdm"
    assert atbash("Hello, world!") == "Svool, dliow!"

    print("Coding complete? Click 'Check' to earn cool rewards!")
