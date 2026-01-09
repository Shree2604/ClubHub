from app.core.club import create_club
from app.core.user import create_user, authenticate_user
from app.tui.run import welcome

def main():
    welcome()

if __name__ == "__main__":
    main()