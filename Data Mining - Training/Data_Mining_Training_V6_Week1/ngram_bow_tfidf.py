# n-gram: sequece of n words
# Bow (Bag of words): turn into a dictionary with the keys are the words and the values are the words' frequencies
# bow has no order and grammar. Because the highest frequency words are often meaningless like "the", "a", we can
# weight a term by the inverse of document frequency, or Tf-idf (term frequency - inverse document frequency)
# tf = số lân 1 từ xuất hiện, idf = log((tổng số văn bản)/(số văn bản xuất hiện từ đang xét ở tf)), tf-idf = tf x idf
# idf có tác dụng lọc những từ thông dụng quá mức Sử dụng log trong idf để "dampen" ảnh hưởng khi số văn bản quá lớn.
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import movie_reviews
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import ClassifierI
from statistics import mode
import random
import pickle

"Separate into sentences, words"
text = '''Hi Mr. Smith, how are you doing today? The weather is great and Python is awesome.'''
print(sent_tokenize(text))
print(word_tokenize(text))
# catch "." in "Mr." is part of a word not a punctuation

"Using stopwords"
sw = stopwords.words("english")
# print(sw)
filtered_sent = [n for n in word_tokenize(text) if n not in sw]
print(filtered_sent)

"Stemming"
ps = PorterStemmer()
words = ["program", "programs", "programer", "programing", "programers"]
for w in words:
    print(w, " : ", ps.stem(w))

"Speech tagging, Chunking, Chinking"
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
# read the raw, original file
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# train PunktSentenceTokenizer with data from train_text and then use PST on sample_text to tokenize it into sentences.
tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content_RegexpParser():
    try:
        for n in tokenized:
            words = nltk.word_tokenize(n)
            tagged = nltk.pos_tag(words)
            # chunkGram = r'''Chunk: {<RB.?>*<VB.?>*<NNP>*<NN>?}'''
            chunkGram = r'''Chunk0: {<.*>+}
                                }<VB.?|IN|DT|TO>+{'''
            # {} chunking lấy, }{ chinking không lấy
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()
    except Exception as e:
        print(str(e))


print(process_content_RegexpParser())


def process_content_ne_chunk():
    try:
        for n in tokenized:
            words = nltk.word_tokenize(n)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged)
            namedEnt.draw()
    except Exception as e:
        print(str(e))


print(process_content_ne_chunk())

'Lemmatizer'

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("run", pos="a"))
# pos default = noun


"Word Net"

syns = wordnet.synsets("program")
print(syns)
# synsets get all sets of synonyms in relation to "program"
print(syns[0])
# syns[0] is the first synset that contain lemmas of synonyms in relation to syns[0]
print(syns[0].lemmas())
# .lemmas get synonyms of "plan"
# the first synonym of plan is "plan"
print(syns[0].lemmas()[0].name())
# .name() get the string of 1st synonym
print(syns[0].definition())
print(syns[0].examples())

synonyms = []
antonyms = []
for g_syn in wordnet.synsets("good"):
    for l in g_syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            # antonym return a list with single lemma containing antonym
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

w1 = wordnet.synset("ship.n.01")
# .synset targets a particular synset instead of .synsets which targets all relatable synsets
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))
# get similarity in meaning
w3 = wordnet.synset("car.n.01")
w4 = wordnet.synset("cat.n.01")
print(w1.wup_similarity(w3))
print(w1.wup_similarity(w4))

"Text classification"
# Movie reviews contain 2 category negative and positive each containing numerous txt files
documents = []
for category in movie_reviews.categories():
    # get the categories of movie_reviews.
    # each category has numerous fileids.txt files
    for fileid in movie_reviews.fileids(category):
        # get all the words in that fileid and add it in with the category for classification
        documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)
# print(documents)

"Frequency Distribution"
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
# get a list of all words that appear in all files
all_words2 = nltk.FreqDist(all_words)
# convert into a dictionary of frequency
word_features = list(all_words2.keys())[:3000]


# get the 3000 least common words in all words
# all_words2 keys are arranged from least to most common

# print(all_words2["stupid"])
# get a particular word


