def iq_test(numbers):
    j = list(map(int, numbers.split(' ')))
    for k, l in enumerate(j):
        if l % 2 == 0:
            j[k] = 'even'
        else:
            j[k] = 'uneven'

    even_count = j.count('even')
    uneven_count = j.count('uneven')

    if(even_count > uneven_count):
      intrus = j.index('uneven') + 1
    else:
      intrus = j.index('even') + 1

    return intrus

if __name__ == "__main__":
   iq_test('2 4 6 7')