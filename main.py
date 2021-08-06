# Computer Olympiad

def Input (n):
    a = {}
    for i in range(0,n):
        sex , name , language = input().split(sep=".")
        name = name.casefold()
        name = name.capitalize()
        a[sex] = (name,language)
    return a

repetition = int(input())
A = Input(repetition)

A = dict(sorted(A.items(),key=lambda item : (item[0],item[0][0])))

for k , v in A.items():
    print(f'{k} : {v}', end='\n')
