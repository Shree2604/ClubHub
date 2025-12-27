import app.core.auth as auth

def main():
    #user = auth.register_user("aarush@gmail.com", "abc123", "abc123", "aarush", "pathak")
    
    inp_email = str(input("Enter email : "))
    inp_pass = str(input("Enter password : "))

    if(auth.authenticate_user(inp_email, inp_pass)):
        print("Logged in!")

if __name__ == "__main__":
    main()