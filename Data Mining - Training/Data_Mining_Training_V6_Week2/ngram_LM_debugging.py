import re
from itertools import chain, product
import math
from collections import defaultdict
from nltk import ngrams

letters = "abcdefghijklmnopqrstuvwxyzáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđABCDEFGHIJKL\
MNOPQRSTUVWXYZÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÉÈẺẼẸÊẾỀỂỄỆÚÙỦŨỤƯỨỪỬỮỰÍÌỈĨỊÝỲỶỸỴĐ"
# bang chu cai tieng viet
typo = {"ă": "aw", "â": "aa", "á": "as", "à": "af", "ả": "ar", "ã": "ax", "ạ": "aj", "ắ": "aws", "ổ": "oor", "ỗ": "oox",
        "ộ": "ooj", "ơ": "ow",
        "ằ": "awf", "ẳ": "awr", "ẵ": "awx", "ặ": "awj", "ó": "os", "ò": "of", "ỏ": "or", "õ": "ox", "ọ": "oj",
        "ô": "oo", "ố": "oos", "ồ": "oof",
        "ớ": "ows", "ờ": "owf", "ở": "owr", "ỡ": "owx", "ợ": "owj", "é": "es", "è": "ef", "ẻ": "er", "ẽ": "ex",
        "ẹ": "ej", "ê": "ee", "ế": "ees", "ề": "eef",
        "ể": "eer", "ễ": "eex", "ệ": "eej", "ú": "us", "ù": "uf", "ủ": "ur", "ũ": "ux", "ụ": "uj", "ư": "uw",
        "ứ": "uws", "ừ": "uwf", "ử": "uwr", "ữ": "uwx",
        "ự": "uwj", "í": "is", "ì": "if", "ỉ": "ir", "ị": "ij", "ĩ": "ix", "ý": "ys", "ỳ": "yf", "ỷ": "yr", "ỵ": "yj",
        "đ": "dd",
        "Ă": "Aw", "Â": "Aa", "Á": "As", "À": "Af", "Ả": "Ar", "Ã": "Ax", "Ạ": "Aj", "Ắ": "Aws", "Ổ": "Oor", "Ỗ": "Oox",
        "Ộ": "Ooj", "Ơ": "Ow",
        "Ằ": "AWF", "Ẳ": "Awr", "Ẵ": "Awx", "Ặ": "Awj", "Ó": "Os", "Ò": "Of", "Ỏ": "Or", "Õ": "Ox", "Ọ": "Oj",
        "Ô": "Oo", "Ố": "Oos", "Ồ": "Oof",
        "Ớ": "Ows", "Ờ": "Owf", "Ở": "Owr", "Ỡ": "Owx", "Ợ": "Owj", "É": "Es", "È": "Ef", "Ẻ": "Er", "Ẽ": "Ex",
        "Ẹ": "Ej", "Ê": "Ee", "Ế": "Ees", "Ề": "Eef",
        "Ể": "Eer", "Ễ": "Eex", "Ệ": "Eej", "Ú": "Us", "Ù": "Uf", "Ủ": "Ur", "Ũ": "Ux", "Ụ": "Uj", "Ư": "Uw",
        "Ứ": "Uws", "Ừ": "Uwf", "Ử": "Uwr", "Ữ": "Uwx",
        "Ự": "Uwj", "Í": "Is", "Ì": "If", "Ỉ": "Ir", "Ị": "Ij", "Ĩ": "Ix", "Ý": "Ys", "Ỳ": "Yf", "Ỷ": "Yr", "Ỵ": "Yj",
        "Đ": "Dd"}


# loi danh may sai. Cái này em sẽ reverse để tìm lỗi sai

