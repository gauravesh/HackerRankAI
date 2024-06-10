
# Enter your code here. Read input from STDIN. Print output to STDOUT
size=int(input())
twoD=list()
for i in range(size):
    temp=input()
    twoD.append(temp)
for i in range(size):
    for j in range(size):
        if twoD[i][j]=='m':
            rowM=i
            colM=j
        if twoD[i][j]=='p':
            rowP=i
            colP=j
numberCols=colP-colM
numberRows=rowP-rowM

while numberRows !=0 or   numberCols != 0:
    if numberRows <0:
        print("LEFT")
        numberRows = numberRows+1
    elif numberRows >0:
        print("RIGHT")
        numberRows=numberRows-1
    if numberCols <0:
        print("UP")
        numberCols+=1
    elif numberCols >0:
        print("DOWN")
        numberCols=numberCols-1
