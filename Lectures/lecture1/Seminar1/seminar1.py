list = []
maxx = int(input(f"Input the 1th number: "))
list.append(maxx)
n = 5
for i in range(1, n):
    print(list)
    list.append(int(input(f"Input the {i + 1}th number: ")))
    if list[i] > maxx:
        maxx = list[i]

# maxx = int(input(f"Input the 1th number: "))
# for i in range(1, 5):
#     temp = int(input(f"Input the {i+1}th number: "))
#     if temp > maxx:
#         maxx = temp
print(maxx)
