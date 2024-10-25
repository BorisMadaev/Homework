team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

challenge_result = result


print('В команде %s участников: %s !' % ('Мастера кода', team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

print('Команда {} решила задач: {} !'.format('Волшебники данных', score_2))
print('{} решили задачи за {} с !'.format('Волшебники данных', round(team2_time, 1)))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!')
