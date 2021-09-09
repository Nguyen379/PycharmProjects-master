import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

train = pd.read_csv("analyzed_train.csv")
test = pd.read_csv("analyzed_test.csv")
# tỉ lệ clicked: not clicked = 1:4 => unbalanced.
# tạo file mới từ file cũ có tỉ lệ clicked: not clicked = 1:1. Dùng gridsearch để tìm feature quan trọng.

pre_X = train[train["click"] == 0].sample(n=len(train[train["click"] == 1]), random_state=42)
# lay 1 luong not clicked = clicked
pre_X = pd.concat([pre_X, train[train["click"] == 1]]).sample(frac=1)
pre_y = pre_X[["click"]].values.ravel()
pre_X.drop(["click"], axis=1, inplace=True)
test.drop(["click"], axis=1, inplace=True)

import lightgbm as lgb
from sklearn.model_selection import GridSearchCV, train_test_split

pre_X_train, pre_X_test, pre_y_train, pre_y_test = train_test_split(pre_X, pre_y, test_size=0.2, stratify=pre_y,
                                                                    random_state=42)

# ti le clicked unbalanced => dung un_balanced hoac chia ra r tim gridsearch trc

# TESTED_PARAMS = {"num_leaves": [255, 512, 1023, 2047],
#                  "max_depth": [12, 16, 20]}

# clf = lgb.LGBMClassifier(boosting_type="goss",
#                          learning_rate=0.001,
#                          is_unbalance=False,
#                          objective="binary",
#                          n_estimators=5000,
#                          max_bin=255,
#                          num_leaves=2047,
#                          max_depth=20,
#                          metric="logloss")
#
# grid_search = GridSearchCV(clf, param_grid=TESTED_PARAMS, scoring="roc_auc", cv=50, verbose=1, n_jobs=-1)
# grid_search.fit(pre_X_train, pre_y_train)
#
# print(grid_search.best_params_)
# print(grid_search.best_estimator_)
# print(grid_search.best_score_)

clf = lgb.LGBMClassifier(boosting_type="goss",
                         learning_rate=0.001,
                         is_unbalance=False,
                         objective="binary",
                         n_estimators=5000,
                         max_bin=255,
                         num_leaves=2047,
                         max_depth=20,
                         metric="logloss")
clf.fit(pre_X, pre_y)
feature_importances = pd.DataFrame(clf.feature_importances_)
feature_importances.index = pre_X.columns
feature_importances.sort_values(feature_importances.columns[0], axis=0, ascending=False, inplace=True)
print(feature_importances)

# pre_X_train = pre_X_train[feature_importances.index[:int(len(feature_importances)/3)]]
# pre_X_test = pre_X_test[feature_importances.index[:int(len(feature_importances)/3)]]


# TESTED_PARAMS = {"learning_rate": np.arange(0.01, 0.11, 0.01),
#                  "num_leaves": [127, 255, 511, 1023]}
# grid_search = GridSearchV(clf, param_grid=TESTED_PARAMS, scoring="roc_auc", cv=100, verbose=1, n_jobs=-1)
# grid_search.fit(pre_X_train, pre_y_train)
#
# print(grid_search.best_params_)
# print(grid_search.best_estimator_)
# print(grid_search.best_score_)
# {'learning_rate': 0.02, 'num_leaves': 127}
# LGBMClassifier(boosting_type='goss', is_unbalance=True, learning_rate=0.02,
#                max_bin=255, max_depth=6, metric='binary_logloss',
#                n_estimators=300, num_leaves=127, objective='binary')
# 0.7042741730132969

# clf = lgb.LGBMClassifier(boosting_type='goss',
#                          learning_rate=0.1,
#                          max_depth=11,
#                          metric='binary_logloss',
#                          n_estimators=500,
#                          num_leaves=511,
#                          objective='binary')
#
# clf.fit(pre_X, pre_y)
# feature_importances = pd.DataFrame(clf.feature_importances_)
# feature_importances.index = pre_X.columns
# feature_importances = feature_importances.sort_values(feature_importances.columns[0], ascending=False)
# print(feature_importances)

