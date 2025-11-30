st=input('enter string ')
st=st.lower()
if st==st[::-1]:
    print(f'{st} is a palindrome string')
else:
    print(f'{st} is not a palindrome string')