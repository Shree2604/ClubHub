import app.core as core # fixed import to avoid identifier confusion

def main():
    #user = core.user.register_user("aarush@gmail.com", "abc123", "abc123", "aarush", "pathak")
    
    # inp_email = str(input("Enter email : "))
    # inp_pass = str(input("Enter password : "))

    # if(core.user.authenticate_user(inp_email, inp_pass)):
    #     print("Logged in!")

    club = core.club.create_club(
        "Epoch", 
        "This is an AI&ML club created for the betterment of the society",
        "epoch123")

if __name__ == "__main__":
    main()