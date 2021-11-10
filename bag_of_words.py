# This is the simplest way to encode our data.
#  This is the technique where each word in a sentence is encoded with an integer and thrown into a collection that
#  does not maintain the order of the words but does keep track of the frequency.

vocab = {}  # maps word to integer representing it
word_encoding = 1


def bag_of_words(text):
    global word_encoding

    words = text.lower().split(" ")  # create a list of all of the words in the text
    bag = {}  # stores all of the encodings and their frequency

    for word in words:
        if word in vocab:
            encoding = vocab[word]  # get encoding from vocab
        else:
            vocab[word] = word_encoding
            encoding = word_encoding
            word_encoding += 1

        if encoding in bag:
            bag[encoding] += 1

        else:
            bag[encoding] = 1
    return bag


text = input('Enter words for encryption: ')
bag = bag_of_words(text)
print(bag)
print(vocab)
