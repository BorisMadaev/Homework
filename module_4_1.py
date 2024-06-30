from fake_math import divide as f_div
from true_math import divide as t_div

result1 = f_div(5, 0)
result2 = f_div(5, 10)
result3 = t_div(123, 0)
result4 = t_div(123, 2)

print(result1)
print(result2)
print(result3)
print(result4)
