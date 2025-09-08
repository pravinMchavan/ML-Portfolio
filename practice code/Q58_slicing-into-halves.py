# 7.Slice a list into two halves and print both halves separately.

def halves(a):
    mid = len(a) // 2
    half1 = a[:mid]
    half2 = a[mid:]
    print(f"fist half:{half1}")
    print(f"second half:{half2}")

halves([1,2,3,4,5,6])