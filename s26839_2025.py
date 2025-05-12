#Orginal
import random

length = int(input("Enter the sequence length: "))
seq_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
name = input("Enter your name: ")

nucleotides = ["A", "C", "G", "T"]
sequence = ''.join(random.choice(nucleotides) for _ in range(length))

insert_pos = random.randint(0, len(sequence))
sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]

a_count = sequence.count("A")
c_count = sequence.count("C")
g_count = sequence.count("G")
t_count = sequence.count("T")
total = a_count + c_count + g_count + t_count

perc_A = (a_count / total) * 100
perc_C = (c_count / total) * 100
perc_G = (g_count / total) * 100
perc_T = (t_count / total) * 100
cg_ratio = (c_count + g_count) / (a_count + t_count)

filename = f"{seq_id}.fasta"
with open(filename, "w") as f:
    f.write(f">{seq_id} {description}\n")
    f.write(sequence_with_name + "\n")

print(f"The sequence was saved to the file {filename}")
print("Sequence statistics:")
print(f"A: {perc_A:.1f}%")
print(f"C: {perc_C:.1f}%")
print(f"G: {perc_G:.1f}%")
print(f"T: {perc_T:.1f}%")
print(f"%CG: {perc_C + perc_G:.1f}")