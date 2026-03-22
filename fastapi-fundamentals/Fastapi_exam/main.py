from fastapi import FastAPI
import json

app = FastAPI()

def load_books():
    with open("books.json", "r") as file:
        book_list = json.load(file)
        print(book_list)
        return book_list

# 1. A GET endpoint at /books that returns all books in the list as a JSON response.
@app.get("/")
def books():
    return load_books()
