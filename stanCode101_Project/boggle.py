"""
File: boggle.py
Name: Anthony Ning
----------------------------------------
The program first asks the user to enter four rows of input (alphabet).
Then the program will find all possibilities of combinations of alphabets and their adjacent neighbors.
If the combination is a word in the dictionary, the program will print it out,
and at last calculate the number of words it found.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	We first put all words in the dictionary into a list.
	Then the program will ask the user to enter four rows of alphabets.
	After that, function 'anagrams' will be executed.
	We will find all combinations of alphabets, and check whether the combination is a word in the dictionary.
	At last, we will print out the number of words the program found.
	"""
	# used to detect the viability of inputs
	illegal = False
	# put all words in the dictionary into the list, all_vocab
	all_vocab = []
	read_dictionary(all_vocab)
	while True:
		row_1 = input('1 row of letters: ')
		row_1 = row_1.split(' ')
		for i in range(len(row_1)):
			if not row_1[i].isalpha() or len(row_1[i]) != 1:
				print('Illegal input')
				illegal = True
				break
		if illegal:
			break
		row_2 = input('2 row of letters: ')
		row_2 = row_2.split(' ')
		for i in range(len(row_2)):
			if not row_2[i].isalpha() or len(row_2[i]) != 1:
				print('Illegal input')
				illegal = True
				break
		if illegal:
			break
		row_3 = input('3 row of letters: ')
		row_3 = row_3.split(' ')
		for i in range(len(row_3)):
			if not row_3[i].isalpha() or len(row_3[i]) != 1:
				print('Illegal input')
				illegal = True
				break
		if illegal:
			break
		row_4 = input('4 row of letters: ')
		row_4 = row_4.split(' ')
		for i in range(len(row_4)):
			if not row_4[i].isalpha() or len(row_4[i]) != 1:
				print('Illegal input')
				illegal = True
				break
		if illegal:
			break

		start = time.time()
		# word_lst is used to store the combination that is a word in the dictionary
		word_lst = []
		anagrams(row_1, row_2, row_3, row_4, [], word_lst, all_vocab)
		print('There are '+str(len(word_lst))+' words in total.')
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')
		break


def read_dictionary(words):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			words.append(line.strip())


def anagrams(r1, r2, r3, r4, location_lst, word_lst, all_vocab):
	# The function is used to find all combinations of alphabets and their adjacent neighbors,
	# and after that, it will check if the combination is a word in the dictionary
	for i in range(4):
		for j in range(4):
			start_point = (i, j)
			location_lst.append(start_point)
			anagrams_helper(r1, r2, r3, r4, start_point, location_lst, word_lst, all_vocab)
			location_lst.pop()


def anagrams_helper(r1, r2, r3, r4, start_point, location_lst, word_lst, all_vocab):
	if len(location_lst) >= 4:
		word = string_manipulation(r1, r2, r3, r4, location_lst)
		exist = check_dictionary(word, all_vocab)
		if exist and word not in word_lst:
			word_lst.append(word)
			print('Found: '+word)

	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			row = start_point[0]
			column = start_point[1]
			row += i
			column += j
			if (row, column) not in location_lst:
				if 0 <= row < 4 and 0 <= column < 4:
					# choose
					location_lst.append((row, column))
					prefix = string_manipulation(r1, r2, r3, r4, location_lst)
					prefix_exist = has_prefix(prefix, all_vocab)
					# explore
					if prefix_exist:
						anagrams_helper(r1, r2, r3, r4, (row, column), location_lst, word_lst, all_vocab)
					# un-choose
					location_lst.pop()


def has_prefix(sub_s, all_vocab):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in all_vocab:
		if word.startswith(sub_s):
			return True
	return False


def string_manipulation(r1, r2, r3, r4, location_lst):
	# the function turns coordinates of alphabets into a string
	word = ''
	for i in range(len(location_lst)):
		if location_lst[i][0] == 0:
			position = location_lst[i][1]
			word += r1[position]
		elif location_lst[i][0] == 1:
			position = location_lst[i][1]
			word += r2[position]
		elif location_lst[i][0] == 2:
			position = location_lst[i][1]
			word += r3[position]
		elif location_lst[i][0] == 3:
			position = location_lst[i][1]
			word += r4[position]
	return word.lower()


def check_dictionary(word, all_vocab):
	# check if the combination is a word in the dictionary
	if word in all_vocab:
		return True
	return False


if __name__ == '__main__':
	main()
