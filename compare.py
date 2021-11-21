from collections import Counter
import os

# Declaring variables
Acids = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'B': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
directory = "./docs/"
data = []
compared_data = []
total_length = 0
i = 0
length_check = True

# Defining read_fasta function
def read_fasta(arq):
  seq = ""
  with open(arq) as f:
    f.readline()
    for line in f:
      seq += line.strip()
  return seq

# Defining treat_data function
# Receives a string of data to be treated
# Returns the count and sort the data ascending
def treat_data(data_to_treat):
  Acids.update(Counter(data_to_treat))
  return sorted(Acids.items())

# Defining compare_data function
# Receives 2 arrays of data and compare the values of each array by subtracting
# Returns compared data: letter of the acid + the difference between each array
def compare_data(data_array1, data_array2):
  return data_array1[0], abs(data_array1[1] - data_array2[1])

# Defining filter_total_differences function
# Receives the compared data
# Return only the data that has differences
def filter_total_differences(comparison):
  return filter(lambda  x: x[1] > 0, comparison)

# Defining simple_variation function
# Receives the total number of different values
# Returns the result of simple variation calculus
def simple_variation(different_values):
  return (total_length - (total_length - different_values)) / total_length

# Iterates over the given directory to find files with the .fasta extension 
for filename in os.listdir(directory):
  if filename.__contains__(".fasta"):
    data_to_treat = read_fasta(directory + filename) # Reading the file
    if total_length == 0: total_length = len(data_to_treat) # Getting the total number of acids
    elif total_length != len(data_to_treat): break; print("Not all sequences are the same length!"); length_check = False # If lengths don't match
    data.append((filename.split(".fasta")[0], treat_data(data_to_treat))) # Treat data and append on the data object

# If lengths match
if length_check:
  while i < (len(data) - 1): # Iterates over the data array
    y = i + 1
    while y < len(data): # Comparing animals with each other
      differences = dict(filter_total_differences(list(map(compare_data, data[i][1], data[y][1])))) # Check all differences
      compared_data.append((data[i][0], data[y][0], simple_variation(sum(differences.values())))) # Append filtered data to the compared_data array
      y += 1
    i += 1

print(compared_data)