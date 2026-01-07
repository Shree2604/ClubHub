from app.db.club import Club, insert_club, ObjectId
from app.db.role import insert_role
from app.db.membership import insert_membership
from app.config import ADMIN_BOOTSTRAP_KEYS

def create_club(
    name: str,
    description: str,
    club_code: str,
    secret_key: str,
    creator_user_id: ObjectId
) -> Club:

    expected_secret_key = ADMIN_BOOTSTRAP_KEYS.get(club_code)
    if expected_secret_key is None:
        raise ValueError("Invalid club code")
    if secret_key != expected_secret_key:
        raise ValueError("Secret key doesn't match")
    
    if not name or not description or not secret_key or creator_user_id is None:
        raise ValueError("All fields are compulsory")
    
    try:
        club = insert_club(name=name, description=description, club_code=club_code)
        lead_role =insert_role(name="Lead", club_id=club._id)
        lead_membership = insert_membership(
            user_id=creator_user_id, 
            club_id=club._id, 
            role_id=lead_role._id)
    except Exception as e:
        # Delete Club and Lead Role from MongoDB
        # if all 3 are not created succesfully
        # This avoids residual data
        print(e)

    return club