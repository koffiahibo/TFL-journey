from ValidData import *

def loop():
    cli = input("Journey CLI -> ")
    value = cli.split(" ")
    command, arg = value[0], value[1:]
    while command != "end":
            if command == "documentation":
                command2 = input("")
            loop()





if __name__ == '__main__':
    loop()
