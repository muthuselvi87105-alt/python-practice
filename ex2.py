num=int(input("enter the number:"))

if(num>100):
    print("large number")
elif(num>50 and num<100):
    print("medium number")
elif(num>1 and num<49):
    print("small number")
else:
    print("invalid")