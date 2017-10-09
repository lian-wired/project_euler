# Answer 1
s = 0
for i in range(1000):
	if i % 3 == 0 or i % 5== 0:
		s+= i
print(s)


# Answer 2
print(sum(set(range(0,1000,3)) | set(range(0,1000,5))))

# Answer 3
print(sum([n for n in range(1000) if n % 3 == 0 or n % 5 == 0]))

