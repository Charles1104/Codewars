def divisors(integer):
  arr = []
  for i in range(2, integer):
    if integer % i == 0:
      arr.append(i)

  if len(arr) == 0:
    return str(integer) + " is prime"

  return arr

if __name__ == "__main__":
   divisors(13)

# BEST PRACTICE
# def divisors(num):
#     l = [a for a in range(2,num) if num%a == 0]
#     if len(l) == 0:
#         return str(num) + " is prime"
#     return l