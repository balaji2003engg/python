"""
This program finds and prints elements that appear exactly twice in a given list.
It uses the Counter class from the collections module to count occurrences.
"""

from collections import Counter

# Sample data list containing some duplicate elements
data = ['a','b','a','c','c','e','c','f','f']

# Count the occurrences of each element in the data list
re = Counter(data)

# Initialize an empty list to store elements that appear exactly twice
result = []

# Print the counter object to show all counts
print(re)

# Iterate through the counter items (element, count)
for k, c in re.items():
    # Check if the count is exactly 2,  dictionay store the element as key and count as value
    if c == 2:
        # Add the element to the result list
        result.append(k)
        
# Print the elements that appear exactly twice
print("duplicates count with 2", result)    