try:
    file = open('sample.txt','r')
    read = file.readline()
    read2 = file.readline()
    print ("Reading file content:")
    print ("line 1:",read,"\nline 2:",read2)
    file.close
except :
    print ("Error:The file 'Sample.txt' was not found")