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
    def __init__(self,title,author,page_number):    
        super().__init__(title,author)      
        self.page_number=int(page_number)
    def __str__(self):
        message = f"{self.title.title()} by {self.author.title()} Page Count{self.page_number}"    
        return message
    
                                                                            
class Library:
    def __init__(self):
        book=list
        self.book=[Book]           
    def add_book(self,book):
        self.book.append(book)   
    def list_books(self):
        return self.book




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