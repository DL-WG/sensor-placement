#!/usr/bin/python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import GPy

""" FILE NAME: 'visualization.py'
    DESCRIPTION: This file is providing visualizations for the data used in this
    project. Particularly, it is used to assist the identification of areas with
    sufficiently high tracer values to place sensors in.
"""

def printHistogramInformation(title, bins, counts):
    """ This function prints the title, bins and counts of the histogram that is displayed.
        Input:
        - title: specifies the title of the histogram.
        - bins: specifies the bins.
        - counts: specifies how many observations are in each bin.
    """
    print(title, ':\n')
    print('Bins:\n', bins, '\n')
    print('counts:\n', counts, '\n')

def showHistogram(data, title, number_bins=400):
    """ This function prints calculates and displays an histogram based on the
        inputted data.
        Input:
        - data: data on which the histogram is calculated on.
        - title: specifies the title of the histogram.
        - number_bins: specifies how many bins the histogram should have
    """
    plt.figure(figsize=(10, 4))
    counts, bins = np.histogram(data, bins=number_bins)
    plt.title(title + '. Number of bins: ' + str(number_bins))
    plt.hist(bins[:-1], bins, weights=counts)
    printHistogramInformation(title, bins, counts)
    plt.show()

df6 = pd.read_csv('data/csv_data/area6.csv')
df8 = pd.read_csv('data/csv_data/area8.csv')
df10 = pd.read_csv('data/csv_data/area10.csv')
df15 = pd.read_csv('data/csv_data/area15.csv')
showHistogram(df6, 'LSBU_500_6')
showHistogram(df8, 'LSBU_500_8')
showHistogram(df6, 'LSBU_500_10')
showHistogram(df8, 'LSBU_500_15')
