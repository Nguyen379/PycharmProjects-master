import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ctr_combined = pd.read_csv("ctr_combined.csv")
lite_train = pd.read_csv("lite_train.csv")
train_len = 2021448
test_len = 4577464
combined_len = 6598912


# convert data in "hour" column in Year-month-date form
def get_date(hour):
    y = "20" + str(hour)[:2]
    m = str(hour)[2:4]
    d = str(hour)[4:6]
    return y + "-" + m + "-" + d


ctr_combined["weekday"] = pd.to_datetime(ctr_combined["hour"].apply(get_date)).dt.dayofweek.astype(str)


# transform hour column into column with only hour instead of full date like before
def tran_hour(x):
    x = x % 100
    while x in [23, 0]:
        return '23-01'
    while x in [1, 2]:
        return '01-03'
    while x in [3, 4]:
        return '03-05'
    while x in [5, 6]:
        return '05-07'
    while x in [7, 8]:
        return '07-09'
    while x in [9, 10]:
        return '09-11'
    while x in [11, 12]:
        return '11-13'
    while x in [13, 14]:
        return '13-15'
    while x in [15, 16]:
        return '15-17'
    while x in [17, 18]:
        return '17-19'
    while x in [19, 20]:
        return '19-21'
    while x in [21, 22]:
        return '21-23'


ctr_combined['hour'] = ctr_combined.hour.apply(tran_hour)
len_of_feature_count = []

for n in ctr_combined.columns[2:23]:
    # print(n, ":", len(ctr_train[n].value_counts()), ":", ctr_train[n].dtypes)
    len_of_feature_count.append(len(ctr_combined[n].value_counts()))

# all columns with dtypes int64 have len(value_count) << 6 million => int64 will be converted to object to be used for
# classification, not regression
list_tran_feature = ctr_combined.columns[2:4].tolist() + ctr_combined.columns[13:23].tolist()
# list feature se bi convert thanh dang object
for n in list_tran_feature:
    ctr_combined[n] = ctr_combined[n].astype(str)

ctr_train_des = ctr_combined.describe()
obj_features = []
# contain features with too many value_counts. Such features will be reduced in dimension to 5 bins
for n in range(len(len_of_feature_count)):
    if len_of_feature_count[n] > 10:
        obj_features.append(ctr_combined.columns[2:23][n])


class Transform_df:
    def __init__(self, df):

        self.df = df
        # boi vi co rat nhieu feature, ta se chia feature thanh 5 bins: <vl, <l, h>&>l ,>h, >vh.
        # vl: very low, l: low, h: high, vh: very high
        # cach tinh bins: click_rate==1 / sum(click_rate). So voi mean click_rate de tinh mean
        self.values = self.df[self.df.columns[0]].value_counts()
        # get value_counts of Series
        if len(self.values) > 1000:
            self.values = self.values[:1000]
            # only get 1000 most common values

        self.values = pd.DataFrame(self.values)
        # each row is like: "feature : occurrences"
        self.values["new_col"] = self.values.index
        # each row is like: "feature : occurrences : feature"
        self.values["click_rate"] = self.values.new_col.apply(self.get_click_rate)
        # each row is like: "feature : occurrences : feature: respective_click_rate_of_feature

        self.vl, self.l, self.h, self.vh = self.get_bins()

    def get_click_rate(self, cell):
        all_clicks = lite_train[lite_train[self.df.columns[0]] == cell]
        click_rate = round((all_clicks.click.sum() / all_clicks.click.count()), 3)
        return click_rate

    def get_bins(self):
        vh = ctr_train_des.loc["mean", "click"] + 0.04
        h = ctr_train_des.loc["mean", "click"] + 0.02
        l = ctr_train_des.loc["mean", "click"] - 0.02
        vl = ctr_train_des.loc["mean", "click"] - 0.04

        vh_index = self.values[self.values["click_rate"] >= vh].index.tolist()
        h_index = self.values[(self.values["click_rate"] > h) & (self.values["click_rate"] < vh)].index.tolist()
        l_index = self.values[(self.values["click_rate"] < l) & (self.values["click_rate"] > vl)].index.tolist()
        vl_index = self.values[self.values["click_rate"] <= vl].index.tolist()
        # return the names of features in their respective bins
        return vl_index, l_index, h_index, vh_index

    def new_ctr_train(self, cell):
        while cell in self.vl:
            return "very_low"
        while cell in self.l:
            return "low"
        while cell in self.h:
            return "high"
        while cell in self.vh:
            return "very_high"
        return "mid"

    def return_value(self):
        return self.df[self.df.columns[0]].apply(self.new_ctr_train)


for n in obj_features:
    t = Transform_df(ctr_combined[[n]])
    ctr_combined[[n]] = t.return_value()

print(ctr_combined)

for n in ctr_combined.columns:
    sns.countplot(x=n, hue="click", data= ctr_combined)
    plt.show()

ctr_combined.drop(["device_id", "C14", "C17", "C19", "C20", "C21"], axis=1, inplace=True)
ctr_combined = pd.get_dummies(ctr_combined)
train = ctr_combined[:train_len]
test = ctr_combined[train_len:]

ctr_combined.to_csv("analyzed_ctr_combined.csv", index=False)
train.to_csv("analyzed_train.csv", index=False)
test.to_csv("analyzed_test.csv", index=False)
