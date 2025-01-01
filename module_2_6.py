import random
n = random.randint(3, 20)
result = []
for i in range(1, 20):
    for j in range(1, 20):
        if n % (i + j) == 0 and i != j:
            result.append([i,j])
        elif i < 19 and i + j < n:
            continue
        else:
            break
    if i >= n:
        break
for i in range(len(result)):
    result[i].sort()
check_ = []
for i in range(len(result) - 1):
    if i == len(result) - 1:
        break
    for j in range(i + 1, len(result)):
        if j == len(result):
            break
        elif result[i] == result[j]:
            check_.append(result[i])
result = []
zero = []
for i in range(len(check_)):
    zero = check_[i]
    for j in range(len(zero)):
        result.append(zero[j])
print(n, ' - ', *result)
