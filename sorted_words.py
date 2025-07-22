my_str="Hello this is an example with cased letter"
words=[word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
    print(word)