class SentenceCorrector:
    def __init__(self, training_file):
        self.sentences = []
        self.all_words = []
        self.laplaceUnigramCounts = defaultdict(lambda: 0)
        self.laplaceBigramCounts = defaultdict(lambda: 0)
        self.total = 0
        self.reverse_typo = {v: k for k, v in typo.items()}
        # typo goc la {"go dung":"go sai"}, reverse de loi sai la key
        self.tokenize_file(training_file)
        self.train_file()

    def tokenize_file(self, training_file):
        with open(training_file, "r", encoding='UTF-8') as f:
            file = f.readlines()
            for sentence in file:
                sentence_clean = [n.lower() for n in re.split(rf'[^{letters}]+', sentence) if n]
                self.sentences.append(sentence_clean)
        self.all_words = list(chain.from_iterable(self.sentences))

    def train_file(self):
        for sentence in self.sentences:
            for (w1, w2) in ngrams(sentence, 2, pad_left=True, pad_right=True):
                self.laplaceBigramCounts[(w1, w2)] += 1
                self.laplaceUnigramCounts[w1] += 1
                self.total += 1
            self.laplaceUnigramCounts[""] += 1
            self.total += 1
            # +1 cho cái pad right ở cuối cùng vì unigram w1 ko chạy đến giá trị cuối cùng

    def minDistance(self, edit_original_word, candidate_word):
        h = len(edit_original_word) + 1
        # so hang
        w = len(candidate_word) + 1
        # so cot
        dp = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            dp[i][0] = i
        for j in range(w):
            dp[0][j] = j
        for i in range(1, h):
            for j in range(1, w):
                insertion = dp[i][j - 1] + 1
                deletion = dp[i - 1][j] + 1
                replacement = dp[i - 1][j - 1] + (edit_original_word[i - 1] != candidate_word[j - 1])
                dp[i][j] = min(deletion, insertion, replacement)
        return dp[-1][-1]

    def edit_original_word(self, original_word):
        for fault in self.reverse_typo:
            if fault in original_word:
                original_word = original_word.replace(fault, self.reverse_typo[fault])
        return original_word

    def candidate_word(self, original_word):
        candidate_words = {}
        edit_original_word = self.edit_original_word(original_word)
        for word in self.all_words:
            candidate_words[word] = self.minDistance(edit_original_word, word)
        list_candidate_words = [k for (k, v) in sorted(candidate_words.items(), key=lambda x: x[1],
                                                       reverse=True) if v == 1]
        list_candidate_words.append(edit_original_word)
        # chi lay tu co minimum edit distance == 1
        return list_candidate_words, len(list_candidate_words)

    def candidate_sentence(self, old_sentence):
        candidate_sentences = []
        words_count = {}
        # words_count = {}
        for word in old_sentence:
            candidate_sentences.append(self.candidate_word(word)[0])
            words_count[word] = self.candidate_word(word)[1]
            # dictionary of word - number of respective candidate_words pairs
        candidate_sentences = list(product(*candidate_sentences))
        return candidate_sentences, words_count

    def correction_score(self, words_count, old_sentence, candidate_sentence):
        # P(X|W)
        score = 1
        for n in range(len(candidate_sentence)):
            # chay tung tu 1 cua candidate sentence: xac xuat viet tu day == tu cua cau goc la: 0.95
            # xac suat viet sai la 0.05 chia deu cho cac truong hop con lai
            if candidate_sentence[n] in words_count:
                score *= 0.95
            else:
                score *= 0.05 / (words_count[old_sentence[n]] - 1)
                # minus 1 which is the original word
        return math.log(score)

    def score(self, candidate_sentence):
        # P(W)
        #     Takes a list of strings as argument and returns the log-probability of the
        #     sentence using the stupid backoff language model.
        #     Use laplace smoothing to avoid new words with 0 probability
        score = 0.0
        for n in range(len(candidate_sentence) - 1):
            if self.laplaceBigramCounts[(candidate_sentence[n], candidate_sentence[n + 1])] > 0:
                score += math.log(self.laplaceBigramCounts[(candidate_sentence[n], candidate_sentence[n + 1])])
                score -= math.log(self.laplaceUnigramCounts[candidate_sentence[n]])
            else:
                # if word isn't found in training data, +1 to all words
                score += (math.log(self.laplaceUnigramCounts[candidate_sentence[n + 1]] + 1) + math.log(0.4))
                # log(a x 0.4) = log(a) + log(0.4)
                score -= math.log(self.total + len(self.laplaceUnigramCounts))
        return score

    def return_best_sentence(self, old_sentence):
        #   Generate all candiate sentences and
        #   Calculate the prob of each one and return the one with highest probability
        #   Probability involves two part 1. correct probability and 2. language model prob
        #   language model prob : use stupid backoff algorithm
        bestScore = float('-inf')
        bestSentence = []
        old_sentence = [word.lower() for word in old_sentence.split()]
        candidate_sentences, word_count = self.candidate_sentence(old_sentence)
        for candidate_sentence in candidate_sentences:
            candidate_sentence = list(candidate_sentence)
            score_pxw = self.correction_score(word_count, old_sentence, candidate_sentence)
            candidate_sentence.append("")
            candidate_sentence.insert(0, "")
            score_px = self.score(candidate_sentence)
            candidate_sentence = ' '.join(candidate_sentence[1:-1])
            bestSentence.append((candidate_sentence, score_pxw, score_px))
        return sorted(bestSentence, key=lambda x: x[1]+x[2])[-5:]


sc = SentenceCorrector('test.txt')
print("chất nượng cuộc xống")
for n in sc.return_best_sentence('chất nượng cuộc xống'):
    print(n)

# loi o old_sentence vs split_old sentence trong test 2

# [('đào ngọc dung', -6.4118211062912165),
# ('đào ngọc dẫn', -6.4118211062912165),
# ('đào ngọc dân', -6.4118211062912165),
# ('đào ngọc duy', -6.4118211062912165),
# ('đào ngọc dun', -6.4118211062912165)]

