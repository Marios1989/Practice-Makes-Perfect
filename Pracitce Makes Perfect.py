def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(is_even(5))
print(is_even(6))

# is_int
def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print(is_int(10))
print(is_int(10.5))

# digit_sum
def digit_sum(n):
    total = 0
    string_n = str(n)
    for char in string_n:
        total += int(char)
    return total


# Alternate Solution:

# def digit_sum(n):
#  total = 0
#  while n > 0:
#    total += n % 10
#    n = n // 10
#  return total

print(
digit_sum(1234))

# factorial
def factorial (x):
  if x==1:
   return 1
  else:
    return x*factorial(x-1)
print(factorial(5))

# is_prime
def is_prime(x):
    if x < 2:
       return False

    elif x == 2:
      return True

    for numbers in range(2,x):
     if x % numbers == 0:
       return False
    return True

# reverse
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word


print(reverse("Hello World"))

# anti_vowel
def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
 print(anti_vowel("hello book"))

# scrabble_score
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

print(scrabble_score("pizza"))

# censor
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)

    return result


print(censor("this hack is wack hack", "hack"))

# count
def count(sequence, item):
    acc = 0
    for nm in sequence:
        if nm == item:
            acc += 1
    return acc


print(count([1, 2, 1, 1], 1))
print(count(['1', '2', '1', '1'], '1'))

# purify
def purify(lst):
    newlst=[]
    for nm in lst:
        if nm%2==0:
            newlst.append(nm)
    return newlst
print(purify([1,2,3]))

# product
def product(lst):
    outcome=1
    for nm in lst:
        outcome *= nm
    return outcome
print(product([4, 5, 5]))

# remove_duplicates
def remove_duplicates(lst):
    newlst=[]
    for nm in lst:
        if nm not in newlst:
            newlst.append(nm)
    return newlst
print(remove_duplicates([1,1,2,2]))

# median
print(round(5/2))
def median(lst):
    lstsorted=sorted(lst)
    if (len(lstsorted)%2 != 0):
        return lstsorted[ (len(lstsorted)+1) /2 - 1]
    else:
        return (lstsorted[len(lstsorted)/2] \
        + lstsorted[len(lstsorted)/2 - 1])/2.0

print(median([7,3,1,4]))          #3.5
print(median([6, 8, 12, 2, 23]))  #3.0


