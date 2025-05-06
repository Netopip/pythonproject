def intervalo(num1, num2):
    return list(range(num1,num2))

def main():
    num1 = int(input())
    num2 = int(input())

    msg = intervalo(num1, num2)
    print(msg)

if __name__ == '__main__':
    main()
