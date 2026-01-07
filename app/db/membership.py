from app.db.models import Membership, ObjectId
from app.db.client import db

from datetime import datetime

def insert_membership(
    user_id: ObjectId,
    club_id: ObjectId,
    role_id: ObjectId
) -> Membership:

    membership = Membership(
        _id=None,
        user_id=user_id,
        club_id=club_id,
        role_id=role_id,
        joined_at=datetime.now(),
        left_at=None
    )

    new_membership_id = db.memberships.insert_one(membership.conv_to_doc()).inserted_id
    membership._id = new_membership_id

    return membership