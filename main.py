def main():
  book_path = "books/frankenstein.txt"
  print_report(book_path)


def read_book(book):
  with open(book) as f:
    file_contents = f.read()
  return file_contents

def word_count(book):
  return len(read_book(book).split())

def char_count(book):
  b = read_book(book).lower()
  letters = {}
  for char in b:
    if char in letters:
      letters[char] += 1
    else:
        letters[char] = 1
  return letters

def sort_on(dict): 
  return dict["num"]

def convert_to_list(dict):
  dict_list = []
  for key, value in dict.items():
    if key.isalpha():
      dict_list.append({"letter": key, "num": value})
  return dict_list


def print_report(book):
  print("--- Begin report of books ---")
  print(f"{word_count(book)} words found in the document\n")
  chars_dict = char_count(book)
  l = convert_to_list(chars_dict)
  l.sort(reverse=True, key=sort_on)
  for char in l:
    print(f"The '{char['letter']}' character was found {char['num']} times")
  print("--- End report ---")


main()

# TODO
# create a function that creates a list of dictionary items to be able to use isalpha() then sorts it