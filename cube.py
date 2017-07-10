def cube_odd(arr):
  sum = 0
  for i, k in enumerate(arr):
    if isinstance(k, (int, float, complex)):
      if k%2 != 0:
        sum += pow(k, 3)
    else:
      return None

  return sum

if __name__ == "__main__":
   cube_odd([1,2,3,4])