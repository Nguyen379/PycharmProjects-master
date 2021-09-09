import re
from keras.preprocessing import sequence
from sklearn.datasets import load_files
import pickle

letters = "abcdefghijklmnopqrstuvwxyzáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđABCDEFGHIJKL\
MNOPQRSTUVWXYZÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÉÈẺẼẸÊẾỀỂỄỆÚÙỦŨỤƯỨỪỬỮỰÍÌỈĨỊÝỲỶỸỴĐ"
# Doc file train, test
reviews_train = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training"
                           r"\Data_Mining_Training_V6_Week2\new train", encoding="utf16")
reviews_test = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training"
                          r"\Data_Mining_Training_V6_Week2\new test", encoding="utf16")
train_files, train_categories = reviews_train.data, reviews_train.target
test_files, test_categories = reviews_test.data, reviews_test.target
print(len(train_files))
print(len(test_files))

# Mục đích: lọc chỉ lấy 1/10 những từ phổ biến nhất còn lại thì bỏ không dùng
# combined_files là kết hợp file train và test. Dùng file này để đếm số từ
combined_files = train_files.copy()
combined_files.extend(test_files)
dict_all_words = {}
new_combined_files = []
for file in combined_files:

    file = file.lower()
    file = re.sub(rf'[^{letters}]+', " ", file)
    file = file.split(" ")
    file = [word for word in file if word]
    # chia 1 câu thành 1 list chứa những từ đơn: "tôi tên là A" => ["tôi", "tên", "là", "A"]
    new_combined_files.append(file)

for file in new_combined_files:
    # đếm số từ: nếu từ nào không có trong dict thì thêm vào, có rồi thì +1
    for word in file:
        if word not in dict_all_words:
            dict_all_words[word] = 1
        else:
            dict_all_words[word] += 1

# lọc lấy 1/10 số từ phổ biến nhất trong tổng số từ làm feature_words.
max_features = len(dict_all_words.items()) // 7
print(max_features) # 8178

sorted_dict_words = sorted(dict_all_words.items(), key=lambda x: x[1])[-max_features:]
# dict có cặp key:value là feature_word:index.
dict_best_words = {k: sorted_dict_words.index((k, v)) for (k, v) in sorted_dict_words}
edited_combined_file = []
for file in new_combined_files:
    # tạo câu mới: những từ trong câu cũ được thay bằng index (thể hiện mức độ phổ biến).
    # Những từ không có trong dict thì bỏ qua
    # cho câu mới này vào 1 new_file r thêm tất cả vào edited_combined_file => chứa tất cả các câu
    new_file = []
    for word in file:
        if word in dict_best_words:
            new_file.append(dict_best_words[word])
    edited_combined_file.append(new_file)


max_len = 0
for file in edited_combined_file:
    if len(file) > max_len:
        max_len = len(file)

max_review_len = max_len//5
print(max_len)
# 2293
edited_combined_file = sequence.pad_sequences(edited_combined_file, maxlen=max_review_len)
print(edited_combined_file.shape)
# (26451, 2293)

with open("X_combined_c.pickle", "wb") as p:
    pickle.dump(edited_combined_file, p)
with open("y_train_c.pickle", "wb") as p:
    pickle.dump(train_categories, p)
with open("y_test_c.pickle", "wb") as p:
    pickle.dump(test_categories, p)

