def split(word):
    return [char for char in word]
def apply_check(x,broom):
    endf = True
    for i in range(len(broom)):
        if x == broom[i]:
            broom = broom[i+1:] + broom[:i]
            endf = False
            break

    return broom, endf

n = int(input())
left = n
brideq=split(input())
broomq= split(input())
for i in range(n):
    broomq , endf = apply_check(brideq[i],broomq)
    if endf == False:
        left -=1

    if left==0 or endf == True:
        break
print(left)