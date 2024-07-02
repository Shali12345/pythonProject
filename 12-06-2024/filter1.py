letters= ['w', 'i','h','j','e']

def find_vowels(letters):
    vowels= ['a','e','i','o','u']
    return letters in vowels


new_list= filter(find_vowels, letters)
print(list(new_list))