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

def find_role(
    _id : ObjectId = None
) -> Role | None:
    # Add name based searching later
    if _id is not None:
        query_filter = {"_id" : _id}
    else:
        raise ValueError("Atleast one query must be specified for search")
    
    role_doc = db.roles.find_one(filter=query_filter)
    
    if role_doc is None:
        return None
    else:
        return Role.conv_to_obj(role_doc)