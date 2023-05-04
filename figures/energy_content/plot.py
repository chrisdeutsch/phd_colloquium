#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme("talk")


x = np.array([5, 27, 68])

fig, ax = plt.subplots(figsize=(1.5, 1.5))
ax.pie(
    x,
    explode=[0.15, 0, 0],
    colors=["#1b9e77", "#d95f02", "#7570b3"],
    #labels=["Ordinary Matter", "Dark Matter", "Dark Energy"],
    #labeldistance=0.25,
    radius=1.25,
    wedgeprops={"linewidth": 1, "edgecolor": "white"},
    textprops={"va": "center", "ha": "left"},
    startangle=90,
    counterclock=False,
    #dict(rotation_mode = 'anchor', va='center', ha='left'),
)
fig.savefig("content.pdf")
