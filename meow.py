import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
    "day" : ["sun", "mon", "tue", "wed", "thur", "fri", "sat"],
    "times_eaten" : [3, 4, 1, 2, 3, 3, 2]
})

print(data)
# data.plot(x="day", y="times_eaten")
sns.histplot(data["times_eaten"], bins=5)
plt.show()