from app.db.models import Club, ObjectId, datetime
from app.db.client import db

def insert_club(
    name: str,
    description: str,
    club_code: str
) -> Club:

    club = Club(
        _id=None,
        name=name,
        description=description,
        club_code=club_code,
        created_at=datetime.now()
    )

    new_club_id = db.clubs.insert_one(club.conv_to_doc()).inserted_id
    club._id = new_club_id

    return club

def find_club(
    _id : ObjectId = None, 
    club_code : str = None,
) -> Club | None:
    # Add name based searching later
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

def get_club_member_count(
    club : Club
) -> int:

    if club is not None:
        query_filter = {"club_id" : club._id}
    else:
        raise ValueError("Atleast one query must be specified for search")
    
    count = db.memberships.count_documents(filter=query_filter)  
    return count