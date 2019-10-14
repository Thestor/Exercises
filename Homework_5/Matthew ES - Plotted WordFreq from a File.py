# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:58:27 2019

@author: Matthew
"""

import matplotlib.pyplot as plt
import re
import numpy as np

def draw_hbar(word_data):
    
    y_pos = np.arange(len(word_data.keys()))
    freq = word_data.values()

    fig, ax = plt.subplots(dpi=80, figsize=(10, 8))

    ax.barh(y_pos, freq, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word_data.keys())
    ax.set_xlabel("Frequency")
    ax.set_title("Word Frequencies")

    plt.axis(xmax = max(word_data.values()) + 1)

    plt.title("Words and Their Frequency")
    plt.xlabel("Frequency")
    plt.ylabel("Word")

    plt.show()

def create_plot_of_wordfreq_from_file(filename):
    
    with open(filename) as f:
        
        sentence = f.read().rstrip()
        word_data = dict()
        new_word_data= dict()
        sentence = re.sub('[^a-zA-Z0-9\n]', ' ', sentence)
        for word in sentence.lower().split():
            word_data[word] = word_data.get(word, 0) + 1
        for key, value in sorted(word_data.items(), key=lambda item: item[1]):
            new_word_data[key] = value
        draw_hbar(new_word_data)
        
        f.close()
        
filename = "Text Files\Indonesia Raya.txt"
create_plot_of_wordfreq_from_file(filename)
        
        