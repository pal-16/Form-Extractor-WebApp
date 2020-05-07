import pandas as pd
import csv
from pathlib import Path

def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if  ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list

def column_value_counts(df,col):
    dictionary = dict(df.groupby([col])[col].count())
    if 'None' in dictionary.keys():
        dictionary.pop('None')
    return dictionary


def add_to_big_dict(df,filename):
    big_dict = {}
    if Path(filename).exists():
        reader = csv.DictReader(open(filename))
        for row in reader:
            for col,val in row.items():
                big_dict.setdefault(col,[]).append(val)
    for col in df.columns:
        col_dict = column_value_counts(df,col)
        for k,_ in col_dict.items():
            if k in big_dict.keys():
                big_dict[k] = int(big_dict[k][0]) + 1
            else:
                big_dict[k]=1
    with open(filename, 'w') as f:  
        w = csv.DictWriter(f,fieldnames=big_dict.keys())
        w.writeheader()
        w.writerow(big_dict)
    return big_dict

def extract_top_skills(observations):
    df = {
        'title': list(observations['title']),
        'databases' : list(observations['databases']),
        'programming languages': list(observations['programming languages']),
        'machine learning': list(observations['machine learning']),
    }
    df = pad_dict_list(df,"None")
    df = pd.DataFrame.from_dict(df)
    big_dict = add_to_big_dict(df.drop('title',axis=1),'top_skills.csv')
    top_skills = [(k,v) for k,v in sorted(big_dict.items(),key = lambda item: item[1])]
    top_titles = extract_top_titles(df)
    return big_dict,top_skills[:5],top_titles

def extract_top_titles(df):
    col_dict = column_value_counts(df,'title')
    big_dict = {}
    if Path('top_titles.csv').exists():
        reader = csv.DictReader(open('top_titles.csv'))
        for row in reader:
            for col,val in row.items():
                big_dict.setdefault(col,[]).append(val)
    for k,_ in col_dict.items():
        if k in big_dict.keys():
            big_dict[k] = int(big_dict[k][0]) + 1
        else:
            big_dict[k]=1
    with open('top_titles.csv', 'w') as f:  
        w = csv.DictWriter(f,fieldnames=big_dict.keys())
        w.writeheader()
        w.writerow(big_dict)
    top_titles = [(k,v) for k,v in sorted(big_dict.items(),key = lambda item: item[1])]
    return top_titles
    
