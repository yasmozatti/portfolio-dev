class Book:
    id : int
    name : str 
    author : str 
    year : int

    def __init__(self, id, name, author, year):
        self.id = id
        self.name = name
        self.author = author
        self.year = year

    def to_dto(self):
        pass