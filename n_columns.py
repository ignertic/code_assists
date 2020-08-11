import numpy as np
import pandas as pd 
# mport numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

train_df = pd.read_csv('https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/regression_sprint/titanic_train_raw.csv')
test_df = pd.read_csv('https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/regression_sprint/titanic_test_raw.csv')


def drop_columns(input_df, threshold, unique_value_threshold):
    columns = input_df.columns
    percent_missing = input_df.isnull().sum() * 100 / len(input_df)
    missing_value_df = pd.DataFrame({'column_name': columns,'percent_missing': percent_missing})
    missing_drop = list(missing_value_df[missing_value_df.percent_missing>threshold].column_name)
    input_df = input_df.drop(missing_drop, axis=1)
    for i in input_df.columns:
        percent = input_df[i].value_counts(normalize=True) * 100
        percent = list(percent)
        avg_of_column = sum(percent)/len(percent)
        if avg_of_column > unique_value_threshold:
            input_df.drop([i], axis = 1) 
    return input_df