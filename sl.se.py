def fares(age, student=False, senior=False):
    print age,student,senior
    if age <=20:
        return 'hel'
    elif age >= 65:
        return 'halv'
    else:
         return 'hel'




print 'barn 11', fares (11)
print 'pension 65',fares (63)
print 'student 22',fares (22)
print 'vuxen 45', fares (45)
