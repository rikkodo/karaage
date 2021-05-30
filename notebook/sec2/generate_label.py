# -*- coding: utf-8 -*-

import os
import sys
import shutil

def generate_label(original_dir, backup_dir, label_name):
    '''
    Generate Labels from dir

    parameter
    ------------
    original_dir: str
        original directory name
    bacukp_dir: str
        backup directory name
    label_name: str
        label_name

    return
    ------------
    NUM_CLASSES: str[]
        list of classes.
    '''
    labels = [d
        for d in os.listdir(original_dir)
            if os.path.isdir(os.path.join(original_dir, d))]
    labels.sort()

    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)

    os.mkdir(backup_dir)

    with open(backup_dir + label_name, 'w') as f:
        for label in labels:
            f.write(label + "\n")

    return labels


if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 4):
        print("Usage: $ python " + param[0] + " original_directory backup directory")
        quit()

    generate_label(param[1], param[2], param[3])