v = int(input())
t = int(input())

d = 109

print(str((((v * t) % d) + d) % d))