from app.db.club import Club, create_club

from dotenv import load_dotenv
from os import getenv

def register_club(
    name: str,
    description: str,
    secret_key: str
) -> Club:

    load_dotenv()
    secret_club_key = getenv("SECRET_KEY")
    
    if not all([name, description, secret_key]):
        raise ValueError("All fields are compulsory")
    
    if secret_key != secret_club_key:
        raise ValueError("Secret key doesn't Match")
    
    club = create_club(name=name, description=description)

    return club