import json
import random

with open("book_data.json", "r") as file:
    data = json.load(file)


# display all books
print("All books:")

for book in data['books']:
    print(f"isbn:{book['isbn']}, title:{book['title']}, author:{book['author']}, publication_year:{book['publication_year']}, genre:{book['genre']}, price:{book['price']}")


# display books only with genre Fantasy
print("\n Fantasy books")

fantasy_books=[book for book in data['books'] if book['genre']=="Fantasy"]

for book in fantasy_books:
    print(f"isbn:{book['isbn']}, title:{book['title']}, author:{book['author']}, publication_year:{book['publication_year']}, genre:{book['genre']}, price:{book['price']}")


# add new book
print("Add new book:\n")

title=input("Enter title of book:")
author=input("Enter author of book:")
publication_year=input("Enter publication year of the book:")
genre=input("Enter the genre of book:")
price=input("Enter price of book:")


new_book={
    "isbn":f"978-{random.randint(1000000000, 9999999999)}",
    "title":title,
    "author":author,
    "publication_year":publication_year,
    "genre":genre,
    "price":price
}

data['books'].append(new_book)
print(json.dumps(data, indent=2))

with open("book_data.json",'w') as file:
    json.dump(data,file,indent=2)


# delete a particular recoed from book

isbn_to_delete=input("Enter isbn of book to be deleted:")

updates_books=[book for book in data['books'] if book['isbn']!=isbn_to_delete]

data['books']=updates_books

with open("book_data.json","w") as file:
    json.dump(data,file,indent=2)
print(f"book with isbn:{isbn_to_delete} is deleted")


