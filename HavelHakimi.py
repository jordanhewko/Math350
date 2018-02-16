
import sys
def get_largest_element(sequence):

	largest = sequence[len(sequence) - 1]

	return int(largest)

def remove_last_element(sequence):

	del sequence[-1]
	return sequence

def reduce(sequence):

	largest = get_largest_element(sequence)
	sequence = remove_last_element(sequence)
	last_element = len(sequence)

	if largest > len(sequence):
		return False

	for i in range(largest, 0, -1):
		sequence[last_element - i] -= 1

	sequence.sort()

	return sequence

def print_sequence(sequence):

	print("sequence: [", end='')

	for i in range(0, len(sequence)):

		if i != (len(sequence) - 1):
			print(str(sequence[i]) + ", ", end='')

		else:
			print(str(sequence[i]) , end='')

	print("]")

def get_valid_integer(i):

	checker = False

	while(checker == False):

		number = input("enter digit number " + str(i) + ": ") 

		try:
			int(number)
			checker = True

		except ValueError:
			print("digit must be a number, try again.")

	return number

def build_sequence(in_string, end=''):

	sequence = in_string.split(",")

	for i in range(0,len(sequence)):
		sequence[i] = int(sequence[i])

	sequence.sort()

	return sequence

def is_odd(integer):

	if (integer % 2 == 0):
		return False
	else:
		return True

def check_handshake_lemma(sequence):

	count = 0
	for i in sequence:
		if (is_odd(i) == True):
			count += 1

	if is_odd(count):
		return False
	else:
		return True


def handle_opt(argv):

	if len(argv) != 2:
		print("usage: python3 HavelHakimi.py sequence")
		sys.exit(1)

	else:

		try:
			out_value = argv[1]
			return out_value

		except ValueError:

			print("ERROR")
			sys.exit(1)

def check_sequence(sequence):


	if (check_handshake_lemma(sequence) == False):
			print("Sequence is not a graph (handshake lemma)")
			return False

	while len(sequence) > 1:
		is_reducable = reduce(sequence)

		if is_reducable == False:
			print("Sequence is not a graph ")
			return False
	else:
		print("Sequence is a graph")
		return True

def check_euler(sequence):

	odd_numbers = 0
	for i in range(0, len(sequence)):
		if (sequence[i] % 2) != 0:
			odd_numbers += 1

	if odd_numbers == 2:
		print("Sequence is semi-Eulerian")
		return True
	elif odd_numbers > 2:
		print("Sequence is neither Eulerian or semi-Eulerian")
		return False
	else:
		print("Graph is Eulerian")
		return True


def main():

	sequence = handle_opt(sys.argv)
	sequence = build_sequence(sequence)
	result = check_sequence(sequence)
	if result == True:
		check_euler(sequence)

if __name__ == "__main__":
    main()