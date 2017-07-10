def filter_list(l):
  new_list = []
  for i in l:
    if isinstance(i, int):
      new_list.append(i)

  return new_list

if __name__ == "__main__":
   filter_list([1, "a", 3, "ret"])

# Alternative A
# def filter_list(l):
#   'return a new list with the strings filtered out'
#   return [i for i in l if not isinstance(i, str)]

# Alternative B
# def filter_list(l):
#   return filter(lambda x: not isinstance(x, basestring), l)
