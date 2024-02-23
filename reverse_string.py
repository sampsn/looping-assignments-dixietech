def reverse_while(s):
    i = len(s) - 1
    new_string = ""
    while i >= 0:
        new_string += s[i]
        i -= 1
    return new_string
    
def reverse_for(s):
    new_string = ""
    for i in range(len(s)):
        new_string += s[-i-1]
    return new_string

def reverse_foreach(s):
    new_string = ""
    for letter in s:
        new_string = letter + new_string
    return new_string


def main():
    s = "Gabriel Sampson"

    print(reverse_while(s))
    print(reverse_for(s))
    print(reverse_foreach(s))

if __name__ == "__main__":
    main()
