from app.core.club import register_club
from app.core.user import register_user, authenticate_user

def main():
    user = register_user("aarush@gmail.com", "abc123", "abc123", "aarush", "pathak")
    
    inp_email = str(input("Enter email : "))
    inp_pass = str(input("Enter password : "))

    if(authenticate_user(inp_email, inp_pass)):
        print("Logged in!")

    """club = register_club(
        "Epoch", 
        "This is an AI&ML club created for the betterment of the society",
        "epoch123")"""

if __name__ == "__main__":
    main()