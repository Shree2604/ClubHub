from app.db.models import Role, ObjectId
from app.db.client import db

def insert_role(
    name: str,
    club_id: ObjectId
) -> Role:

    if not all([name, club_id]):
        raise ValueError("All fields are compulsory")

    role = Role(
        _id=None,
        name=name,
        club_id=club_id,
        count=1
    )

    new_role_id = db.roles.insert_one(role.conv_to_doc()).inserted_id
    role._id = new_role_id

    return role