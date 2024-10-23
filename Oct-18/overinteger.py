num=int(input("Enter the no of integers to be inputed:"))
integers=[]
for i in range(num):
    integer=int(input("Enter the integer:"))
    integers.append(integer)
    if (integer>100):
       integers[i]="over"
print(integers)
