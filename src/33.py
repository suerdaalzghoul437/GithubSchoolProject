import pandas as pd
data = {
    "StudentID": [101, 102, 103],
    "CourseName": ["Mathematics", "Physics", "Chemistry"],
    "Grade": [85, 90, 76]
}
df = pd.DataFrame(data)
print(df)
