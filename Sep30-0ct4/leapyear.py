year=int(input("Enter the year:"))
for i in range(2024,year+1):
    if(i%4==0 and i%100!=0):
        print(i)
