group = {
  1 : {'first_name' : 'Тайвин', 'middle_name' : 'Ланистер', 'sex' : 'man', 'experience' : 1, 'home_work' : [10, 10, 10, 10, 10], 'exam' : 10},
  2 : {'first_name' : 'Нэд', 'middle_name' : 'Старк', 'sex' : 'man', 'experience' : 0, 'home_work' : [2, 4, 6, 8, 10], 'exam' : 2},
  3 : {'first_name' : 'Роберт', 'middle_name' : 'Баратеон', 'sex' : 'man', 'experience' : 0, 'home_work' : [2, 3, 2, 2, 3], 'exam' : 1},
  4 : {'first_name' : 'Серсея', 'middle_name' : 'Ланистер', 'sex' : 'woman', 'experience' : 1, 'home_work' : [3, 3, 3, 3, 3], 'exam' : 3},
  5 : {'first_name' : 'Кэйтлин', 'middle_name' : 'Старк', 'sex' : 'woman', 'experience' : 0, 'home_work' : [4, 3, 4, 3, 4], 'exam' : 3},
  6 : {'first_name' : 'Маргари', 'middle_name' : 'Тирэл', 'sex' : 'woman', 'experience' : 1, 'home_work' : [6, 7, 7, 8, 10], 'exam' : 9},
  7 : {'first_name' : 'Ходор', 'middle_name' : 'Ходор', 'sex' : 'man', 'experience' : 0, 'home_work' : [10, 10, 10, 10, 10], 'exam' : 10},
  8 : {'first_name' : 'Тайвин', 'middle_name' : 'Ланистер', 'sex' : 'man', 'experience' : 1, 'home_work' : [10, 10, 10, 10, 10], 'exam' : 10}
}

# Среднее значение (список усредняемых значений)
def result_middle_appraise(appraise):
  middle_appraise = sum(appraise) / len(appraise)
  return middle_appraise
  
# Среднее значение оценки за ДЗ по группе (словарь с перечнем студентов) 
def middle_appraise_homework(dic):
  home_work = []
  for character in dic.values():
    home_work.append(result_middle_appraise(character['home_work']))
  result = result_middle_appraise(home_work)
  return result
  
# Средняя оценка за экзамен (словарь с перечнем студентов)
def middle_appraise_exam(dic):
  exam = []
  for character in dic.values():
    exam.append(character['exam'])
  result = result_middle_appraise(exam)
  return result
  
# Словарь списка студентов по ключу в словаре с характеристиками(исходный словарь, ключ характеристики по которой нужно отсортировать стедентов, значение ключа)
def dictionary_key(dic, key, value):
  dictionary_new = {}
  for student, character in dic.items():
    if character[key] == value:
      dictionary_new[student] = character
  return dictionary_new
  
# Вычисляем интегральную оценку(сдоварь с характеристиками стедентов)
def integral_appraise(dic):
  integral_appraise_result = 0.6 * result_middle_appraise(dic['home_work']) + 0.4 * dic['exam']
  return integral_appraise_result

# Записываем в характеристики интегральную оценку (словарь группы)
def dictionary_integral_appraise(dic):
  for value in dic.values():
    value['integral_appraise'] = integral_appraise(value)
  return dic

# Список словарей характеристик лучших студентов (словарь группы)
def best_students(dic):
  best_dic = []
  for value in dictionary_integral_appraise(dic).values():
    if len(best_dic) == 0:
      best_dic.append(value)
    elif best_dic[0]['integral_appraise'] < value['integral_appraise']:
      best_dic.clear()
      best_dic.append(value)
    elif best_dic[0]['integral_appraise'] == value['integral_appraise']:
      best_dic.append(value)
  return best_dic
  
# Выводим лучших студентов (Список словарей с лучшими студентами)
def print_best_students(lists):
  print('Лучшие студенты: ', end = '')
  for name in lists:
    print("{first_name} {middle_name} ".format(**name), end = '')
  print(' с интегральной оценкой {}'.format(lists[0]['integral_appraise']))
  
  
# Вывод результата
def print_results():
  # Средняя оценка по группк за ДЗ
  print('Средняя оценка за домашние задания по группе: {:.1f}'.format(middle_appraise_homework(group)))
  # Средняя оценка за экзамен
  print('Средняя оценка за экзамен: {:.1f}\n'.format(middle_appraise_exam(group)))
  # Средняя оценка за домашние задания у мужчин
  print('Средняя оценка за домашние задания у мужчин: {:.1f}'.format(middle_appraise_homework(dictionary_key(group, 'sex', 'man'))))
  # Средняя оценка за экзамен у мужчин
  print('Средняя оценка за экзамен у мужчин: {:.1f}'.format(middle_appraise_exam(dictionary_key(group, 'sex', 'man'))))
  # Средняя оценка за домашние задания у женщин
  print('Средняя оценка за домашние задания у женщин: {:.1f}'.format(middle_appraise_homework(dictionary_key(group, 'sex', 'woman'))))
  # Средняя оценка за экзамен у женщин
  print('Средняя оценка за экзамен у женщин: {:.1f}'.format(middle_appraise_exam(dictionary_key(group, 'sex', 'woman'))))
  print(' ')
  # Средняя оценка за домашние задания у студентов с опытом
  print('Средняя оценка за домашние задания у студентов с опытом: {:.1f}'.format(middle_appraise_homework(dictionary_key(group, 'experience', 1))))
  # Средняя оценка за экзамен у студентов с опытом
  print('Средняя оценка за экзамен у студентов с опытом: {:.1f}'.format(middle_appraise_exam(dictionary_key(group, 'experience', 1))))
  # Средняя оценка за домашние задания у студентов без опыта
  print('Средняя оценка за домашние задания у студентов без опыта: {:.1f}'.format(middle_appraise_homework(dictionary_key(group, 'experience', 0))))
  # Средняя оценка за экзамен у студентов без опыта
  print('Средняя оценка за экзамен у студентов без опыта: {:.1f}'.format(middle_appraise_exam(dictionary_key(group, 'experience', 0))))
  print(' ')
  if len(best_students(group)) == 1:
    print('Лучший студент: {} {} с интегральной оценкой {}'.format(best_students(group)[0]['first_name'], best_students(group)[0]['middle_name'], best_students(group)[0]['integral_appraise']))
  else:
    print_best_students(best_students(group))
    
print_results()