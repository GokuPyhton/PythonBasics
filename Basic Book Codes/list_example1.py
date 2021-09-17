vowels = ['a', 'e', 'i', 'o', 'u']
#word = "Milliways"
word = input("Provide any word to input = ")
found = []

for letter in word:

    if letter in vowels:

        if letter not in found:

            #inserting object in list
            found.append(letter)

            
for vowel in found:
    print(vowel)
