#Orginal
# import random

# length = int(input("Enter the sequence length: "))
# seq_id = input("Enter the sequence ID: ")
# description = input("Provide a description of the sequence: ")
# name = input("Enter your name: ")

# nucleotides = ["A", "C", "G", "T"]
# sequence = ''.join(random.choice(nucleotides) for _ in range(length))

# insert_pos = random.randint(0, len(sequence))
# sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]

# a_count = sequence.count("A")
# c_count = sequence.count("C")
# g_count = sequence.count("G")
# t_count = sequence.count("T")
# total = a_count + c_count + g_count + t_count

# perc_A = (a_count / total) * 100
# perc_C = (c_count / total) * 100
# perc_G = (g_count / total) * 100
# perc_T = (t_count / total) * 100
# cg_ratio = (c_count + g_count) / (a_count + t_count)

# filename = f"{seq_id}.fasta"
# with open(filename, "w") as f:
#     f.write(f">{seq_id} {description}\n")
#     f.write(sequence_with_name + "\n")

# print(f"The sequence was saved to the file {filename}")
# print("Sequence statistics:")
# print(f"A: {perc_A:.1f}%")
# print(f"C: {perc_C:.1f}%")
# print(f"G: {perc_G:.1f}%")
# print(f"T: {perc_T:.1f}%")
# print(f"%CG: {perc_C + perc_G:.1f}")







# Improved

import random
import sys

# ORIGINAL:
# length = int(input("Enter the sequence length: "))
# MODIFIED (justification: added input validation for better robustness):
def get_sequence_length():
    while True:
        try:
            length = int(input("Enter the sequence length: "))
            if length <= 0:
                raise ValueError
            return length
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

length = get_sequence_length()
seq_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
name = input("Enter your name: ")

nucleotides = ["A", "C", "G", "T"]
sequence = ''.join(random.choice(nucleotides) for _ in range(length))

insert_pos = random.randint(0, len(sequence))
sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]

# ORIGINAL:
# a_count = sequence.count("A")
# MODIFIED (justification: used Counter for efficiency):
from collections import Counter
counts = Counter(sequence)
a_count = counts.get("A", 0)
c_count = counts.get("C", 0)
g_count = counts.get("G", 0)
t_count = counts.get("T", 0)

total = a_count + c_count + g_count + t_count

perc_A = (a_count / total) * 100
perc_C = (c_count / total) * 100
perc_G = (g_count / total) * 100
perc_T = (t_count / total) * 100
cg_ratio = (c_count + g_count) / (a_count + t_count)

filename = f"{seq_id}.fasta"
try:
    with open(filename, "w") as f:
        f.write(f">{seq_id} {description}\n")
        # ORIGINAL:
        # f.write(sequence_with_name + "\n")
        # MODIFIED (justification: wrap at 60 characters per FASTA format):
        for i in range(0, len(sequence_with_name), 60):
            f.write(sequence_with_name[i:i+60] + "\n")
except IOError as e:
    print(f"Error writing to file {filename}: {e}", file=sys.stderr)
    sys.exit(1)

print(f"The sequence was saved to the file {filename}")
print("Sequence statistics:")
print(f"A: {perc_A:.1f}%")
print(f"C: {perc_C:.1f}%")
print(f"G: {perc_G:.1f}%")
print(f"T: {perc_T:.1f}%")
print(f"%CG: {perc_C + perc_G:.1f}")
