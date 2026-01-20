from ValidData import *
from commands import *
cmd = {"plan-journey": plan_journey}

"""
cmd = {"help": all_commands,
       "plan-journey", 
       "check disruptions", 
       "exit"}
"""

def loop():
    while True:
        command = input("Tfl Journey >>")
        if command in cmd:
            cmd[command]()

        elif command == "exit":
            break
        else :
            print("Unknown command")


if __name__ == "__main__":
    loop()

