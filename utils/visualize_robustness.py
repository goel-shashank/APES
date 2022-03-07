import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

params = {
    "axes.titlesize": 22,
    "legend.fontsize": 16,
    "figure.figsize": (10, 8),
    "axes.labelsize": 16,
    "axes.titlesize": 16,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "figure.titlesize": 22
}

plt.rcParams.update(params)
plt.style.use("seaborn-whitegrid")
sns.set_style("white")

df_disability = pd.read_csv("data/predictions/disability.predictions.csv") 
df_gender = pd.read_csv("data/predictions/gender.predictions.csv") 
df_religion = pd.read_csv("data/predictions/religion.predictions.csv") 
df_race = pd.read_csv("data/predictions/race.predictions.csv") 

df_disability["Type of Social Bias"] = "Disability"
df_gender["Type of Social Bias"] = "Gender"
df_religion["Type of Social Bias"] = "Religion"
df_race["Type of Social Bias"] = "Race"

udf = pd.concat([df_disability[:(len(df_disability) // 2)].reset_index(drop = True), df_gender[:(len(df_gender) // 2)].reset_index(drop = True), df_religion[:(len(df_religion) // 2)].reset_index(drop = True), df_race[:(len(df_race) // 2)].reset_index(drop = True)]).reset_index(drop = True)
ldf = pd.concat([df_disability[(len(df_disability) // 2):].reset_index(drop = True), df_gender[(len(df_gender) // 2):].reset_index(drop = True), df_religion.loc[(len(df_religion) // 2):].reset_index(drop = True), df_race.loc[(len(df_race) // 2):].reset_index(drop = True)]).reset_index(drop = True)

df = pd.DataFrame(columns = ["Correct", "Probability"])
df["Type of Social Bias"] = udf["Type of Social Bias"]
df["Correct"] = (udf["prediction"] != ldf["prediction"]).apply(lambda x: "Correct" if(x) else "Incorrect")
df["uconfidence"] = udf["confidence"]
df["lconfidence"] = ldf["confidence"]
df["Probability"] = df.apply(lambda row: abs(row["uconfidence"] - row["lconfidence"]) if (row["Correct"] == "Correct") else abs(1 - row["uconfidence"] - row["lconfidence"]), axis = 1)
df = df.drop(columns = ["uconfidence", "lconfidence"])

df["Bucket"] = pd.qcut(df["Probability"], 50, labels = False)
sizes = df.groupby(["Type of Social Bias", "Correct", "Bucket"]).size()
df = df.groupby(["Type of Social Bias", "Correct", "Bucket"]).agg("mean").reset_index()

fig, ax = plt.subplots()
sns.stripplot(x = df["Type of Social Bias"], y = df["Probability"], hue = df["Correct"], sizes = sizes * 5, palette = "Set2", dodge = True)
ax.get_legend().remove()
ax.legend(loc = "upper center", bbox_to_anchor = (0.5, 1.1), ncol = 2, fancybox = True, shadow = True)
ax.set_ylabel(ax.get_ylabel(), labelpad = 15)
ax.set_xlabel(ax.get_xlabel(), labelpad = 15)
plt.savefig("plots/robustness.png")