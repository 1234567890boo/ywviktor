file=open('fileGetFrom.txt','r')
fileDict={}
for line in file:
    line=line.strip()
    line=line.split()
    fileDict[line[0]]=float(line[1])
print(fileDict)
file.close()

#make tkinter that makes radio buttons with food name
#make text file with quiz questions