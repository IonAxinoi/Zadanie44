import pandas as pd

# Создание исходного DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Генерация one-hot представления
one_hot = pd.get_dummies(data['whoAmI'])

# Объединение исходного DataFrame с one-hot представлением
data_one_hot = pd.concat([data, one_hot], axis=1)

# Удаление исходного столбца 'whoAmI'
data_one_hot.drop(columns=['whoAmI'], inplace=True)

print(data_one_hot.head())
