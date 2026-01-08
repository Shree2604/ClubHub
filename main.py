from app.core.club import create_club
from app.core.user import create_user, authenticate_user
from app.tui.run import Welcome, login

def main():
    Welcome()


if __name__ == "__main__":
    main()