def is_isogram(string):
  dict1 = {}
  string = string.lower()
  for i in string:
    if i in dict1:
      dict1 = "no isogram"
      print("False")
    else:
      dict1[i] = 1

  print("True")

if __name__ == "__main__":
   is_isogram("Tt")