def work_with_file(file_name):
  with open(file_name) as f:
    a = f.readlines()
    return a

for_res = [['2.txt'] + work_with_file('2.txt'), ['1.txt'] + work_with_file('1.txt'), ['3.txt'] + work_with_file('3.txt')]
sort_for_res = sorted(for_res, key=len)
count = 0
with open('res.txt', 'w') as res:
  for i in sort_for_res:
      count += 1
      for k in range(len(i)):
        if k == 0:
          res.write(i[k] + '\n' + f'{count}\n')
        else:
          res.write(f'Строка номер {k} файла {i[0]}\n' + i[k].strip() + '\n')