#stored user input in two diff strings
str1 = input("Enter first word: ")
str2 = input("Enter second word: ")

#sorts both strings into a list
list1 = sorted(str1)
list2 = sorted(str2)

if(list1 == list2): #compare if sorted lists are equal
  print("You found an angram!")
else:
  print("These words are not anagrams")