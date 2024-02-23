def list_multiply_while(a: list[int],  b: list[int]) -> list[int]:
    i = 0
    c = []
    while i < len(a):
        c.append(a[i]*b[i])
        i += 1
    return c


def list_multiply_for(a: list[int],  b: list[int]) -> list[int]:
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c

def list_multiply_foreach(a: list[int],  b: list[int]) -> list[int]:
    c = []
    for num in a:
        c.append(num*b[a.index(num)])
    return c


def main():
    a = [1, 2, 3]
    b = [4, 5, 6]

    print(list_multiply_while(a, b))
    print(list_multiply_for(a, b))
    print(list_multiply_foreach(a, b))


if __name__ == "__main__":
    main()