def find_features(document):
    features = {}
    words = set(document)
    for word in word_features:
        features[word] = (word in words)
        # equal to True or False
    return features


# print(find_features(movie_reviews.words("neg/cv000_29416.txt")))
# get feature words of a particular file

"Feature words"

featuresets = []
for (all_words, category) in documents:
    featuresets.append((find_features(all_words), category))
# print(featuresets)
# get the features words of each file of each category

"Training and testing with NaiveBayesClassfier"

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

classfier = nltk.NaiveBayesClassifier.train(training_set)
# print(nltk.classify.accuracy(classfier, testing_set))
# classfier.show_most_informative_features(15)

# save_classfier = open("naivebayes.pickle", "wb")
# pickle.dump(classfier, save_classfier)
# save_classfier.close()
# save file uing pickle

"Saving model with pickle"
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
# print(nltk.classify.accuracy(classifier, testing_set))

"MultinomialNB, GaussianNB, BernoulliNB, NB= Naivebayes"

'''
1.Gaussian NB: should be used for features in decimal form. GNB assumes features to follow a normal distribution.
2.MultiNomial NB: should be used for the features with discrete values like word count 1,2,3...
3.Bernoulli NB: should be used for features with binary or boolean values like True/False or 0/1.
'''
MNB_classifier = SklearnClassifier(MultinomialNB())
# MultinomialNB() now inherits sklearnclassifier's methods such as .train
MNB_classifier.train(training_set)
# print(nltk.classify.accuracy(MNB_classifier, testing_set))

# GNB_classifier = SklearnClassifier(GaussianNB())
# GNB_classifier.train(training_set)
# print(nltk.classify.accuracy(GNB_classifier, testing_set))
BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
# print(nltk.classify.accuracy(BNB_classifier, testing_set))

"LogisticRegression, SGDClassifier, SVC"


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self.classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self.classifiers:
            v = c.classify(features)
            # each classifier classifies features (feature words) based on given category
            votes.append(v)
        # votes have different results, mode returns the most voted result
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self.classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


# linear regression is for predicting continuous output, logistic regression is for classification, categorization
LR_classifier = SklearnClassifier(LogisticRegression())
LR_classifier.train(training_set)
# print(nltk.classify.accuracy(LR_classifier, testing_set))

SGDCC_classifier = SklearnClassifier(SGDClassifier())
SGDCC_classifier.train(training_set)
# print(nltk.classify.accuracy(SGDCC_classifier, testing_set))

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
# print(nltk.classify.accuracy(SVC_classifier, testing_set))

Linear_SVC_classifier = SklearnClassifier(LinearSVC())
Linear_SVC_classifier.train(training_set)
# print(nltk.classify.accuracy(Linear_SVC_classifier, testing_set))

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
# print(nltk.classify.accuracy(NuSVC_classifier, testing_set))

"Using different classifiers to vote and determine the optimal accuracy"
voted_classifier = VoteClassifier(NuSVC_classifier, Linear_SVC_classifier, SVC_classifier, SGDCC_classifier,
                                  LR_classifier, MNB_classifier, BNB_classifier)

# print(nltk.classify.accuracy(voted_classifier, testing_set))
#
# print(voted_classifier.classify(testing_set[0][0]), "   ", voted_classifier.confidence(testing_set[0][0]) * 100)
# print(testing_set[0][0])
# print(voted_classifier.classify(testing_set[1][0]), "   ", voted_classifier.confidence(testing_set[1][0]) * 100)
# print(testing_set[1][0])
# print(voted_classifier.classify(testing_set[2][0]), "   ", voted_classifier.confidence(testing_set[2][0]) * 100)
# print(testing_set[2][0])
# print(voted_classifier.classify(testing_set[3][0]), "   ", voted_classifier.confidence(testing_set[3][0]) * 100)
# print(testing_set[3][0])
# print(voted_classifier.classify(testing_set[4][0]), "   ", voted_classifier.confidence(testing_set[4][0]) * 100)
# print(testing_set[4][0])
# print(voted_classifier.classify(testing_set[5][0]), "   ", voted_classifier.confidence(testing_set[5][0]) * 100)
# print(testing_set[5][0])
