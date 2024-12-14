def separate_vowels_consonants(input_string):
    # Define vowels
    vowels = "aeiouAEIOU"

    # Use list comprehension to filter vowels and consonants
    #vowel_list = [char for char in input_string if char.isalpha() and char in vowels]
    consonant_list = [char for char in input_string if char.isalpha() and char not in vowels]

    #return vowel_list, consonant_list
    return consonant_list


# Example usage
input_string = "Hello World"
#vowels, consonants = separate_vowels_consonants(input_string)
consonants = separate_vowels_consonants(input_string)

#print("Vowels:", vowels)
print("Consonants:", consonants)