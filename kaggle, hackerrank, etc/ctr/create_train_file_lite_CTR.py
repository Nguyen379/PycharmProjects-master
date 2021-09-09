import pandas as pd

chunksize = 10**6

ctr_train = pd.DataFrame()
for chunk in pd.read_csv("train.csv", chunksize=chunksize):
    ctr_train = pd.concat([ctr_train, chunk.sample(frac=.05, replace=False, random_state=42)], axis=0)

ctr_train.reset_index(inplace=True)
ctr_train.drop(["index"], axis=1)
ctr_train.to_csv("lite_train.csv", index=False)
train_len = len(ctr_train)
print(train_len)

# ctr_test = pd.DataFrame()
# for chunk in pd.read_csv("test.csv", chunksize=chunksize):
#     ctr_test = pd.concat([ctr_test, chunk.sample(frac=.1, replace=True, random_state=42)], axis=0)
# ctr_test.reset_index(inplace=True)
# ctr_test.to_csv("lite_test2.csv", index=False)
ctr_test = pd.read_csv("test.csv")
test_len = len(ctr_test)
print(test_len)

ctr_combined = pd.concat([ctr_train, ctr_test]).drop(['index', 'id'], axis=1)
# combine test file to process both data at the same time
ctr_combined.to_csv("ctr_combined.csv", index=False)
combined_len = len(ctr_combined)
print(combined_len)

