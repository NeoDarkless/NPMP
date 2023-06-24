import datetime
import random

# Setup
cmd_dict = {
    "help": "List of commands",
    "about": "About NPMP",
    "datetime": "Prints the date and time on your computer",
    "randint": "Prints a random integer between two provided integers (inclusive)",
    "exit": "Exits the program"
}

print("""                                                                                                                                                                       
NNNNNNNN        NNNNNNNN PPPPPPPPPPPPPPPPP    MMMMMMMM               MMMMMMMM PPPPPPPPPPPPPPPPP   
N:::::::N       N::::::N P::::::::::::::::P   M:::::::M             M:::::::M P::::::::::::::::P  
N::::::::N      N::::::N P::::::PPPPPP:::::P  M::::::::M           M::::::::M P::::::PPPPPP:::::P 
N:::::::::N     N::::::N PP:::::P     P:::::P M:::::::::M         M:::::::::M PP:::::P     P:::::P
N::::::::::N    N::::::N   P::::P     P:::::P M::::::::::M       M::::::::::M   P::::P     P:::::P
N:::::::::::N   N::::::N   P::::P     P:::::P M:::::::::::M     M:::::::::::M   P::::P     P:::::P
N:::::::N::::N  N::::::N   P::::PPPPPP:::::P  M:::::::M::::M   M::::M:::::::M   P::::PPPPPP:::::P 
N::::::N N::::N N::::::N   P:::::::::::::PP   M::::::M M::::M M::::M M::::::M   P:::::::::::::PP  
N::::::N  N::::N:::::::N   P::::PPPPPPPPP     M::::::M  M::::M::::M  M::::::M   P::::PPPPPPPPP    
N::::::N   N:::::::::::N   P::::P             M::::::M   M:::::::M   M::::::M   P::::P            
N::::::N    N::::::::::N   P::::P             M::::::M    M:::::M    M::::::M   P::::P            
N::::::N     N:::::::::N   P::::P             M::::::M     MMMMM     M::::::M   P::::P            
N::::::N      N::::::::N PP::::::PP           M::::::M               M::::::M PP::::::PP          
N::::::N       N:::::::N P::::::::P           M::::::M               M::::::M P::::::::P          
N::::::N        N::::::N P::::::::P           M::::::M               M::::::M P::::::::P          
NNNNNNNN         NNNNNNN PPPPPPPPPP           MMMMMMMM               MMMMMMMM PPPPPPPPPP          
                                                                                                                                                                              
Welcome to NPMP. Enter *help* for a list of commands.""")

while True:
    cmd = input("> ")
    if cmd == "help":
        print("Here is a list of commands:", cmd_dict)
    elif cmd == "about":
        print("NPMP (Neo's Python Multipurpose) is a program by NeoDarkless made to improve programming skills.")
    elif cmd == "datetime":
        x = datetime.datetime.now()
        print(x.strftime("%A %d %B %Y\n%X"))
    elif cmd == "randint":
        start = int(input("Starting integer? > "))
        finish = int(input("Finishing integer? > "))
        ans = random.randint(start, finish)
        print(ans)
    elif cmd == "exit":
        break
    else:
        print(f"{cmd} is an invalid command. Use *help* for a list of commands.")