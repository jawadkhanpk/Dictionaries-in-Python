programming_dictionaries = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Program": "Set of rules and techniques that tells the computer what to do and how to do",
}

print(programming_dictionaries)
# to add the key and value in the dictionary we use....
programming_dictionaries["Loop"] = "repetition of something is called loop"

print(programming_dictionaries)


#creating an empty dictionary

empty_dictionary = {}

# wipe previous dictionary
programming_dictionaries = {}
print(programming_dictionaries)


# loop through a dictionary
for key in programming_dictionaries:
    print(key)
    print(programming_dictionaries[key])