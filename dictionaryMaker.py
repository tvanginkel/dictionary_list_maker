from itertools import combinations, permutations
import os
import enum

# Enum for size units
class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4

def convert_unit(size_in_bytes):
   """ Convert the size from bytes to other units like KB, MB or GB"""
   if 1000 <= size_in_bytes < 1000000:
       return  str(round(size_in_bytes/1024, 2)) + " KB"
   elif 1000000<= size_in_bytes < 1000000000:
       return  str(round(size_in_bytes/(1024 * 1024), 2)) + " MB"
   elif 1000000000 <= size_in_bytes < 1000000000000000:
       return  str(round(size_in_bytes/(1024 * 1024 * 1024),2)) + " GB"
   else:
       return str(size_in_bytes) + " bytes"

# Define the path to the output file
path = "wordlist.txt"

# The list of words to use
words = ['Word1', 'Word2', 'Word3'] 

print("=============================================================")
print("Wordlist: " + str(words) + "\n")
# Create/Open the file and empty it
open(path, "w").close()

# Open the file in append mode
f = open(path, "a")

total= 0
# Loop trough all the posibilities
for s in range(1+len(words)): 
    # Get all possible combinations
    for item in combinations(words, s):
        # Of each combination find all posible permutations
        for i in permutations(item):
            total+=1
print("* Generating " + str(total) + " combinations")
# Loop trough all the posibilities
for s in range(1+len(words)): 
    # Get all possible combinations
    for item in combinations(words, s):
        # Of each combination find all posible permutations
        for i in permutations(item):
            string = ""
            for b in i:
                string+=b # Casto tuple to a string
            if string != "":
                f.write(string + "\n") # Write to file

# Close the file                
f.close()
print("* Total file size: " + convert_unit(os.path.getsize(path)))
print("=============================================================")
