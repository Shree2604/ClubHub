from app.tui import text
import os
from rich import print
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from app.core.user import create_user, authenticate_user
from app.core.club import create_club


console = Console()

def clrTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Welcome():
    clrTerminal()
    console.print(Markdown(text.Welcometxt))
    input("Press Enter to continue to login page: ")
    clrTerminal()
    login()

def login():
    console.print(Markdown(text.Logintxt))
    inp = int(input ("Enter the option number: "))
    clrTerminal()
    match inp:
        case 1:
            email = str(input("Enter your E-mail: "))
            password1 = str(input("Enter your password: "))
            password2 = str(input("Confirm password: "))
            first_name = str(input("Enter your first name: "))
            last_name = str(input("Enter your last name: "))

            user = create_user(
                email=email, 
                password1=password1,
                password2=password2,
                first_name=first_name,
                last_name=last_name
            )

            print("[bold green]Account Successfully Created[/bold green]")

        case 2: 
            print("Feature will be added later")
            
        case 3:
            Welcome()

        case _:
            print("[bold red]Please fill an invalid input[/bold red]")
            input("Press Enter to go to login page: ")
            login()
        




    