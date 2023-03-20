import pandas as pd
import seaborn as sns
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


def draw():
    ChatGPT = [0.5558, 0.7504, 0.8065, 0.8553, 0.871]
    ChatGPT_des = [0.5962, 0.733, 0.7936, 0.8317, 0.8615]
    Codex = [0.2849, 0.4195, 0.5255, 0.6007, 0.6455]
    Codex_des = [0.2956, 0.4734, 0.576, 0.6568, 0.705]

    fig = plt.figure(figsize=(10, 7))

    # Generate sample data
    x = [1,2,3,4,5]

    # Plot the lines
    plt.plot(x, ChatGPT, label='ChatGPT')
    plt.plot(x, ChatGPT_des, label='ChatGPT_D')
    plt.plot(x, Codex, label='Codex')
    plt.plot(x, Codex_des, label='Codex_D')

    # Set the x and y labels and title
    plt.xticks(np.arange(min(x), max(x) + 1, 1), fontsize=28, )
    plt.yticks(fontsize=28, )
    plt.xlabel('TOP', size=31)
    plt.ylabel('Repair rate', size=31)
    # plt.title('Repair rate of ChatGPT and Codex across TOP-N')

    # Set the legend
    plt.legend(fontsize=18)

    plt.subplots_adjust(bottom=0.2, left=0.2)
    plt.savefig('./figure/repair_top.jpg')

    # Show the plot
    plt.show()

draw()

