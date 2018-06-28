n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
#print (student_marks)
query_name = input()
for k,v in student_marks.items():
    if k == query_name:
        avg_mark = format(round(sum(v)/len(v), 2), '.2f')
print (avg_mark)
