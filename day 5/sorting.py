# def bubble(arr,size):
#     for j in range(size):
#         print(f'pass {j}:')
#         for i in range(0,size-1):
#             print(f'IT {i}:',end="")
#             print(arr)
#             if(arr[i+1]<arr[i]):
#                 temp=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=temp
#     return arr

# size=int(input("Enter a size"))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(bubble(arr,size))



# def bubble(arr,size):
#     for j in range(size):
#         flag=False
#         print(f'pass {j}:')
#         for i in range(0,size-1):
#             print(f'IT {i}:',end="")
#             print(arr)
#             if(arr[i+1]<arr[i]):
#                 flag=True
#                 temp=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=temp
#         if flag==False:
#             break
#     return arr

# size=int(input("Enter a size"))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(bubble(arr,size))


def selection(arr,size):
    for j in range(0,size-1):
        min=j
        for i in range(j+1,size):
            if(arr[min]>arr[i]):
                min=i

  #swapping 
    return arr

size=int(input("enter a size"))
arr=[]
for i in range(0,size):
    arr.append(int(input()))
print(selection(arr,size))