def translate(text):
    words = text.split()
    result = []
    
    for word in words:
        if word[0] in "aeiou" or word[0:2] in ["xr", "yt"]:
            result.append(word + "ay")
            
        elif word[0:2] == "qu":
            result.append(word[2:] + word[:2] + "ay")
        elif len(word) >= 3 and word[1:3] == "qu":
            result.append(word[3:] + word[:3] + "ay")
            
        elif len(word) >= 2 and word[1] == "y":
            result.append(word[1:] + word[:1] + "ay")
        elif len(word) >= 3 and word[2] == "y":
            result.append(word[2:] + word[:2] + "ay")
            
        elif len(word) >= 2 and word[1] in "aeiou":
            result.append(word[1:] + word[:1] + "ay")
        elif len(word) >= 3 and word[2] in "aeiou":
            result.append(word[2:] + word[:2] + "ay")
        elif len(word) >= 4 and word[3] in "aeiou":
            result.append(word[3:] + word[:3] + "ay")
            
        else:
            result.append(word + "ay")
            
    return " ".join(result)

