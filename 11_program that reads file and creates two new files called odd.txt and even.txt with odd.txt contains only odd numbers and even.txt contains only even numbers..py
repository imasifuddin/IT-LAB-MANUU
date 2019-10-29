
# integer value.txt, even.txt and odd.txt are in same location in python file


f=open("integer value.txt",'r')

for i in f:
    if int(i)%2==0:
        f1=open("even.txt",'a')
        f1.write(i)
        f1.close()
    else:
        f2=open("odd.txt",'a')
        f2.write(i)
        f2.close()

f.close()

print("Before spliting the numbers are")
f=open("integer value.txt",'r')
print(f.read())

print("After spliting, even numbers are")
f1=open("even.txt",'r')
print(f1.read())

print("After spliting, odd numbers are")
f2=open("odd.txt",'r')
print(f2.read())

f.close()
f1.close()
f2.close()
