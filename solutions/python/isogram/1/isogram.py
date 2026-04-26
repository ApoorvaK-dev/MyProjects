def cleantext(text):
    punctuation = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    clean_text = ""

    for char in text:
        if char not in punctuation:
            clean_text += char
    return clean_text

def is_isogram(string):
    x = ' '.join(cleantext(string.lower()))
    y = x.split()
    return len(y) == len(set(y))

