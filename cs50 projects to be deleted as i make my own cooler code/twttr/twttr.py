def main():
    tweet = input("Input: ")
    consonants =  shorten(tweet)
    print(consonants)


def shorten(word):
    #list of vowels upper and lowercase
    #I didn't force the imput to lowercase as usual becaus then the output would be lowercase
    #char = 'aeiouAEIOU' works and is faster to type, but I think this is more friendly to later additions
    char = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',]
    no_vowel = []
    for letter in word:
        #checks if each lette is a vowel
        if letter in char:
        #passes if it is, leaving it out of the output
            pass
        #if it isn't a vowel, it adds it to the list "no_vowel"
        else:
            no_vowel.append(letter)
    #outside of the for loop, it joins the list into a string with no spaces between elements
    result = "".join(no_vowel)
    return result

if __name__ == '__main__':
    main()
