from sklearn.linear_model import SGDClassifier
import re
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
letters = "abcdefghijklmnopqrstuvwxyzáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđABCDEFGHIJKL\
MNOPQRSTUVWXYZÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÉÈẺẼẸÊẾỀỂỄỆÚÙỦŨỤƯỨỪỬỮỰÍÌỈĨỊÝỲỶỸỴĐ"

reviews = load_files(r"E:\PycharmProjects\Data Mining - Training\Data_Mining_Training_V6_Week2"
                     r"\combined_for_cross_validation", encoding="utf16")
files, categories = reviews.data, reviews.target
new_combined_files = []
all_words = []

for file in files:
    file = file.lower()
    file = re.sub(rf'[^{letters}]+', " ", file)
    new_combined_files.append(file)
    file = file.split(" ")
    file = [word for word in file if word]
    all_words.extend(file)

one_quarter = len(set(all_words))//4
print(one_quarter)


"TfidfVectorizer"
vectorizer = TfidfVectorizer(max_features=one_quarter, min_df=10)
files_vectorized = vectorizer.fit_transform(new_combined_files)
files_vectorized = files_vectorized.toarray()
print(files_vectorized.shape)

# pca = PCA().fit(files_vectorized)
# print(pca.explained_variance_ratio_)
# plt.plot(np.cumsum(pca.explained_variance_ratio_))
# plt.xlabel('number of components')
# plt.ylabel('cumulative explained variance')
# plt.show()

pca = PCA(n_components=6000)
files_vectorized = pca.fit_transform(files_vectorized)

files_train, files_test, categories_train, categories_test = train_test_split(files_vectorized, categories)

sgdc_clf = SGDClassifier()
sgdc_clf.fit(files_train, categories_train)
print(sgdc_clf.score(files_test, categories_test))

lsvc_clf = LinearSVC()
lsvc_clf.fit(files_train, categories_train)
print(lsvc_clf.score(files_test, categories_test))
categories_pred = lsvc_clf.predict(files_test)
print(accuracy_score(categories_test, categories_pred))
# f1_score la diem ket hop giua precision vs recall
# MICRO: weights each sample equally => no favouring any class
# WEIGHTED: The F1 Scores are calculated for each label and then their average is weighted by support - which is the
# number of true instances for each label => favoring majority
# MACRO: weights each class equally => favoring minority
print(f1_score(categories_test, categories_pred, average='macro'))
print(f1_score(categories_test, categories_pred, average='micro'))
print(f1_score(categories_test, categories_pred, average='weighted'))


"CountVectorizer"
vectorizer2 = CountVectorizer(max_features=one_quarter, min_df=10)
files_vectorized2 = vectorizer2.fit_transform(new_combined_files)
files_vectorized2 = files_vectorized2.toarray()
print(files_vectorized2.shape)

# pca = PCA().fit(files_vectorized2)
# print(pca.explained_variance_ratio_)
# plt.plot(np.cumsum(pca.explained_variance_ratio_))
# plt.xlabel('number of components')
# plt.ylabel('cumulative explained variance')
# plt.show()

pca = PCA(n_components=2000)
files_vectorized2 = pca.fit_transform(files_vectorized2)

files_train2, files_test2, categories_train2, categories_test2 = train_test_split(files_vectorized2, categories)

sgdc_clf2 = SGDClassifier()
sgdc_clf2.fit(files_train2, categories_train2)
print(sgdc_clf2 .score(files_test2, categories_test2))

lsvc_clf = LinearSVC()
lsvc_clf.fit(files_train2, categories_train2)
categories_pred2 = lsvc_clf.predict(files_test2)
print(lsvc_clf.score(files_test2, categories_test2))
print(accuracy_score(categories_test2, categories_pred2))
# f1_score la diem ket hop giua precision vs recall
# MICRO: weights each sample equally => no favouring any class
# WEIGHTED: The F1 Scores are calculated for each label and then their average is weighted by support - which is the
# number of true instances for each label => favoring majority
# MACRO: weights each class equally => favoring minority
print(f1_score(categories_test2, categories_pred, average='macro'))
print(f1_score(categories_test2, categories_pred, average='micro'))
print(f1_score(categories_test2, categories_pred, average='weighted'))

"Accuracy_score là 0.9"
