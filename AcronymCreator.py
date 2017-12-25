# reading Input file
infile = open("data.txt")
content=infile.readlines()

# Getting data into list
content = [x.strip() for x in content]
listdata=[]

# Check for Equal String
def checkEqual(myList):
   return all(x==myList[0] for x in myList)

# Traversing the string and creatin acronym
for i in content:
    words = i.split()
    if(checkEqual(content)):
        temp = ''.join(w[0].upper() for w in words)
        listdata.append(temp)
    else:
        temp= ''.join(w[0].upper() for w in words)
        if temp not in listdata:
            listdata.append(temp)
        else:
            value=''.join(words[0][:2].upper())
            words.pop(0)
            temp = ''.join(w[0].upper() for w in words)
            temp=''.join(value+temp)
            if temp not in listdata:
                listdata.append(temp)
            else:
                listdata.append('Error: Cannot find unique acronym for')
    temp = ''

# printing the Desired Output
for i in range(len(content)):
    print listdata[i]+'->' +content[i]