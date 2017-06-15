# November 20, 2016

def main():

	word_ct = 0
	length_ct = 0
	line_words = str(input("Enter a line of words, press Enter to stop: "))

	if len(line_words) == 0:
		print("\n")
		print("Number of words seen: ", word_ct)
		print("Average length of words: ", length_ct)


	while len(line_words) != 0:
		while len(line_words) !=0:
			word_split = len(line_words.split())
			word_ct += word_split
			length_split = line_words.split()
			length_ct += len("".join(length_split[:]))
			line_words = str(input("Enter a line of words, press Enter to stop: "))
	
		length_average = (length_ct/word_ct)
		print("\n")
		print("Total number of words seen:", word_ct)	
		print("Average length of words: ", length_average)	
main()
