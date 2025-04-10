import pandas as pd
import seaborn as sns
import numpy as np


titanic_data = sns.load_dataset("titanic")


def count_nulls(data): #1
    return data.isnull().sum()


def delete_nulls(data): #2
    rows_half = data.shape[0] / 2
    cols_half = data.shape[1] / 2
    for column in data.columns:
        if data[column].isnull().sum() > rows_half:
            del data[column]
    for index, row in data.iterrows():
        if row.isnull().sum() > cols_half:
            data.drop(index, inplace=True)


def fill_nulls(data): #3
    men_mask = data['who'] == 'man'
    women_mask = data['who'] == 'woman'
    child_mask = data['who'] == 'child'

    men_age = data[men_mask]['age'].median()
    women_age = data[women_mask]['age'].median()
    child_age = data[child_mask]['age'].median()

    data.loc[men_mask, 'age'] = data.loc[men_mask, 'age'].fillna(men_age)
    data.loc[women_mask, 'age'] = data.loc[women_mask, 'age'].fillna(women_age)
    data.loc[child_mask, 'age'] = data.loc[child_mask, 'age'].fillna(child_age)


def delete_withnull_rows(data): #4
    for index, row in data.iterrows():
        if row.isnull().sum() > 1:
            data.drop(index, inplace=True)


def from_city_max(data): #5
    return data['embark_town'].value_counts().idxmax()


def survivors_proportion(data, tag=None): #6, #8
    match tag:
        case None:
            return (data['survived'].value_counts(normalize=True)[1]) * 100
        case _:
            unique = data[tag].unique()
            result = [
                round(data[data[tag] == v]['survived'].value_counts(normalize=1)[1] * 100, 2)
                for v in unique
            ]
            return pd.Series(result, index=unique)


def survivors_by_city(data): #7
    return data[data['survived'] == 1]['embark_town'].value_counts()


# # Task 1
# print("\033[1mTask 1:\033[0m\n")
# print( count_nulls(titanic_data) )
# 
# # Task 2
# print("\n\033[1mTask 2:\033[0m\n")
# delete_nulls(titanic_data)
# print( titanic_data.isnull().sum() )
# 
# # Task 3
# print("\n\033[1mTask 3:\033[0m\n")
# fill_nulls(titanic_data)
# print( titanic_data.isnull().sum() )
# 
# # Task 4
# print("\n\033[1mTask 4:\033[0m\n")
# delete_withnull_rows(titanic_data)
# print( titanic_data.isnull().sum() )
# 
# # Task 5
# print("\n\033[1mTask 5:\033[0m\n")
# print("Больше всего пассажиров прибыли из города:", from_city_max(titanic_data) )
# 
# # Task 6
# print("\n\033[1mTask 6:\033[0m\n")
# print("Доля выживших пассажиров: {:.2f}%".format(survivors_proportion(titanic_data)))

# # Task 7
# print("\n\033[1mTask 7:\033[0m\n")
# print("Количество выживших пассажиров в городах:\n", survivors_by_city(titanic_data))

# # Task 8
# print("\n\033[1mTask 8:\033[0m\n")
# print("Доля выживших пассажиров по классам:\n", survivors_proportion(titanic_data, 'class'))
