from nltk.corpus import reuters
from nltk import ngrams
from collections import defaultdict

# Create a placeholder for model
# model = defaultdict(lambda: defaultdict(lambda: 0))
model = defaultdict(lambda: defaultdict(int))
# nested dictionary
for sentence in reuters.sents():
    for (w1, w2, w3) in ngrams(sentence, 3, pad_left=True, pad_right=True):
        model[w1, w2][w3] += 1
        # count the frequency of each word that follows w1_w2

for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    # each key leads to a dict: model[w1_w2].values() get the the values of all keys of nested dict model[w1_w2]
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count
    # count the probability of each word that follows w1_w2

print(model["today", "the"])
