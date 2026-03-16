num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
operator=(input("enter the operator:"))

if(operator =="+"):
   print("addition:",num1+num2)
elif(operator =="-"):
   print("subtraction:",num1-num2)
elif(operator =="*"):
   print("multiplication:",num1*num2)
elif(operator =="/"):
   print("division:",num1/num2)
elif(operator =="%"):
   print("modulus:",num1%num2)
elif(operator =="**"):
   print("exponent:",num1**num2)
elif(operator =="//"):
   print("floordivision:",num1//num2)
else:
   print("not matching")