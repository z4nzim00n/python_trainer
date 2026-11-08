import math

radians = float(input())

# math.degrees уже содержит формулу radians * 180 / pi.
degrees = math.degrees(radians)
print(f"Degrees: {degrees:.2f}")
