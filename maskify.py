def maskify(cc):

  new_string = ""

  for i,k in enumerate(cc):
    if i < len(cc) - 4:
      new_string += "#"
    else:
      new_string += k

  return new_string

if __name__ == "__main__":
   maskify("toto")