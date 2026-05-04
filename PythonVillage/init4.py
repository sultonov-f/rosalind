a = int(input())
b = int(input())

# first odd >= a
start = a if a % 2 != 0 else a + 1

# last odd <= b
end = b if b % 2 != 0 else b - 1

if start > end:
    print(0)
else:
    n = ((end - start) // 2) + 1
    total = n * (start + end) // 2
    print(total)
