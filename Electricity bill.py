#electricity bill

a = int(input("Enter Previous Reading:-  "))
b = int(input("Enter current Reading:-  "))
c = b - a
print("Unit :-  ", c)
if(c<=150):
    payAmount=c*3.5
elif(c>=151) and (c<=250):
    payAmount=(150*3.5)+(c-150)*5
elif(c>=250):
    payamount=(150*3.5)+(250-150)*5+(c-250)*6
print("\nTotal amount = %.2f" %payAmount)