from sklearn.metrics import roc_auc_score, confusion_matrix

cols = feature_importances[:25]
print(cols)
features = cols.index
print(features)

X_train = train[features]
y_train = train[["click"]].values.ravel()
X_test = test[features]

clf.fit(X_train, y_train)
y_pred = clf.predict(X_train)
print(roc_auc_score(y_train, y_pred) * 100)

confmat = confusion_matrix(y_true=y_train, y_pred=y_pred, labels=[0, 1])
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va="center", ha="center")

plt.xlabel("Predicted")
plt.ylabel("True")
plt.tight_layout()

submission = pd.read_csv("sampleSubmission.csv")
submission[submission.columns[1]] = clf.predict_proba(X_test)[:, 1]
submission.to_csv("submission_lightgbm.csv", index=False)
plt.show()

"lan 1"
# device_model_mid        7989
# device_model_very_high  6613
# C18_0                   5779
# weekday_1               5556
# C18_3                   5331
# ...                      ...
# C16_20                     0
# C16_1024                   0
# C15_768                    0
# C15_120                    0
# C16_90                     0
#
# [101 rows x 1 columns]

"lan 2"
# device_model_mid        7989
# device_model_very_high  6613
# C18_0                   5779
# weekday_1               5556
# C18_3                   5331
# ...                      ...
# C1_1012                  294
# device_type_5            266
# C16_480                  260
# device_type_1            175
# C15_728                  173
#
# [80 rows x 1 columns]

# Em thấy điểm thấp như vậy vì lightgbm xác định sai những cái feature importances: lẽ ra những cái app_id, site_id phải
# cao hơn nhiều như trong ảnh xgboost

"dart"
# clf = lgb.LGBMClassifier(boosting_type="dart",
#                          learning_rate=0.001,
#                          is_unbalance=False,
#                          objective="binary",
#                          n_estimators=5000,
#                          max_bin=255,
#                          num_leaves=511,
#                          max_depth=20,
#                          metric="logloss")
#                         0
# banner_pos_0        93498
# weekday_1           85798
# C18_0               82921
# C18_1               80387
# device_conn_type_0  79499
# ...                   ...
# banner_pos_3            0
# C16_36                  0
# C15_480                 0
# C16_20                  0
# C16_320                 0
#
# [101 rows x 1 columns]
#                         0
# banner_pos_0        93498
# weekday_1           85798
# C18_0               82921
# C18_1               80387
# device_conn_type_0  79499
# ...                   ...
# C16_480             12988
# banner_pos_7        11940
# app_domain_high     11519
# site_domain_high    10719
# device_conn_type_3  10149
#
# [61 rows x 1 columns]
# 61
# 51.57401604800952

"goss"
# clf = lgb.LGBMClassifier(boosting_type="goss",
#                          learning_rate=0.001,
#                          is_unbalance=False,
#                          objective="binary",
#                          n_estimators=5000,
#                          max_bin=255,
#                          num_leaves=2047,
#                          max_depth=20,
#                          metric="logloss")
# [101 rows x 1 columns]
#                              0
# device_model_mid        472511
# C18_0                   470655
# weekday_1               449756
# weekday_2               443529
# weekday_3               424819
# device_model_very_high  345770
# C18_3                   299403
# C18_2                   268577
# hour_13-15              267819
# weekday_6               253035
# hour_15-17              250382
# hour_11-13              247792
# device_model_high       246082
# hour_09-11              243998
# banner_pos_0            242040
# hour_07-09              240858
# hour_05-07              236576
# device_conn_type_0      231789
# weekday_0               231768
# weekday_4               228805
# weekday_5               228072
# hour_17-19              221349
# hour_03-05              207910
# device_ip_mid           193320
# device_model_very_low   192140
