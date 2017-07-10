def likes(names):
  length = len(names)
  length2 = len(names) - 2
  if length == 0:
    print("no one likes this")
  elif length == 1:
    print(names[0] + " likes this")
  elif length == 2:
    print(" and ".join(names) + " likes this")
  elif length == 3:
    print(", ".join(names[:2]) + " and " + names[2] + " like this")
  else:
    print(", ".join(names[:2]) + " and " + str(length2) + " others like this")

if __name__ == "__main__":
   likes(['Max', 'John', 'Mark', 'Maxou'])

# BEST PRACTICE
# def likes(names):
#     formats = {
#             0: "no one likes this",
#             1: "{} likes this",
#             2: "{} and {} like this",
#             3: "{}, {} and {} like this",
#             4: "{}, {} and {others} others like this"
#         }
#     n = len(names)
#     return formats[min(n,4)].format(*names, others=n-2)