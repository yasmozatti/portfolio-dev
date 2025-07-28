from DTOs.book_dto import BookDTO
import DTOs

class Book:
    def __init__(self, id, name, author, year):
        self.id = id
        self.name = name
        self.author = author
        self.year = year

    def to_dto(self):
        return BookDTO(
            id=self.id,
            name=self.name,
            author=self.author,
            year=self.year
        )

    