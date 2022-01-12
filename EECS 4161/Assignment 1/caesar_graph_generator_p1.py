from matplotlib import pyplot as plt

# Necessary Variables
inputReader = open("input.txt", "r")
charFreq = {}

# Populate dictionary charFreq with empty entries [a,z]
for i in range(97, 123):
    charFreq[chr(i)] = 0

# Iterate through input and record number of characters read so far...
for line in inputReader.readlines():
    for j in line:
        if j.lower() in charFreq.keys():
            charFreq[j.lower()] += 1

# Information Prompt
print("EECS 4161 == Assignment #1 Helper Program ==")
print("The frequency of the letters of the alphabet in English (By Most Frequent):")
print("\t E @ 11.2%")
print("\t A @ 8.5%")
print("\t R @ 7.6%")
print("\t I @ 7.5%")
# Graphing the Character Frequency
plt.style.use("seaborn")
plt.bar(charFreq.keys(), charFreq.values(), label="Ciphertext")
plt.xlabel("Characters")
plt.ylabel("Frequency")
plt.title("Ciphertext Character Frequency Visualizer")
plt.legend()
plt.show()
inputReader.close()



