def alphabet_position(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  if type(text) == str:
      text = text.lower()
      result = ''
      for letter in text:
        if letter.isalpha():
            result = result + ' ' + str(alphabet.index(letter) + 1)
      print(result.lstrip(' '))

if __name__ == "__main__":
   alphabet_position("The sunset sets at twelve o' clock.")

# Alternate A
# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())