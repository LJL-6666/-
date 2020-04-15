score = float(input('input the score:'))
if score >= 90:
    grade = '优秀'
elif score >= 80:
    grade = '良好'
elif score >= 70:
    grade = '优秀'
elif score >= 60:
    grade = '及格'
else:
    grade = '不及格'
print('the grade is :',grade)
