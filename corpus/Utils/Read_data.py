import pandas as pd

def get_raw_data(file_path, label):
    df = pd.read_csv(file_path)
    texts1 = df['Oración 1'].values.tolist()
    texts2 = df['Oración 2'].values.tolist()
    similarities = df['Similitud'].values.tolist()
    texts = list(zip(texts1, texts2))
    if label == 1:
        labels = [1]*len(texts1)
    else:
        labels = [0]*len(texts1)
 
    return labels, texts, similarities

def unzip_texts(zip_list):
    res = [[ i for i, j in zip_list ], [ j for i, j in zip_list ]]
    return res[0], res[1]