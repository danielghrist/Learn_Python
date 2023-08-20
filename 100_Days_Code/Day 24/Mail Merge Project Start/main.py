# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

names_list = []

with open("Input/Names/invited_names.txt", "r") as name_file:
    read_names = name_file.read()
    names_list = read_names.split("\n")

with open("Input/Letters/starting_letter.txt") as template_file:
    contents = template_file.read()
    for name in names_list:
        write_contents = contents.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}_letter.txt", "w") as write_file:
            write_file.write(write_contents)










# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
