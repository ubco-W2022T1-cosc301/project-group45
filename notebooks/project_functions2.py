import numpy as np
import pandas as pd
import seaborn as sns

def load_and_process (uncleaned):
    df = pd.read_csv(uncleaned)
    cleaned_data = (df.copy()
                    .drop(['age','smoker', 'bmi'], axis=1)
                    .assign(sex_region= df['sex'].astype(str) + "_" + df['region'].astype(str))
                    .assign(parent= df["children"] > 0)
                   )
    return cleaned_data