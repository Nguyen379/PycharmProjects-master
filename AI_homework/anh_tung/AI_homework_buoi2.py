import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# sns.displot(tips['total_bill'], bins=50, kde=True)
# sns.countplot(x="sex", data=tips)
# sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)
# sns.violinplot(x="day", y="total_bill", hue="sex", data=tips)

titanic = sns.load_dataset('titanic')
# sns.jointplot(data=titanic, x="fare", y="age")
# sns.displot(titanic['fare'], bins=20, color='red')
# sns.boxplot(data=titanic, y="age", x="class")
# sns.swarmplot(data=titanic, x='class', y='age')
# sns.countplot(data=titanic, x='sex')
sns.heatmap(titanic.corr(), cmap="coolwarm", annot=True)
sns.set_style('white') # no squares dividing
plt.legend()
plt.show()
