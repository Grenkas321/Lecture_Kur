has_positive = False
current_sum = 0
best_sum = 0
max_negative = -10**9

while True:
    num = int(input())
    if num == 0:
        break
    if num > 0:
        has_positive = True
    if not has_positive and num > max_negative:
        max_negative = num
    current_sum = max(0, current_sum + num)
    if current_sum > best_sum:
        best_sum = current_sum

print(best_sum if has_positive else max_negative)
