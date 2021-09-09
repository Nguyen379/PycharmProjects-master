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


# lỗi đánh máy khi type. Em sẽ reverse nó lại xong khi mà chạy 1 string thì nó sẽ replace các cụm này = từ đúng.
#  ví dụ: "nawm" => "năm"

class SentenceCorrector:
    def __init__(self, training_file):
        self.sentences = []
        self.all_words = []
        self.laplaceUnigramCounts = defaultdict(lambda: 0)
        # key:valule la "cap tu (w1, w2)" : "so lan xuat hien (w1,w2)"
        self.laplaceBigramCounts = defaultdict(lambda: 0)
        # key:value la "tu don w1" : "so lan xuat hien w1"
        self.total = 0
        # so luong tat ca tu
        self.reverse_typo = {v: k for k, v in typo.items()}
        # typo goc la {"go dung":"go sai"}, reverse de loi sai la key
        self.tokenize_file(training_file)
        self.train_file()

    def tokenize_file(self, training_file):
        with open(training_file, "r", encoding="UTF-8") as f:
            file = f.readlines()
            for sentence in file:
                sentence = sentence.replace("\n", "")
                sentence_clean = [n.lower() for n in re.split(rf'[^{letters}]+', sentence) if n]
                # doc tung sentence cua training file: lower() viet hoa thanh viet thuong,
                # khi split tat ca nhung ki hieu khong thuoc bang chu cai: "?", "!", "@" se bi xoa
                # 1 cau se dc tokenize thanh cac tu. Moi sentence clean la 1 list chua phan tu la cac tu
                if sentence_clean:
                    # replace("\n", "") o tren vs cai nay de loc het nhung cai xuong dong
                    self.sentences.append(sentence_clean)
        self.all_words = list(chain.from_iterable(self.sentences))
        # chua tat ca tu cua file. from_iterable de unpack va loc tu giong nhau

    def train_file(self):
        for sentence in self.sentences:
            for (w1, w2) in ngrams(sentence, 2, pad_left=True, pad_right=True):
                self.laplaceBigramCounts[(w1, w2)] += 1
                # default dict laplaceBigramCounts se tinh so lan xuat hien cap tu w1, w2
                self.laplaceUnigramCounts[w1] += 1
                # default dict laplaceUnigramCounts se tinh so lan xuat hien tu w1
                self.total += 1
            self.laplaceUnigramCounts[""] += 1
            self.total += 1
            # +1 do pad-right o cuoi la ""
            # self.total + 1 cx la do co pad_right

    def minDistance(self, edit_original_word, candidate_word):
        # levenshtein distance de tim tu giong nhat
        h = len(edit_original_word) + 1
        # so hang
        w = len(candidate_word) + 1
        # so cot
        dp = [[0 for _ in range(w)] for _ in range(h)]
        # tao bang tinh khoang cach: edit distance cua leetcode
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
            # thay loi danh may bang tu dung
            # "nawm" => "năm"
        return original_word

    def candidate_word(self, original_word):
        candidate_words = {}
        edit_original_word = self.edit_original_word(original_word)
        for word in self.all_words:
            candidate_words[word] = self.minDistance(edit_original_word, word)
            # loop tung tu 1 trong all_word de tim tu giong nhat
        list_candidate_words = [k for (k, v) in sorted(candidate_words.items(), key=lambda x: x[1],
                                                       reverse=True) if v == 1]
        # list_candidate_words chua cac candidate word
        # candidate_word la word co minDistance vs original word == 1 (rat giong nha)
        list_candidate_words.append(edit_original_word)
        # them ca original word vao list de ti nua generate all possible sentences
        return list_candidate_words, len(list_candidate_words)
        # return ca len(list_candidate_word) de tinh xac suat cac tu

    def candidate_sentence(self, old_sentence):
        candidate_sentences = []
        words_count = {}
        for word in old_sentence:
            candidate_sentences.append(self.candidate_word(word)[0])
            words_count[word] = self.candidate_word(word)[1]
            # words_count la dictionary chua cap key:value la original_word:len(list_candidate_words)
        candidate_sentences = list(product(*candidate_sentences))
        # generate all possible sentences
        return candidate_sentences, words_count

    # noisy channel model co 2 phan: P(X) = P(X|W) x P(W)
    # moi method se tinh 1 cai r nhan lai vs nhau
    # vi nhan ra so rat nho nen se dung log(xac suat) cho de nhin. Log cang lon => sac xuat cang lon

    def correction_score(self, words_count, old_sentence, candidate_sentence):
        # old_sentence va candidate_sentence deu co dang la 1 list, moi phan tu cua list la 1 word
        # P(X|W): original_word co xac suat la 0.95, moi candidate_word co xac suat la 0.05/len(lost_candidate_words)
        # diem xac suat P(X|W) cua moi candidate_sentence se duoc tinh bang cach nhan xac suat tung tu 1 vs nhau
        score = 1
        for n in range(len(candidate_sentence)):
            # chay tung word trong sentence:
            if candidate_sentence[n] in words_count:
                # words_count: dictionary cap key:value la original_word: len(list_candidate_words)
                # neu nhu tu nay cua candidate sentence cung xuat hien trong old_sentence
                score *= 0.95
            else:
                score *= 0.05/(words_count[old_sentence[n]]-1)
                # tru 1 la tru di original_word: xac suat candidate_word = 0.05 chia deu ra
        return math.log(score)
        # tra diem log r cong vao cho de nhin

    def score(self, candidate_sentence):
        # P(W)
        # tinh bang stupid backoff language model.
        # 1 tu duoc tinh theo 2 cach laplaceBigramCounts: xuat hien theo cap va laplalceUnigramCounts: xuat hien don le
        # laplace smoothing duoc su dung de giai quyet truong hop tu day khong xuat hien trong ca 2 default dict o tren
        score = 1
        for n in range(len(candidate_sentence) - 1):
            if self.laplaceBigramCounts[(candidate_sentence[n], candidate_sentence[n+1])] > 0:
                # score = bigram/unigram
                # tinh nhu the nay no se tang weight cho nhung cap tu hay xuat hien vs nhau
                score *= self.laplaceBigramCounts[(candidate_sentence[n], candidate_sentence[n+1])]
                score /= self.laplaceUnigramCounts[candidate_sentence[n]]
            else:
                # score = unigram/all words
                score *= (self.laplaceUnigramCounts[candidate_sentence[n+1]] + 1) * 0.4
                # 0.4: regularization constant
                # neu candidate_sentence[n] khong ton tai thi thay the no = candidate_sentence[n+1]
                # khi day laplaceUnigramCounts se co them 1 truong hop candidate_sentence[n+1] nen se + 1 roi moi * 0.4
                score /= self.total + len(self.laplaceUnigramCounts)
        return math.log(score)

    def return_best_sentence(self, old_sentence):
        # noisy channel model co 2 phan: P(X) = P(X|W) x P(W)
        # moi method se tinh 1 cai r nhan lai vs nhau
        # vi nhan ra so rat nho nen se dung log(xac suat) cho de nhin. Log cang lon => sac xuat cang lon
        bestScore = float('-inf')
        bestSentence = []
        old_sentence = [word.lower() for word in old_sentence.split()]
        # bien thanh list cac tu
        candidate_sentences, words_count = self.candidate_sentence(old_sentence)
        for candidate_sentence in candidate_sentences:
            candidate_sentence = list(candidate_sentence)
            # convert thanh dang list cac tu
            score = self.correction_score(words_count, old_sentence, candidate_sentence)
            candidate_sentence.append("")
            candidate_sentence.insert(0, "")
            score += self.score(candidate_sentence)
            # them "" o dau va cuoi cau vi ngrams có pad_left, pad_right
            if score >= bestScore:
                bestScore = score
                bestSentence = candidate_sentence
                # diem cao nhat la sac xuat cao nhat
        bestSentence = " ".join(bestSentence[1:-1])
        # bo pad_left, pad_right
        return bestSentence, bestScore


sc = SentenceCorrector("test.txt")
print(sc.return_best_sentence('chất nượng cuộc xống'))
