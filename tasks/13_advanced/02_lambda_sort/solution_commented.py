n = int(input())
people = []
for _ in range(n):
    name, score = input().split()
    people.append((name, int(score)))

# Кортеж в key задаёт два правила: минус балла и имя по возрастанию.
people.sort(key=lambda person: (-person[1], person[0]))

for name, score in people:
    print(f"{name}: {score}")
