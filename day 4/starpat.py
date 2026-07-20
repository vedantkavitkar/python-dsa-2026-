# rows=int(input("enter rows"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# # Pyramid Pattern

# rows = int(input("Enter rows: "))
# for i in range(1, rows + 1):
#     for k in range(rows,i,-1):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# # Hollow Kite Pattern

# rows = int(input("Enter rows: "))

# # ---------- Upper Half ----------
# for i in range(1, rows + 1):

#     # Spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Hollow part
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # ---------- Lower Half ----------
# for i in range(rows - 1, 0, -1):

#     # Spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Hollow part
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # ---------- Bottom Solid Triangle ----------
# for i in range(1, rows):

#     # Spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Stars
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()