def rotate(text, key):
    dictionary = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    caps = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()

    # FIX 1: Removed .lower() and .split() so we don't lose caps or spaces.
    # Treating the string directly as an iterable keeps every character intact.
    list = text 

    output = ""
    for i in list:
        if i.isupper():
            for x in caps:
                if x == i:
                    index = caps.index(x)
                    index = index + key
                    # FIX 2: Changed to >= 26 and used 'while' in case the key is larger than 26
                    while index >= 26: 
                        index = index - 26
                    output += caps[index]
        # FIX 3: Changed 'else' to 'elif i.islower()' to specifically target lowercase letters
        elif i.islower():
            for x in dictionary:
                if x == i:
                    index = dictionary.index(x)
                    index = index + key
                    while index >= 26:
                        index = index - 26
                    output += dictionary[index]
        # FIX 4: Added a final 'else' to append spaces and punctuation as-is
        else:
            output += i 
            
    return output

