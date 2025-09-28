# Merge two dictionaries and print the result.
def iterate():
    student1 = {'name1':'pravin', 'std1':'9', 'school1':'ckt'}
    student2 = {'name2':'kiran', 'std2':'8', 'school2':'bckt'}
    student1.update(student2)
    print(student1)
iterate()