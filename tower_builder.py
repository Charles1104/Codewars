def tower_builder(n_floors):
  arr = []
  max_length = n_floors * 2 - 1
  for i in range(1, n_floors + 1):
    arr.append(" " * int((max_length - (i * 2 - 1)) / 2) + "*" * (i * 2 - 1) + " " * int((max_length - (i * 2 - 1)) / 2))
  print(arr)

if __name__ == "__main__":
   tower_builder(3)

# BEST PRACTICE
# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]