# put your code here.
def wordcount(file_name):

    #empty list to hold all the words in this file
    all_the_words = []

    #iterate through the file to get all the words
    #and put them in the list
    text = open(file_name)

    for lines in text:
        lines = lines.rstrip()
        word = lines.split(" ")

        #combine all words into one list
        all_the_words.extend(word)

        #testing
        print all_the_words
    


