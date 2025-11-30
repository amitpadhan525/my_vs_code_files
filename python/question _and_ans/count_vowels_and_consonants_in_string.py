string=input('enter string :')
vowel=0
consonants=0
for char in string:
    if char in 'aeiou':
        vowel+=1
    else:
        consonants+=1

print('vowels=',vowel)
print('consonants=',consonants)