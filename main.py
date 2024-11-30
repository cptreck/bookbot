def main():
  book_path = "books/frankenstein.txt"
  print(word_count(book_path))
  

def read_book(book):
  with open(book) as f:
    file_contents = f.read()
  return file_contents

def word_count(book):
  return len(read_book(book).split())

 


main()