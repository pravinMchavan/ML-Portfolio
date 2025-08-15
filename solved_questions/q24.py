# Check if three sides can form a triangle (sum of any 2 sides > third).

side1 = int(input("side 1 ="))
side2 = int(input("side 2 ="))
side3 = int(input("side 3 ="))

if (side1 + side2) > side3 and (side1 + side3) > side2 and (side3 + side2) > side1:
    print("It can form tringle")
else:
    print("It can not form tringle")