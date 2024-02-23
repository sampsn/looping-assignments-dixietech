def char_count_while(target: str, c) -> int:
    occurences = 0
    i = 0
    while i < len(target):
        if c == target[i]:
            occurences += 1
        i += 1

    return occurences

def char_count_for(target: str, c) -> int:
    occurences = 0
    for i in range(len(target)):
        if c == target[i]:
            occurences += 1
    return occurences

def char_count_foreach(target: str, c) -> int:
    occurences = 0
    for letter in target:
        if c == letter:
            occurences += 1
    return occurences

def main():
    target = "Gabriel Sampson"
    c = "G"

    print(char_count_while(target, c))
    print(char_count_for(target, c))
    print(char_count_foreach(target, c))
    
    print()

    c = "a"

    print(char_count_while(target, c))
    print(char_count_for(target, c))
    print(char_count_foreach(target, c))

if __name__ == "__main__":
    main()
