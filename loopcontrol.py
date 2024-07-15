# BREAK STATEMENT

for num in range (1,11):
    if num == 6:
        break
    print(num)

courses = ['html','css','js','python','java','angular js','react js']
for course in courses:
    if course == 'python':
        break
    print(course)

# CONTINUE

for a in range (1,11):
    if a == 6:
        continue
    print(a)

# PASS 

for b in range (1,11):
    if b == 5:
        pass
    print(b)