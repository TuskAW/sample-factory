import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()

labels = ['20', '40', '80', '160', '320', '640']
fps_by_method_10_core_cpu = dict(
    impala=[8590, 10596, 10941, 10928, 13328, math.nan],
    rllib=[9384, 9676, 11171, 11328, 11590, 11345],
    ours=[10894, 16982, 25068, 37410, 46977, 52033]
)

fps_by_method_36_core_cpu = dict(
    impala=[6951, 8191, 8041, 9900, 10014, math.nan],
    rllib=[9384, 9676, 11171, 11328, 11590, 11345],
    ours=[10894, 16982, 25068, 37410, 46977, 50222]
)

data = fps_by_method_10_core_cpu

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()

item_idx = 0
bars = dict()
for key, value in data.items():
    rects = ax.bar(x + item_idx * width - len(data) * width / 2, value, width, label=key)
    bars[key] = rects
    item_idx += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Num. environments in parallel')
ax.set_ylabel('Environment frames per second')
ax.set_title('Throughput of different RL methods')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom')


autolabel(bars['ours'])

fig.tight_layout()
plt.show()