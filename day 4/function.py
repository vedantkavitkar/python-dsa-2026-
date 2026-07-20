#FUNCTIONS 

# def diff(start,end,num):
# divsum=0
# nondivsum=0
# for i in range(start,end+1)
#      if i%num==0:
#           divsum+=i
# def    else:
#         nondivsum+=i
# diff=abs(divsum-nondivsum)
# #print(divsum,nondivsum)
# return diff 

# def demo(str1):
#     str2=""
#     for i in str1:
#      if i not in str2:
#         if str1.count(i)>1:
#             str2+=i
#             str2+=str(str1.count(i))
#         else:
#             str2+=i
#     print(str2)

# str1=input("enter")
# demo(str1)


def demo(*args):
    c = 0
    for i in args:
        c += i
    return c
print(demo(30,20,30,70))