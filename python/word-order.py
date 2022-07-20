from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]

print(len(Counter(words).keys()))
for count in Counter(words).values():
    print(count, end=' ')