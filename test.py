import HavelHakimi


def check_sequence():

	test = [
	[1,1,2,3,3,4,5,5,6,8,10],
	[2,2,4,4,4,4],
	[2,3,3,4,4],
	]
	for i in range(0, len(test)):
		test_result = HavelHakimi.check_sequence(test[i])

def check_euler():

	test = [
	[1,1,2,3,3,4,5,5,6,8,10],
	[2,2,4,4,4,4],
	[2,3,3,4,4],
	]
	for i in range(0, len(test)):
		test_euler_result = HavelHakimi.check_euler(test[i])


def main():

	check_sequence()
	check_euler()

if __name__ == "__main__":
    main()