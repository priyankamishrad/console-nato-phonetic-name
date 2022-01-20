import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for(index,row) in data.iterrows()}
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("What word do you want to be broken down?: ").upper()

# Method 1: List comprehension
# output = [ new_dict[i] for i in user_input]
# print(output)

# Method 2: Nested loops
final = []
for i in user_input:
    for (index,row) in data.iterrows():
        if i == row.letter:
            final.append(row.code)

print(final)
