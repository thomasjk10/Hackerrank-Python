from operator import itemgetter
n = int(input())
stud_marks = list()
new_list = list()

for i in range(n):
    name = input()
    score = float(input())
    stud_marks.append([])
    stud_marks[i] = [name, score]

print (stud_marks)
min_scper = min(stud_marks, key=lambda x: x[1])
min_score = min_scper[1]
new_list = [i for i in stud_marks if i[1] != min_score ]
min_scper2 = min(new_list, key=lambda x: x[1])
min_score2 = min_scper2[1]
new_list2 = [i for i in new_list if i[1] == min_score2 ]
new_list2.sort(key=itemgetter(0))

for name in new_list2:
    print (name[0])
