def solution(number):
  sum = 0
  for i in range(3, number):
    if i % 3 == 0 or i % 5 == 0:
      sum += i

  print(sum)

if __name__ == "__main__":
   solution(10)