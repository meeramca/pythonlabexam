def compare(s1,s2,n):
    list1 = []
    list2 = []
    for i in range(0,n):
        list1.append(s1[i])
        list2.append(s2[i])
    for i in range(0,n):
        if list1 == list2:
            return True
        else:
            return False
s1 = input("enter string 1 : ")
s2 = input("enter string 2 : ")
n= int(input("enter the number upto which check : "))
checking = compare(s1,s2,n)
print("result is ",checking)
