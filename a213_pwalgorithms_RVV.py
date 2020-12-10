# Module pwalgorithms

# get words from password dictionary file

completePhrase = ""

def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, ommitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def schoolPass(password, num):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w1 in words:

    for w2 in words:
      phrase = w1 + w2
      completePhrase = w1 + num + w2
      guesses += 1
      
      if (phrase == password):
        print("complete password: ", completePhrase)
        return True, guesses
        
  return False, guesses

def two_word(password, num):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w1 in words:

    for w2 in words:
      phrase = w1 + w2
      guesses += 1
      
      if (phrase == password):
        return True, guesses
        
  return False, guesses
