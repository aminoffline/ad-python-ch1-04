# Computer Olympiad

def Input (n):
    a = []
    for i in range(0,n):
        sex , name , language = input().split(sep=".")
        name = name.casefold()
        name = name.capitalize()
        a.append((sex,name,language))
    return a

repetition = int(input())
A = Input(repetition)
A = sorted(A,key=lambda tup : (tup[0],tup[1]))

for j in A:
    j = str(j)
    j = j.replace(": ", ":")
    j = j.replace("(", "")
    j = j.replace(")", "")
    j = j.replace(", ", " ")
    j = j.replace("'", "")
    j = j.replace('"', '')
    print(j , end="\n")