from app.db.models import ObjectId, User, Club, Membership
from app.db.client import db
from pymongo.cursor import Cursor

def find_user(
    _id: ObjectId = None, 
    email : str = None,
) -> User | None:
    if _id is not None:
        query_filter = {"_id" : _id}
    elif email is not None:
        query_filter = {"email" : email}
    else:
        raise ValueError("Atleast one query must be specified for search")
    
    user_doc = db.users.find_one(filter=query_filter)
    
    if user_doc is None:
        return None
    else:
        return User.conv_to_obj(user_doc)

def find_club(
    _id: ObjectId = None, 
    club_code : str = None,
) -> Club | None:
    if _id is not None:
        query_filter = {"_id" : _id}
    elif email is not None:
        query_filter = {"club_code" : club_code}
    else:
        raise ValueError("Atleast one query must be specified for search")
    
    club_doc = db.clubs.find_one(filter=query_filter)
    
    if club_doc is None:
        return None
    else:
        return Club.conv_to_obj(club_doc)

def find_memberships(
    _id : ObjectId = None,
    user_id: ObjectId = None, 
    club_id: ObjectId = None, 
    role_id: ObjectId = None,
) -> list | None:
    if _id is not None:
        query_filter = {"_id" : _id}
    elif user_id is not None:
        query_filter = {"user_id" : user_id}
    elif club_id is not None:
        query_filter = {"club_id" : club_id}
    elif role_id is not None:
        query_filter = {"role_id" : role_id}
    else:
        raise ValueError("Atleast one query must be specified for search")
    
    memberships = list()

    with db.memberships.find(filter=query_filter) as cursor:
        for doc in cursor:
            memberships.append(Membership.conv_to_obj(doc))

    return memberships