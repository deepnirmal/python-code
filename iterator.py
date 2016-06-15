numbers={'abc':'345','def':'234','xyz':'123'}

it= iter(numbers)

print(next(it))
print(next(it))
print(next(it))

for key in numbers:
	print(key,numbers[key])

