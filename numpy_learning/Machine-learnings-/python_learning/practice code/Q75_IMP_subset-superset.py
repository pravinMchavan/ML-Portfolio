# 6.	Check if one set is a subset or superset of another and print the result.

def check(set1, set2):
    is_sub = set1.issubset(set2)
    is_sup = set1.issuperset(set2)
    return is_sub, is_sup
print(check({1,2,3},{1,2,3}))