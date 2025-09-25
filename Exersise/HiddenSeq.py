P = eval(input())
Q = eval(input())

for elem in P:
    if elem not in Q:
        print("NO")
        exit()

if len(P) == 1:
    print("YES")
    exit()

pos_dict = {}
for idx, val in enumerate(Q):
    if val not in pos_dict:
        pos_dict[val] = []
    pos_dict[val].append(idx)

for start in pos_dict[P[0]]:
    max_step = (len(Q) - start) // (len(P) - 1)
    for d in range(1, max_step + 1):
        current_idx = start
        found = True
        for i in range(1, len(P)):
            current_idx += d
            if current_idx >= len(Q):
                found = False
                break

            if current_idx not in pos_dict[P[i]]:
                found = False
                break
        if found:
            print("YES")
            exit()

print("NO")
