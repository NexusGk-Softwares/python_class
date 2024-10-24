books = {
    'title': 'the book',
    'author': 'john doe',
    'publication_year': 2020,
    'genre': 'fiction'
     
    }
print(books)

books['title'] = 'the new book'
print(books)

books['new_key'] = 'new value'
print(books)

del books['genre']
print(books)

books.clear()
print(books)

if 'title' in books:
    print('title is present in the dictionary')
else:
    print('title is not present in the dictionary')
    
