n = input()
n = list(map(int, str(n)))

output = []

current = 0
for i in range(len(n)):
    while (current < n[i]):
        output.append('(')
        current += 1
    while (current > n[i]):
        output.append(')')
        current -= 1
    output.append(n[i])
while(current):
    output.append(')')
    current -= 1

print(''.join(map(str, output)))
