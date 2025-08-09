class Book:
    def __init__(self,title,author,year):
        self.author=author
        self.title=title
        self.year=year
    def __str__(self):
         message=f"{self.title} by {self.author}, published in {self.year}"
         return message
         
    def __repr__(self):
         message=f"Book('{self.title}', '{self.author}', {self.year})"          
         return message 
                 
 
    def __del__(self):
        print(f"Deleting {self.title} {self.year}{self.author}")
        


from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()