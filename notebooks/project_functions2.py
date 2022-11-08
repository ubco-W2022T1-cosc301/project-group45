import numpy as np
import pandas as pd
import seaborn as sns

def load_and_process (uncleaned):
    cleaned1 = (pd.read_csv(uncleaned).copy().drop(['age','smoker', 'bmi'], axis=1))
    cleaned2 = cleaned1.assign(parent= cleaned1["children"] > 0)
    
    return cleaned2