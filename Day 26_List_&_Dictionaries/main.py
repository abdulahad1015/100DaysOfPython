
import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
file=pandas.read_csv("nato_phonetic_alphabet.csv")
file_dict= {row.letter:row.code for (index,row) in file.iterrows()}

#print(file_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_list=[]
word=input("Enter a word: ")
for i in word.upper():
    word_list.append(file_dict[i])

print(word_list)