"""This is the entry point of the program."""


def highest_number_cubed(limit):
	for i in range(1, limit):
		if i**3 < limit:
			continue
		else:
			break

	return (i-1)

print(highest_number_cubed(12000))