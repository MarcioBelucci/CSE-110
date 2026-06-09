with open("books.txt") as books_file:
    for line in books_file:
        parts = line.split()
        print(parts)