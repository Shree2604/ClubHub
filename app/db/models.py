from bson.objectid import ObjectId
from datetime import datetime

class User:
    def __init__(
        self,
        _id: ObjectId | None,
        email: str,
        pw_hash: str,
        first_name: str,
        last_name: str,
    ):
        self._id = _id
        self.email = email
        self.pw_hash = pw_hash
        self.first_name = first_name
        self.last_name = last_name
    
    def get_id(self):
        return self._id

    @classmethod
    def conv_to_obj(cls, doc):
        return cls(
            _id=doc["_id"],
            email=doc["email"],
            pw_hash=doc["pw_hash"],
            first_name=doc["first_name"],
            last_name=doc["last_name"],
        )

    def conv_to_doc(self):
        return {
            "_id": ObjectId() if self._id is None else self._id,
            "email": self.email,
            "pw_hash": self.pw_hash,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }


class Club:
    def __init__(self, 
            _id : ObjectId | None, 
            name : str, 
            description : str, 
            club_code : str,
            created_at : datetime, 
        ):
            self._id = _id
            self.name = name
            self.description = description
            self.club_code = club_code
            self.created_at = created_at

    def get_id(self):
        return self._id

    @classmethod
    def conv_to_obj(cls, doc):
        return cls(
            _id=doc["_id"],
            name=doc["name"],
            description=doc["description"],
            club_code=doc["club_code"],
            created_at=doc["created_at"],
        )

    def conv_to_doc(self):
        return {
            "_id" : (ObjectId() if self._id is None else self._id),
            "name" : self.name,
            "description" : self.description,
            "club_code" : self.club_code,
            "created_at" : self.created_at,
        }

class Role:
    def __init__(self, 
            _id : ObjectId | None, 
            name : str, 
            club_id : ObjectId, 
            count : int
        ):
            self._id = _id
            self.name = name
            self.club_id = club_id
            self.count = count
    
    def get_id(self):
        return self._id

    @classmethod
    def conv_to_obj(cls, doc):
        return cls(
            _id=doc["_id"],
            name=doc["name"],
            club_id=doc["club_id"],
            count=doc["count"]
        )

    def conv_to_doc(self):
        return {
            "_id" : (ObjectId() if self._id is None else self._id),
            "name" : self.name,
            "club_id" : self.club_id,
            "count" : self.count
        }

class Membership:
    def __init__(self, 
            _id : ObjectId | None, 
            user_id : ObjectId, 
            club_id : ObjectId, 
            role_id : ObjectId, 
            joined_at : datetime, 
            left_at : datetime | None
        ):
            self._id = _id
            self.user_id = user_id
            self.club_id = club_id
            self.role_id = role_id
            self.joined_at = joined_at
            self.left_at = left_at
    
    def get_id(self):
        return self._id

    @classmethod
    def conv_to_obj(cls, doc):
        return cls(
            _id=doc["_id"],
            user_id=doc["user_id"],
            club_id=doc["club_id"],
            role_id=doc["role_id"],
            joined_at=doc["joined_at"],
            left_at=doc["left_at"]
        )

    def conv_to_doc(self):
        return {
            "_id" : (ObjectId() if self._id is None else self._id),
            "user_id" : self.user_id,
            "club_id" : self.club_id,
            "role_id" : self.role_id,
            "joined_at" : self.joined_at,
            "left_at" : self.left_at,
        }