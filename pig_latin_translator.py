## PIG LATIN TRANSLATOR ##

## PROJECT STRUCTURE ##

# Notes: A Welcome message is displayed to the user.
print("\nWelcome to the Pig Latin Translator! Here you will be able to convert any sentence into Pig Latin!")

# Notes: Creating a string by getting input from the user which will be used later and translated into Pig Latin. The strip() function is used to remove any whitespace,
# and the lower() function is used to convert the entire string to lowercase
original = input("\nPlease enter the sentence you would like translated.\nSentence: ")

# Notes: Creating a list by using the split() function on the "original" string
original_list = original.split()

# Notes: Below I create an empty list which will store the translated words.
new_list = []

# Notes: Creating a for-loop that will run through each word in original_list and translate and append it accordingly.
for word in original_list:
    
    # Notes: if-statement that will add "yay" to the end of words in original_sentence that start with a vowel, and append it to new_list
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_list.append(new_word)
        
    # Notes: An else-statement that will run in the case that the word doesn't start with a vowel. Each time the loop runs, a temporary variable called vowel_position
    # with a 0 value is created. This will later be used to determine the index location of the first vowel in the word.
    else:
        vowel_position = 0
        
        # Notes: A for-loop that will itirate through each letter in words not starting with a vowel. For each consonant counted, the value of vowel_position is increased by 1.
        # This will run continuously until the loop encounters the first vowel in the word.
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        # Notes: Temporary variables created withing the for-loop in order to create the translated word. The "consonant" variable saves the part of the word after the index
        # position of "vowel_position, and "the_rest saves the part of the word up until the index value of "vowel_position".
        consonant = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + consonant + "ay"
        new_list.append(new_word)

translated = " ".join(new_list)

print(translated)
