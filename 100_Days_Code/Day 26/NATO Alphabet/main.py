# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# DAY 26 END NATO ALPHABET PROJECT
import pandas
# import gtts
# from playsound import playsound

# Create a pandas DataFrame from the CSV
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)
# print(type(df))
# print(df.__repr__)
# Create dictionary from the pandas DataFrame
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(new_dict)

# Create a list of the phonetic code words from a word that the user inputs.
user_word = ""

while user_word != "EXIT":
    user_word = input("Please enter a word (Type 'EXIT' to quit): ").upper()
    try:
        user_nato = [phonetic_dict[char] for char in user_word]
    except KeyError:
        print(
            f"Sorry {user_word} is not valid.  Please only use letters in the english alphabet, no spaces.")
        user_word = input(
            "Please enter a word (Type 'EXIT' to quit): ").upper()
        continue
    else:
        print(f"{user_nato}\n")
    # nato_tts = [gtts.gTTS(word).save(f"{word}.mp3") for word in user_nato]
    # print(nato_tts)
    # for speech in user_nato:
    #     speech_word_file = f"{speech}.mp3"
    #     speech_word = gtts.gTTS(speech)
    #     speech_word.save(speech_word_file)
    #     print(speech_word_file)
    #     print(type(speech_word_file))
    #     playsound(speech_word_file)

    # tts= gtts.gTTS("Danny")
    # tts.save("Danny.mp3")
    # speech_word = "Danny"
    # playsound(f"{speech_word}.mp3")
