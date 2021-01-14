def main(x):
    x = x + 10
    b = valor(x)
    return b + x

def valor(b):
    b = b + 20
    return b

    


if __name__ == '__main__':
    print(main(3))
    