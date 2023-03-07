import sys
def decript(decript):
    resultStr=""
    i=0
    while i < len(decript)-1:
        if decript[i]!=".":
            resultStr += decript[i]
        if decript[i]=="." and decript[i+1]==".":
            resultStr=resultStr[0:len(resultStr)-1]
            i+=1
        i+=1
    if decript[-1]!=".":
        resultStr+=decript[-1]
    print(resultStr)
if __name__ == "__main__":
    decript(sys.stdin.read())