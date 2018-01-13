
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
	last_element = len(sequence) - 1

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

def build_sequence(size, end=''):

	sequence = []

	for i in range(0,size):

		number = input("enter digit number " + str(i) + ": ") 
		sequence.append(int(number))

	sequence.sort()

	return sequence

def main():

	size = input("Enter the length of the sequence: ")
	sequence = build_sequence(int(size))
	
	print_sequence(sequence)
	while len(sequence) > 1:
		is_reducable = reduce(sequence)
	#is_reducable = reduce(sequence)

	if is_reducable == False:
		print("Sequence is not a graph")
	else:
		print("Sequence is a graph")


main()