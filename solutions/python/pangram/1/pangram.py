def cleantext(text):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    clean_text = ""

    for char in text:
        if char not in punctuation:
            clean_text += char

    return clean_text
def is_pangram(sentence):
    x = ' '.join(cleantext(sentence.lower()))
    y = x.split()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabets:
        if char not in y:
            return False
    return True

