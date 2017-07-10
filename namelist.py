def namelist(names):

  array_of_names = []

  for i, k in enumerate(names):
    array_of_names.append((names[i]["name"]))

  if len(array_of_names) == 0:
    return ''
  elif len(array_of_names) == 1:
    return(array_of_names[0])
  elif len(array_of_names) == 2:
    return(" & ".join(array_of_names))
  else:
    last_index = len(array_of_names) - 1
    return(", ".join(array_of_names[:-1]) + " & " + array_of_names[last_index])

if __name__ == "__main__":
   namelist([])