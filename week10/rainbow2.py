n, k = map(int, input().split())
P = list(map(int, input().split()))

color_pos = [[] for _ in range(k+1)]
for i in range(n):
    color_pos[P[i]].append(i)

min_length = float('inf')
for i in range(n):
    max_pos = i
    for color in range(1, k+1):
        pos = [x for x in color_pos[color] if x >= i]
        if not pos:
            break
        max_pos = max(max_pos, pos[0])
    else:
        if is_rainbow(0, i) and is_rainbow(max_pos+1, n):
            min_length = min(min_length, max_pos-i+1)

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)
