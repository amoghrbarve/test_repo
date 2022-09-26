def input_word():
    word = input("Enter the scanned word ")
    return word


def is_tachycardic(word):
    if word == "tachycardic":
        return True
    else:
        return False


if __name__ == "__main__":
    word = input_word()
    value = is_tachycardic(word)
