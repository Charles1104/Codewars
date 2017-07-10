import functools


def find_short(s):
  arr = s.split(" ")
  arr_len = list(map(lambda x: len(x), arr))

  return functools.reduce(lambda a, b: a if a < b else b, arr_len)

# Best practice
# def find_short(s):
#     return min(len(x) for x in s.split())

if __name__ == "__main__":
   find_short("bitcoin take over the world maybe who knows perhaps")

