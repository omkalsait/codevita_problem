# First we required me a function to check to update the best time and best combination
def check_comb(comb,time):
    global best_time, best_comb
    if abs(time) < best_time:
        best_comb = comb
        best_time = abs(time)
        print('changed')
    print(best_comb,best_time)

# Then we require the logic to get best combination
def get_best(comb, ns):
    global v_list, n, half_time, flag
    comb.append(0)
    print(ns,n)
    for i in range(ns, n):
        if flag:
            break
        comb[-1]=v_list[i]
        time = half_time-sum(comb)
        check_comb(comb[:], time)
        if time==0:
            flag=True
            break
        elif time<0:
            continue
        else:
            get_best(comb[:],i+1)







# Now just take the input and show the output
v_list = input()
v_list = sorted(list(map(int, v_list.split())), reverse=True)
total_req = sum(v_list)
best_time = 10000
best_comb = []
n = len(v_list)
flag = False
half_time = int(total_req/2)
get_best([], 0)
print(max(sum(best_comb), total_req-sum(best_comb)))