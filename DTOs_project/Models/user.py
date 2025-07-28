from DTOs import *

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def to_dto(self):
        from dtos.user_dto import UserDTO
        return UserDTO(id=self.id, name=self.name, email=self.email)