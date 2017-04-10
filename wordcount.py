# put your code here.


#putting it all in one function
#will figure out if they can be broken later

def get_word_list(file_name):
    """Separates words and creates master list of all the words

    Given a file of text, iterates through that file and puts all
    the words into a list.
    """

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

    #create an empty dictionary to hold the words
    word_count = {}

    #iterate though the list to count number of occurances
    for word in all_the_words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

    #testing
    print word_count


