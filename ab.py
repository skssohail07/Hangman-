file=open("E://wordlist2.txt","r")
list1=[]
for line in file:
    line_strip=line.strip()
    line_split=line_strip.split()
    list1.append(line_split)

file.close()
#print(list1)

listfinal=[]
for i in list1:
    for j in i:
        listfinal.append(j)
        

print(listfinal)



        
