import re
import os
import sys
import argparse

NO_DOT_ID_REGEX = ">(\S+)[^>]*"
DOT_ID_REGEX = ">(\S[^.]+)[^>]*"

parser = argparse.ArgumentParser(description="Seqeuence extractor for FASTA files.")
parser.add_argument('-d', action="store_true", dest="parse_dot", default=False, help="Indicate that the FASTA file has dots in the ID. Example: ENSRNOP00000049172.4")
parser.add_argument('id_filename', action="store", help="Path to a plaintext file of the IDs with one on each line.")
parser.add_argument('sequence_filename', action="store", help="Path to a FASTA file that contains the sequences with corresponding IDs you want to extract.")

def make_output_filename(filename):
	path = os.path.abspath(filename)
	directory = os.path.split(path)[0]
	full_filename = os.path.split(path)[1]
	base = os.path.splitext(full_filename)[0]
	extension = os.path.splitext(full_filename)[1]
	return os.path.join(directory, base+"_extracted"+extension)

def main():
	arguments = parser.parse_args()

	if not os.path.isfile(arguments.id_filename) or not os.path.isfile(arguments.sequence_filename):
		print "Please check that the paths to the ID file and sequence file are correct."
		return

	output_filename = make_output_filename(arguments.sequence_filename)

	with open (arguments.sequence_filename, "r") as sequence_file, open (arguments.id_filename, "r") as id_file, open(output_filename, "w+") as output_file:
		sequences = file.read(sequence_file)
		id_list = [line.strip() for line in id_file]
		regex = re.compile(DOT_ID_REGEX) if arguments.parse_dot else re.compile(NO_DOT_ID_REGEX)
		sequence_count = 0

		for sequence in regex.finditer(sequences):
			if sequence.group(1) in id_list:
				output_file.write(sequence.group())
				sequence_count += 1

		if sequence_count == 0:
			print "** Check that arguments were ordered correctly: python seqex.py ID_FILE SEQUENCE_FILE **"
			print "** FASTA file might have a dots in the ID.  Run again w/ the -d flag. **"

		print "Sequences extracted: " + str(sequence_count)
		print "Extracted file: " + output_filename

if __name__ == "__main__":
	main()
