def loop():
    cli = input("Journey CLI -> ")
    value = cli.split(" ")
    command, arg = value[0], value[1:]
    while command != "end":
        return 0





if __name__ == '__main__':
    loop()
