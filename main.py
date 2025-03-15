from crud import add_books,get_book,get_member,add_members,Issue_book,return_book,view_transaction

def addbook():
    title=input("Enter Books title:")
    author=input("enter Book author:")
    isbn=input("Enter ISBN NO:")
    count=input("Enter copies Count:")
    add_books(title,author,isbn,count)


def getbook():
    # Fetch the list of books
    books = get_book()
    
    # If no books are available, print a friendly message
    if not books:
        print("\nNo books available.\n")
        return
    
    # Print a header for the book details
    print("=" * 60)
    print(f"{'ID':<5} {'TITLE':<40} {'AUTHOR':<30} {'COPIES AVAILABLE':<10}")
    print("-" * 60)
    
    # Print each book in a structured format
    for book in books:
        print(f"{book.id:<5} {book.title:<40} {book.author:<30} {book.count:<10}")
    
    print("=" * 60)
def addmember():
    name=input("ENTER Member Name:")
    email=input("Enter Member Email:")
    add_members(name,email)
   
def getmember():
    member=get_member()
    for mem in member:
        print(f"ID:{mem.id} \n Name:{mem.name} \n Email:{mem.email}")

def issuebook():
    book_id=int(input("Enter Book ID:"  ))
    member_id=int(input("Enter Member id"))
    Issue_book(book_id,member_id)

def returnbook():
    transaction_id=int(input("Enter Transaction id:"))
    return_book(transaction_id)

def getTransactionbyMember():
    member_id=int(input("Enter Member ID"))
    transactions=view_transaction(member_id)

    for transaction in transactions:
         return_state="Returns" if transaction.return_date else "Not Returned"
         print(f"Transacion ID:{transaction.id},BOOK ID:{transaction.book_id},Issue Date:{transaction.issue_date},Return Date:{transaction.return_date}")

def main():
    while True:
        print("******************************************************")
        
        print("1.add book")
        print("2.View book")
        print("3.Add members")
        print("4.View Members")
        print("5.Issue Book")
        print("6.return Book")
        print("7.View Transaction By Member")
        print("8.Break")
        print("**************************************************")
        choice=input("Enter Your choice:")



    
        if choice=='1':
            print("Lets add books:")
            addbook()
        elif choice =='2':
            getbook()
        elif choice =='3':
            addmember()
        elif choice =='4':
            getmember()
        elif choice =='5':
            issuebook()
        elif choice=='6':
            returnbook()
        elif choice=="7":
            getTransactionbyMember()
        else:
            break

    
        
if __name__== '__main__':
    main()


