paragraph=input("Enter the pragraph  ")
words=paragraph.split()
print('palindromic words are:  ')
for i in range (len(words)):
    if words[i]==words[i][::-1]:
        print(f'{i}.',words[i])

