import re, os, sys

ID_REGEX = ">(\S+)[^>]*"
OUTPUT_FILE = "output.txt"

def main(id_filename, sequence_filename):
	with open (sequence_filename, "r") as sequence_file, open (id_filename, "r") as id_file, open(OUTPUT_FILE, "w+") as out_file:
		sequences = file.read(sequence_file)
		id_list = [line.strip() for line in id_file]
		regex = re.compile(ID_REGEX)
		for sequence in regex.finditer(sequences):
			if sequence.group(1) in id_list:
				out_file.write(sequence.group())

if __name__ == "__main__":
	if len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
	else:
		print "Usage: python seqex.py id_file sequence_file"