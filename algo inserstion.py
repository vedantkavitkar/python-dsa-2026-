# for i in range(1,size):
#     Temp=arr[i]
#     j=i-1
#     while j>=0 AND Temp<=arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         #after while loop
#         arr[j+1]=Temp

# ---------------------- Insertion Sort ----------------------


# ---------------------- Insertion Sort ----------------------

# def insertion(arr, size):

#     for i in range(1, size):

#         temp = arr[i]
#         j = i - 1

#         while j >= 0 and temp < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = temp

#     return arr


# size = int(input("Enter size: "))

# arr = []

# # Take input for all elements
# for i in range(size):
#     arr.append(int(input()))

# print("Sorted Array:", insertion(arr, size))