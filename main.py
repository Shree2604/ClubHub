from app.core.club import create_club
from app.core.user import create_user, authenticate_user

def main():
    user = create_user(
        email="aarush@gmail.com", 
        password1="abc123",
        password2="abc123",
        first_name="aarush",
        last_name="pathak"
    )
    
    inp_email = str(input("Enter email : "))
    inp_pass = str(input("Enter password : "))

    if(authenticate_user(inp_email, inp_pass)):
        print("Logged in!")

    club = create_club(
        name="Epoch",
        description="This is an AI&ML club created for the betterment of the society",
        club_code="EPOCH",
        secret_key="epoch123",
        creator_user_id=user._id
    )

    print("Club Created!")

if __name__ == "__main__":
    main()