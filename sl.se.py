def fares(age, student=False, senior=False):
    #print age,student,senior
    if age <=20:
        return 'halv'
    elif age >= 65:
        return 'halv'
    else:
         return 'hel'




print 'barn 12',fares (12)
print 'pension 65',fares (65)
print 'student 20',fares (20)
print 'vuxen 45',fares (45)
