import collections
import itertools
import math
import re

import enchant
import nltk.data


class Sentence_Corrector:
    def __init__(self, training_file):
        self.laplaceUnigramCounts = collections.defaultdict(lambda: 0)
        self.laplaceBigramCounts = collections.defaultdict(lambda: 0)
        self.total = 0
        self.sentences = []
        self.importantKeywords = set()
        self.d = enchant.Dict("en_US")
        self.tokenize_file(training_file)
        self.train()

    def tokenize_file(self, file):
        # """
        #   Read the file, tokenize and build a list of sentences
        # """
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        f = open(file)
        content = f.read()
        for sentence in tokenizer.tokenize(content):
            sentence_clean = [i.lower() for i in re.split('[^a-zA-Z]+', sentence) if i]
            self.sentences.append(sentence_clean)

    def train(self):
        # """
        #   Train unigram and bigram
        # """
        for sentence in self.sentences:
            sentence.insert(0, '<s>')
            sentence.append('</s>')
            for i in range(len(sentence) - 1):
                token1 = sentence[i]
                token2 = sentence[i + 1]
                self.laplaceUnigramCounts[token1] += 1
                self.laplaceBigramCounts[(token1, token2)] += 1
                self.total += 1
            self.total += 1
            self.laplaceUnigramCounts[sentence[-1]] += 1

    def candidate_word(self, word):
        # """
        # Generate similar word for a given word
        # """
        suggests = []
        for candidate in self.importantKeywords:
            if candidate.startswith(word):
                suggests.append(candidate)
        suggests.append(word)

        if len(suggests) == 1:
            suggests = self.d.suggest(word)
            suggests = [suggest.lower() for suggest in suggests][:4]
            suggests.append(word)
            suggests = list(set(suggests))

        return suggests, len(suggests)

    def candidate_sentence(self, sentence):
        # """ Takes one sentence, and return all the possible sentences, and also return a dictionary of word :
        # suggested number of words """
        candidate_sentences = []
        words_count = {}
        for word in sentence:
            candidate_sentences.append(self.candidate_word(word)[0])
            words_count[word] = self.candidate_word(word)[1]

        candidate_sentences = list(itertools.product(*candidate_sentences))
        return candidate_sentences, words_count

    def correction_score(self, words_count, old_sentence, new_sentence):
        # """ Take a old sentence and a new sentence, for each words in the new sentence, if it's same as the original
        # sentence, assign 0.95 prob If it's not same as original sentence, give 0.05 / (count(similarword) - 1) """
        score = 1
        for i in range(len(new_sentence)):
            if new_sentence[i] in words_count:
                score *= 0.95
            else:
                score *= (0.05 / (words_count[old_sentence[i]] - 1))
        return math.log(score)

    def score(self, sentence):
        # """
        #     Takes a list of strings as argument and returns the log-probability of the
        #     sentence using the stupid backoff language model.
        #     Use laplace smoothing to avoid new words with 0 probability
        # """
        score = 0.0
        for i in range(len(sentence) - 1):
            if self.laplaceBigramCounts[(sentence[i], sentence[i + 1])] > 0:
                score += math.log(self.laplaceBigramCounts[(sentence[i], sentence[i + 1])])
                score -= math.log(self.laplaceUnigramCounts[sentence[i]])
            else:
                score += (math.log(self.laplaceUnigramCounts[sentence[i + 1]] + 1) + math.log(0.4))
                score -= math.log(self.total + len(self.laplaceUnigramCounts))
        return score

    def return_best_sentence(self, old_sentence):
        # """
        #   Generate all candiate sentences and
        #   Calculate the prob of each one and return the one with highest probability
        #   Probability involves two part 1. correct probability and 2. language model prob
        #   correct prob : p(c | w)
        #   language model prob : use stupid backoff algorithm
        # """
        bestScore = float('-inf')
        bestSentence = []
        old_sentence = [word.lower() for word in old_sentence.split()]
        sentences, word_count = self.candidate_sentence(old_sentence)
        for new_sentence in sentences:
            new_sentence = list(new_sentence)
            score = self.correction_score(word_count, new_sentence, old_sentence)
            new_sentence.insert(0, '<s>')
            new_sentence.append('</s>')
            score += self.score(new_sentence)
            if score >= bestScore:
                bestScore = score
                bestSentence = new_sentence
        bestSentence = ' '.join(bestSentence[1:-1])
        return bestSentence, bestScore


corrector = Sentence_Corrector('big.txt')
print(corrector.return_best_sentence('this is wron spallin word'))
print(corrector.return_best_sentence('aoccdrning to a resarch at cmabridge university'))
corrector.return_best_sentence('it does not mttaer in waht oredr the ltteers')
corrector.return_best_sentence('the olny important tihng is taht')
corrector.return_best_sentence('Can they leav him my messages')
corrector.return_best_sentence('This used to belong to thew queen')
