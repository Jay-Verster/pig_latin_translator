## PIG LATIN TRANSLATOR ##

## PROJECT STRUCTURE ##

# Notes: A Welcome message is displayed to the user.
print("\nWelcome to the Pig Latin Translator! Here you will be able to convert any sentence into Pig Latin!")

# Notes: Creating a string by getting input from the user which will be used later and translated into Pig Latin. The strip() function is used to remove any whitespace,
# and the lower() function is used to convert the entire string to lowercase
original = input("\nPlease enter the sentence you would like translated.\nSentence: ")

# Notes: Creating a list by using the split() function on the "original" string
original_list = original.split()

new_list = []

for word in original_list:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_list.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        consonant = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + consonant + "ay"
        new_list.append(new_word)

translated = " ".join(new_list)

print(translated)

# Those starting with a consonant or consonant cluster get split, added to the end of the word and the suffix "ay" is added.

# Append all new altered words to a list, and convert the list into a string which is displayed to the user