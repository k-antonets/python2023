import string

def inputVector() -> list[int]:
    vctr = []
    inpt = input('Vector: ')
    while inpt != '':
        num = int(inpt)
        vctr.append(num)
        inpt = input('Next element: ')
    return vctr


def multiplyVector(scalar: int, vector: list[int]) -> list[int]:
    result = [0] * len(vector)
    for index, value in enumerate(vector):
        result[index] = value * scalar
    return result

def main():
    m = int(input("Multiplier: "))
    vctr = inputVector()
    res = multiplyVector(m, vctr)
    print(res)


if __name__ == '__main__':
    main()

