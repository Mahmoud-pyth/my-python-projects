library = []
wish = []
book_1 = input("Enter the name of the book you own:\n")
library.append(book_1)
book_2 = input("Enter the name of another book you own (or press 'Enter' to skip):\n")
if book_2:
  library.append(book_2)
print(f"Your library: {library}\n")
book_1 = input("Enter the name of the book you wish to have:\n")
wish.append(book_1)
book_2 = input("Enter the name of another book you wish to have (or press 'Enter' to skip :\n")
if book_2:
  wish.append(book_2)
print(f"Your wishlist is: {wish}")
book_3 = input("Enter the name of a book from your wishlist that you've gain (or press 'Enter' to skip):\n ")
if book_3 in wish:
 library.append(book_3)
 wish.remove(book_3)
print(f"update library: {library}")
print(f"update wishlist: {wish}\n")
given = input("Enter the name of a book from your library you wish to given to someone (or press 'Enter' to skip):\n")
if given in library:
  library.remove(given)
print(f"your final library is: {library}")
