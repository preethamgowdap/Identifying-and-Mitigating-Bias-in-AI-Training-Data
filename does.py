import pandas as pd

data = {
    "age": [25, 45, 35],
    "education": ["Bachelors", "Masters", "PhD"],
    "income": ["<=50K", ">50K", ">50K"]
}

df = pd.DataFrame(data)
df.to_csv("adult_income.csv", index=False)

print("Sample dataset created successfully!")
