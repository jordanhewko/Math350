
import sys
def get_largest_element(sequence):

	largest = sequence[len(sequence) - 1]
	print("largest element is " + str(largest))

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
	print_sequence(sequence)
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

def build_sequence(size, end=''):

	sequence = []

	for i in range(0,size):
		
		number = get_valid_integer(i) 
		sequence.append(int(number))

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
		print("usage: python3 HavelHakimi.py sequence_length")
		sys.exit(1)
	
	else:

		try:
			out_value = int(argv[1])
			return argv[1]

		except ValueError:
			
			print("Type Error: sequence_length must be an integer")
			sys.exit(1)



def main():

	size = handle_opt(sys.argv)
	sequence = build_sequence(int(size))
	
	print_sequence(sequence)
	if (check_handshake_lemma(sequence) == False):
			print("Sequence is not a graph (handshake lemma)")
			sys.exit(1)

	while len(sequence) > 1:
		is_reducable = reduce(sequence)
	
		if is_reducable == False:
			print("Sequence is not a graph ")
			sys.exit(1)
	else:
		print("Sequence is a graph")
		sys.exit(0)

main()