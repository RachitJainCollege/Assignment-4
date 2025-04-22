a=input("Enter text to write to the file :")
file=open('output.txt','w')
wr = file.write(a)
print ("Data successfully written to output.txt")

b=input("\n\nEnter additional text to append : \n")
file=open('output.txt','a')
wr = file.write(b)
print ("Data successfully appended")

print("\n\nFinal content of output.txt: ")
file=open('output.txt','r')
r = file.read()
print (r)
file.close