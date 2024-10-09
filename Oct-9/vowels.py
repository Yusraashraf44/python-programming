vowels=['a','e','i','o','u','A','E','I','O','U']
vowel_found=[]
word=input("Enter a word:")
for i in word:
    if i in vowels:
        vowel_found.append(i)
if vowel_found:
    print(vowel_found)
else:
    print("vowels are not found")
    
