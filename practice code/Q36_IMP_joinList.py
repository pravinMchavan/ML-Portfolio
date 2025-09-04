# 10.Join a list of words into a single string separated by spaces and print it.
def join():

    list1 = ["pra", "vin"]
    list2 = ["ki", "ran"]
    
    newlist = list1 + list2
    sentence = " ".join(newlist)
    print(sentence)

join()