
'''running this script will read in eng-ood_NT.tsv and return three files
eng-ood_train.txt, eng-ood_dev.txt, and eng-ood_test.txt'''

# open and read tsv file of parallel verses line by line
with open('eng-ood_NT.tsv') as inp:
	lines = inp.readlines()

# make txt files to write preprocessed text to
with open("eng-ood_train.txt", 'w') as train_file:
	with open("eng-ood_dev.txt", 'w') as dev_file:
		with open("eng-ood_test.txt", 'w') as test_file:

			# assign index to each line with enumerate()
			# remember each line in the tsv file is a verse
			for i,line in enumerate(lines):
				# strip extra white space from each line
				# split the source and target language at tab
				line = line.strip().split('\t')
				# assign the variable eng to index line[1] and strip white space
				eng = line[1].strip()
				# assign the variable ood line[2] and strip white space
				ood = line[2].strip()

				# use modulo operator on the verse's index to sep 10% of data to dev, 10 % to test, 
				# and remaining 80% to train
				# if the remainder of i/10 equals 0
				# write lines with orth tag, source language, triple bar, and target language to dev set
				if i % 10 == 0:
					dev_file.write(f"<sax> {eng} ||| {ood}\n")
				# # if the remainder of i/10 equals 1
				# write lines with orth tag, source language, triple bar, and target language to test set
				elif i % 10 == 1:
					test_file.write(f"<sax> {eng} ||| {ood}\n")
				# write remaining lines to train
				else:
					train_file.write(f"<sax> {eng} ||| {ood}\n")







