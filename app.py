from menu.main_menu import destination_menu
from icecream import ic
import matplotlib.pyplot as plt
import seaborn as sns

__name__ = "__main__"

if __name__ == "__main__":
    destination_menu()

a = 5
ic(a)
# # data to display on plots
# x = [100, 100, 8]
# y = [100, 10, 10]

# # This will plot a simple line chart
# # with elements of x as x axis and y
# # as y axis
# plt.plot(x, y)
# plt.title("Line Chart")

# # Adding the legends
# plt.legend(["Line"])
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")
sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    col="time",
    hue="smoker",
    style="smoker",
    size="size",
)

plt.show()
