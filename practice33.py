#https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/little-monk-and-goblet-of-fire/
from collections import deque



#n = int(raw_input())

school_q = deque()
student_q = [ deque(), deque(), deque(), deque() ] 


with open("70fae0d0-a-input-70fad9b.txt.clean.txt", 'r') as f:
    n = int(f.readline())
    for _ in range(n):

#for _ in range(n):
    #op = raw_input().split()
        op = f.readline().split()
        if op[0] == 'E':
            school = int(op[1])
            student = int(op[2])
            if not student_q[school-1]:
                school_q.append(school)
            student_q[school-1].append(student)
            #if school < 3:
            #    print op, school, student, len(student_q[school-1])
        else:
            school = school_q[0]
            student = student_q[school-1].popleft()
            if not student_q[school-1]:
                school_q.popleft()
            print school, student

    