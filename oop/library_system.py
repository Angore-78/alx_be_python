class Book:
    def __init__(self,title,author):
        self.author=author
        self.title=title
        print(f'{self.title} by {self.author}')             
 
        
class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size=float(file_size)
    def __str__(self):
        message = f'{self.title.title()} by {self.author.title()} File Size{self.file_size}'
        return message
        
                              
                                                    
class PrintBook(Book):
    def __init__(self,title,author,page_count):    
        super().__init__(title,author)      
        self.page_count=int(page_count)
    def __str__(self):
        message = f"{self.title.title()} by {self.author.title()} Page Count{self.page_count}"    
        return message
    
                                                                            
class Library:
    def __init__(self):

        self.books=[]           
    def add_book(self,books):
        self.books.append(books)   
    def list_books(self):
        return self.books




def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()