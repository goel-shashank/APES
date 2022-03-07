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

df = pd.concat([df_disability, df_gender, df_religion, df_race])
df["Incorrect"] = (df["prediction"] != df["label"]).apply(lambda x: "Incorrect" if(x) else "Correct")
df["Probability"] = df["confidence"]
df["Bucket"] = pd.qcut(df["Probability"], 50, labels = False)
sizes = df.groupby(["Type of Social Bias", "Incorrect", "Bucket"]).size()
df = df.groupby(["Type of Social Bias", "Incorrect", "Bucket"]).agg("mean").reset_index()

fig, ax = plt.subplots()
sns.stripplot(x = df["Type of Social Bias"], y = df["Probability"], hue = df["Incorrect"], sizes = sizes * 5, palette = "Set2", dodge = True)
ax.get_legend().remove()
ax.legend(loc = "upper center", bbox_to_anchor = (0.5, 1.1), ncol = 2, fancybox = True, shadow = True)
ax.set_ylabel(ax.get_ylabel(), labelpad = 15)
ax.set_xlabel(ax.get_xlabel(), labelpad = 15)
plt.savefig("bias.png")