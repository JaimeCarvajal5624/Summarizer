import spacy

nlp = spacy.load("en_core_web_sm")

# Extractive summary by word count
testText = "The idea of this text is to be summarized. A sumarized text retains most of the important information. I " \
           "believe this text will be well sumarized. My name is Jaime Carvajal and I enjoy natural language " \
           "processing. I really like dogs and spending time with them. It is very important to understand how a " \
           "summarizer works. This is an extra sentence. "
a = input("Write or paste the text you want summarized. Write nothig to use the premade example.\n")
if a != "":
    testText = a
# Tokenization of example
doc = nlp(testText)

# Creation of a dictionary
wordDictionary = {}

# Loop that gives each sentence a weight
for word in doc:
    word = word.text.lower()
    if word in wordDictionary:
        wordDictionary[word] += 1
    else:
        wordDictionary[word] = 1

# Create a list of tuples (Sentence text, score, index)
sents = []

# Score sentences
sentScore = 0
for index, sent in enumerate(doc.sents):
    for word in sent:
        word = word.text.lower()
        sentScore += wordDictionary[word]
    sents.append((sent.text.replace("\n", " "), sentScore / len(sent), index))

# Finding most important sentences for the text summarizer
# Sort sentence by word occurrences
sents = sorted(sents, key=lambda x: -x[-1])
# Return top 3 words
sents = sorted(sents[:3], key=lambda x: x[2])

# Returning the summary
summaryText = ""
for sent in sents:
    summaryText += sent[0] + " "

print(summaryText)
