import os
import mlflow
import argparse

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main(args):
    # enable auto logging
    print("###############$$$$$$$$$$$$$$$$$$$")
    mlflow.autolog()

    # read in data
    print("ds:",args.dataset)
    mlflow.log_param("###dataset", args.dataset)
    df = pd.read_csv(args.cdataset)


    print("########### ", df)


def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--dataset", type=str)
    # parse args
    args = parser.parse_args()

    # return args
    return args


# run script
if __name__ == "__main__":
    # parse args
    args = parse_args()

    # run main function
    main(args)