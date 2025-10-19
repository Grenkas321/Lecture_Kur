import sys

lines = [line.strip() for line in sys.stdin if line.strip()]

start = lines[-2]
end = lines[-1]

graph = {}
for line in lines[:-2]:
    a, b = line.split()
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

go = set()
stack = [start]

while stack:
    cur = stack.pop()
    if cur == end:
        print("YES")
        break
    if cur not in go:
        go.add(cur)
        if cur in graph:
            stack.extend(graph[cur])
else:
    print("NO")        