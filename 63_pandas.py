import pandas as pd

data = {
    'name':["Ayush", "aryan", "Akash"],
    'age' :[18 ,19, 20],
    'scores': [70, 95, 90]
}

df = pd.DataFrame(data)
print(df['scores'])
mean = df['scores'].mean()
print(mean)