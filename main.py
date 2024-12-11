from string import ascii_lowercase


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        results = count_characters(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for key in sorted(results, key=results.get, reverse=True):
            print(f"The '{key}' character was found {results[key]} times")
        print("--- End report ---")


def count_characters(text):
    text = text.lower()
    table = {}
    for char in text:
        if char in ascii_lowercase:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1
    return table


if __name__ == "__main__":
    main()
