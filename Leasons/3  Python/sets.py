#use sets if values are unique

s = set()

s.add(1)
s.add(4)
s.add(2)
s.add(3)
s.add(1)

print(s)

s.remove(2)

print(f"It has {len(s)} elements")