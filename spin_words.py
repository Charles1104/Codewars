def spin_words(sentence):
  arr = sentence.split()
  new_arr = []
  for i in arr:
    if len(i) >= 5:
      new_string = ""
      for j in i[::-1]:
        new_string += j
      new_arr.append(new_string)
    else:
      new_arr.append(i)

  new_arr = " ".join(new_arr)

  print(new_arr)


if __name__ == "__main__":
   spin_words("Hey fellow warriors")