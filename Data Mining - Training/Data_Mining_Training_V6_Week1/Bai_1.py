def check_word(word):
    for num in range(1, len(word) + 1):
        if word[:num] in wordDict:
            if len(word) == len(s):
                sentences.append("separator")
                # num = 3 cat duoc word[:num]=="cat", word[num:]=="sanddog" cat tiep duoc "sand" va "dog"
                # num = 4 cat duoc "cats", "anddog" cat tiep duoc "and" va "dog"
                # vi day la 2 truong hop rieng (s nguyen ven chua bi cat) nen them separator
                # de split ra thanh 2 cau
            sentences.append(word[:num])
            # tu duoc cat them vao list sentences
            check_word(word[num:])
            # sau khi tim duoc tu cat thi cho ve con lai "sanddog" vao loop de tim tiepp


if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    sentences = []
    output = []
    check_word(s)
    string_sentences = " ".join(sentences[1:]).split("separator")
    # tach ra thanh cac cau boi vi num = 3 va num = 4 cat khac nhau
    string_sentences = map(lambda x: x.strip(), string_sentences)
    # cac cau bi thua dau spacebar hay tab thi strip di cho de nhin
    for n in string_sentences:
        if n.replace(" ", "") == s:
            output.append(n)
    # cho vao output ket qua r print ra
    print(output)

