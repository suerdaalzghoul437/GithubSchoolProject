import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Generate some synthetic data
data = {
    'age': [25, 30, 35, 40, 45],
    'salary': np.random.normal(50000, 10000, 6)
}

df = pd.DataFrame(data)

# Use LinearRegression from scikit-learn to fit the model
model = LinearRegression()
model.fit(df[['age']], df['salary'])

# Get the prediction for a given age
age = 35
predicted_salary = model.predict([age])
print("Predicted salary for age 35:", predicted_salary)
