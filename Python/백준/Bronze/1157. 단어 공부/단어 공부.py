a = input()
a = list(a.upper())

l = [0 for i in range(26)]  # List to store the frequency of each letter
for i in a:
    if 'A' <= i <= 'Z':  # Check if the character is a letter
        l[ord(i) - 65] += 1  # Update the frequency of the corresponding letter

max_ = 0
tie = False  # Flag to check if there's a tie
result = ''

# Find the letter with the highest frequency
for i in range(26):
    if l[i] > max_:
        max_ = l[i]
        result = chr(i + 65)  # Store the most frequent letter
        tie = False  # Reset the tie flag as we have a new max frequency
    elif l[i] == max_:
        tie = True  # Set the flag if there's a tie

# Output the result
if tie:
    print("?")
else:
    print(result)
