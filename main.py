import numpy as np
import pandas as pd
import seaborn as sns



# Load (Adjust paths based on your folder structure)
train = pd.read_csv('data_set_ALL_AML_train.csv')
test = pd.read_csv('data_set_ALL_AML_independent.csv')

gene_names = train['Gene Accession Number']
df_numeric = train.drop(['Gene Description', 'Gene Accession Number'], axis=1)


df_numeric = df_numeric.loc[:, ~df_numeric.columns.str.contains('call')]


X_train = df_numeric.T

# Renaming columns to GAN for readability
X_train.columns = gene_names.values

print(f"New Shape: {X_train.shape}") # Should be (32, 7129)

log_data = {
    'experiment_id': [],
    'feature_selection': [], 
    'model_type': [],       
    'accuracy': [],
    'notes': []
}

# Create the dataframe and save it as your initial log
log_df = pd.DataFrame(log_data)
log_df.to_csv('experiment_log.csv', index=False)