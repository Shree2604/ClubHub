import app.core.user as user
import app.core.club as club

def main():
    # user = user.register_user("aarush@gmail.com", "abc123", "abc123", "aarush", "pathak")
    
    club = club.create_club("Epoch", "This is an AI&ML club created for the betterment of the society",["lead",] ,"epoch123")

    # inp_email = str(input("Enter email : "))
    # inp_pass = str(input("Enter password : "))

    # if(user.authenticate_user(inp_email, inp_pass)):
    #     print("Logged in!")

if __name__ == "__main__":
    main()