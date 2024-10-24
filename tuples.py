    #NexusGK__Python___Tuples__
languages = ('python', 'java','javascript')
print(languages)

#accessing elements
print(languages[0])  # prints "python"
print(languages[1])  # prints "java"

#sets
students = {'john', 'ann', 'carol' , 'jovial'}
print(students)
if 'peter' in students:
    print('Peter is a student.')
else:
    print('not present in students')
students.add('vivian')
print(students)
students.update(['dan','alex'])
print(students)
students.remove('carol')
print(students)