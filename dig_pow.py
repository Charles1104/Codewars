def dig_pow(n, p):
  strNum = str(n)
  arr = []
  for k, i in enumerate(strNum):
    arr.append(pow(int(i), p + k))

  if (sum(arr) % n == 0):
    print(int(sum(arr) / n))
  else:
    print("-1")

if __name__ == "__main__":
   dig_pow(89, 1)

# BEST PRACTICE
# def dig_pow(n, p):
#   s = 0
#   for i,c in enumerate(str(n)):
#      s += pow(int(c),p+i)
#   return s/n if s%n==0 else -1