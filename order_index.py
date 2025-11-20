# import Bio
import math
import sys
from datetime import datetime

print(datetime.now())

# current_sequence_file_path = "test_sequences/toy_sequence.txt"
current_sequence_file_path = "final_candidates_output/SRR12340680-50k/gdtools_output_SRR12340680-50k.txt"

with open(current_sequence_file_path, 'r', encoding='utf-8') as file:
    file_contents = file.read()

current_sequence = file_contents.replace("\n","")
current_sequence = current_sequence.upper()
current_sequence = current_sequence.replace("N","")

N = len(current_sequence)
k = 4
L = N - k + 1
p = (current_sequence.count("A") + current_sequence.count("T")) / N
q = 1 - p
k_mers = []
L_m_values = [0] * (k + 1)
deviation_distance = 0
normalized_deviation_distance = 0

# getting k-mers
for nucleotide_index in range(L):
    if nucleotide_index < L:  
        k_mers.append(current_sequence[nucleotide_index:nucleotide_index + k])

# determining L set values
for k_mer in k_mers:
    L_m_values[k_mer.count("A") + k_mer.count("T")] += 1

# getting deviation from expected randomization
for m,L_m_value in enumerate(L_m_values):
    deviation_distance += abs(L_m_value - (N * math.comb(k,m) * (p**m) * (q**(k -  m))))/L
# deviation_distance = deviation_distance/L

# normalizing to AT/GC ratio (p/q)
normalized_deviation_distance = deviation_distance/(2 - (2 * (p**k + q**k)))

# print(k_mers)
print(L_m_values)
print("p is ", p)
print("q is ", q)
print(normalized_deviation_distance)
print(datetime.now())
sys.exit()