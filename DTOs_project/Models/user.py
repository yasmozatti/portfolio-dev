from DTOs.user_dto import *

class User:
    def __init__(self, id, name, email, adress):
        self.id = id
        self.name = name
        self.email = email
        self.adress = adress

    def to_dto(self):
        return UserDTO(
            id=self.id,
            name=self.name,
            email=self.email,
            adress=self.adress
        )
