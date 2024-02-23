def summation_while(n: int) -> int:
    x = 0
    while n > 0:
        x += n
        n -= 1
    return x

def summation_for(n: int) -> int:
    x = 0
    for i in range(n+1):
        x += i
    return x


def main():
    print(summation_while(5))
    print(summation_for(5))

if __name__ == "__main__":
    main()
