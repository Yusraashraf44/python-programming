names=[]
word=input("Enter first names separated by spaces: ")
names.append(word)
a_count=0
for name in names:
    a_count=name.lower().count('a')
    print("The letter 'a' appears ",a_count," times in the list")
