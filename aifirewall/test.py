import pandas
from sklearn.preprocessing import LabelEncoder
from numpy import array
from sklearn.preprocessing import OneHotEncoder

df = pandas.DataFrame({
    'pets': ['cat', 'dog', 'cat', 'monkey', 'dog', 'dog'],
    'owner': ['Champ', 'Ron', 'Brick', 'Champ', 'Veronica', 'Ron'],
    'location': ['San_Diego', 'New_York', 'New_York', 'San_Diego', 'San_Diego',
                 'New_York']
})

a = df.apply(LabelEncoder().fit_transform)
a = array(a)
df_2 = pandas.get_dummies(df,drop_first=True)
a = df.reindex(columns = df_2.columns, fill_value=0)
print(a)
print(df_2)
