#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names=[]
letter=""
new_filename=""
with open("Input/Names/invited_names.txt") as data:
    for i in data:
        names.append(i)
with open("Input/Letters/starting_letter.txt") as data:
    letter=data.read()

for i in names:
    new_letter=letter.replace("[name]",i[:len(i)-1])
    new_filename=i[:len(i)-1]
    print(f"{i[:len(i)-1]}.txt")
    with open(f"Output/ReadyToSend/{new_filename}.txt",mode="w") as data:
        data.write(new_letter)


