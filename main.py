from app.tui.run import welcome
from app.core.user import get_user_clubs, authenticate_user

def main():
    welcome()

    #user = authenticate_user("aarush@gmail.com", "abc123")
    #print(get_user_clubs(user))

if __name__ == "__main__":
    main()