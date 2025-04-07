import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)
X = df[['feature1', 'feature2']]
y = df['target_column']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Assuming 'target_column' is the name of your target column
model = ...
