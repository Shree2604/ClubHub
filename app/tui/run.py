from app.tui import text
from app.core.user import User, create_user, authenticate_user
from app.core.club import Club, create_club

# separate app imports from third party imports
from rich.console import Console
from rich.table import Table

import os
import time

console = Console()

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pause():
    time.sleep(2.5)

def welcome():
    clear_terminal()
    console.print(text.welcome)
    input("\nPress any key to continue to login page")
    login()

def login():
    clear_terminal()
    console.print(text.login)
    inp = int(input("Enter the option number: "))
    clear_terminal()

    match inp:
        case 1:
            email = str(input("Enter your E-mail: "))
            password1 = str(input("Create a new password: "))
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

            if user is not None:
                console.print("\n[bold green]Account Successfully Created[/bold green]")
                console.print("[green]Redirecting to homepage...[/green]")
                pause()
                homepage(user)
            else:
                console.print("\n[bold red]Something went wrong, please try again![/bold red]")
                console.print("[yellow]Redirecting back to login...[/yellow]")
                pause()
                login()

        case 2: 
            email = str(input("Enter your E-mail: "))
            password = str(input("Enter your password: "))

            user = authenticate_user(email=email, password=password)

            if user is not None:
                console.print("\n[bold green]Logged in Successfully[/bold green]")
                console.print("[green]Redirecting to homepage...[/green]")
                pause()
                homepage(user)
            else:
                console.print("\n[bold red]Something went wrong, please try again![/bold red]")
                console.print("[yellow]Redirecting back to login...[/yellow]")
                pause()
                login()
            
        case 3:
            welcome()

        case _:
            console.print("\n[bold red]Please enter a valid input[/bold red]")
            console.print("[yellow]Redirecting back to login...[/yellow]")
            pause()
            login()

def homepage(user:User):
    clear_terminal()
    console.print(text.homepage)
    inp = int(input("Enter the option number: "))
    clear_terminal()

    match inp:
        case 1:
            name = str(input("Enter the name of the club: "))
            description = str(input("Enter the description for the club: "))
            club_code = str(input("Enter the club code: "))
            secret_key = str(input("Enter the secret key: "))

            club = create_club(
                name=name,
                description=description,
                club_code=club_code,
                secret_key=secret_key,
                creator_user_id=user._id
            )

            if club is not None:
                console.print("\n[bold green]Club Created Successfully!![/bold green]")
                console.print("[green]Redirecting to Clubpage...[/green]")
                pause()
                clubpage()
            
            else:
                console.print("\n[bold red]Something went wrong, please try again![/bold red]")
                console.print("[yellow]Redirecting back to Homepage...[/yellow]")
                pause()
                homepage(user)

        case 2:
            console.print("\n[yellow]Feature will be added later[/yellow]")
            console.print("[yellow]Redirecting back to homepage...[/yellow]")
            pause()
            homepage(user)

        case 3:
            console.print("\n[yellow]Feature will be added later[/yellow]")
            console.print("[yellow]Redirecting back to homepage...[/yellow]")
            pause()
            homepage(user)

        case _:
            console.print("\n[bold red]Please fill a valid input[/bold red]")
            console.print("[yellow]Redirecting back to homepage...[/yellow]")
            pause()
            homepage(user)

def clubpage():
    clear_terminal()
    console.print(text.clubpage)
    inp = int(input("Enter the option number: "))
    clear_terminal()