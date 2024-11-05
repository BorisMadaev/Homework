import pandas as pd
import numpy as np


matrix_0 = np.zeros((10, 3))

print(f'\n{matrix_0}')

matrix_1 = np.ones((10, 3))

print(f'\n{matrix_1}')

matrix = np.random.randn(10, 3)

print(f'\n{matrix}')

dates = pd.date_range("20241105", periods=10)

print(f'\n{dates}')

df = pd.DataFrame(matrix, index=dates, columns=list("ABС"))

print(f'\n{df}')

df0 = df.head(2)

print(f'\n{df0}')

df1 = df.tail(3)

print(f'\n{df1}')
