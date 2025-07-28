from Models.book import Book
from Models.user import User
import Models
import DTOs

book = Book(1, "1984", "George Orwell", 1949)
user = User(1, "Yasmim", "yasmimk@ex.com", "Rua x")

book_dto = book.to_dto()
user_dto = user.to_dto()

print("Book em DTO:")
print(book_dto.json())

print("User em DTO:")
print(user_dto.json())
