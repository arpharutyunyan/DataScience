import string
text_data = [
    'Test!!!! hello. esim. test2...',
    '100% ola!! #HashTag',
    'testText???!!?'
]
cleared=[]
for line in text_data:
    for letters in line:
        if letters in string.punctuation:
            line=line.replace(letters, "")
    cleared.append(line)
print(cleared)