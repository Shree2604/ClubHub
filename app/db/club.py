from app.db.models import Club, ObjectId
from app.db.client import db

# separate third-party imports from local app
from datetime import datetime

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