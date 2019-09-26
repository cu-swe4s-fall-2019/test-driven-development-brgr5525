import sys
import os.path
from os import path
import math_lib
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def boxplot(L, out_file_name):

    try:
        exist = path.exists(out_file_name)
    except TypeError:
        raise TypeError('No file name given.')

    if exist:
        raise SystemExit('File already exists.')

    width = 3
    height = 3

    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.boxplot(L)

    mean = round(math_lib.list_mean(L), 5)
    stdev = round(math_lib.list_stdev(L), 7)

    title = str('Mean: ' + str(mean) + ' Stdev: ' + str(stdev))
    ax.set_title(title)

    ax.set_xlabel('Value')
    ax.set_ylabel('Distribution')

    plt.savefig(out_file_name, bbox_inches='tight')


def histogram(L, out_file_name):
    try:
        exist = path.exists(out_file_name)
    except TypeError:
        raise TypeError('No file name given.')

    if exist:
        raise SystemExit('File already exists.')

    width = 3
    height = 3

    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.hist(L)

    mean = round(math_lib.list_mean(L), 5)
    stdev = round(math_lib.list_stdev(L), 7)

    title = str('Mean: ' + str(mean) + ' Stdev: ' + str(stdev))
    ax.set_title(title)

    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    plt.savefig(out_file_name, bbox_inches='tight')


def combo(L, out_file_name):
    try:
        exist = path.exists(out_file_name)
    except TypeError:
        raise TypeError('No file name given.')

    if exist:
        raise SystemExit('File already exists.')

    fig, axs = plt.subplots(1, 2)

    # Create the box subplot
    axs[0].boxplot(L)

    mean = round(math_lib.list_mean(L), 5)
    stdev = round(math_lib.list_stdev(L), 7)

    title = str('Mean: ' + str(mean) + ' Stdev: ' + str(stdev))
    axs[0].set_title(title)

    axs[0].set_xlabel('Value')
    axs[0].set_ylabel('Distribution')

    # Create the histogram subplot
    axs[1].hist(L)

    axs[1].set_title(title)

    axs[1].set_xlabel('Value')
    axs[1].set_ylabel('Frequency')

    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                        hspace=0.4, wspace=0.4)

    plt.savefig(out_file_name, bbox_inches='tight')
