def sum_pairs(ints, s):
  first = ""
  second = ""
  index = 10000000
  for k, i in enumerate(ints[:-1:]):
    for l, j in enumerate(ints[k + 1::]):
      if i + j == s and l < index:
        arr = []
        index = l
        first = i
        second = j
        arr.append(first)
        arr.append(second)

  if first + second != s:
    return None

  return arr

if __name__ == "__main__":
   sum_pairs([10, 5, 2, 3, 7, 5], 10)