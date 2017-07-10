def dirReduc(arr):
  a = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
  i = 0
  while i < len(arr) - 1:
    second = arr[i + 1]

    if a[arr[i]] == second:
      del(arr[i])
      del(arr[i])
      i = 0

    else:
      i += 1

  return arr

if __name__ == "__main__":
   dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])