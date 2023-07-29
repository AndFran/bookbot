def count_words(text: str):
    words = text.split()
    return len(words)


def letter_count(text: str):
    frequency_dict = {}
    for character in text:
        character = character.lower()
        if not character.isalpha():
            continue

        frequency_dict[character] = frequency_dict.get(character, 0) + 1
    return frequency_dict


def show_report(path: str, total_words: int, frequency_dict: dict):
    print(f"--- Begin report of {path} - --")
    print(f"{total_words} words found in the document")
    print("\n")
    results_list = [(key, value) for key, value in frequency_dict.items()]
    results_list.sort(key=lambda v: v[1], reverse=True)

    for key, value in results_list:
        print(f"The {key} character was found {value} times")


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    frequency_dict = letter_count(file_contents)
    show_report("books/frankenstein.txt", word_count, frequency_dict)

