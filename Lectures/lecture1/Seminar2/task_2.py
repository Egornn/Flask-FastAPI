# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# - Для
# n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input())

# answer="{"
# for i in range (1,n):
#     answer+=str(i)+": "+str(3*i+1)+", "      #answer+=1  <=> answer=answer+1
# answer+=str(n)+": "+str(3*n+1)+"}"
# print(answer)

dict = {}
for i in range(1, n + 1):
    dict[str(i) + "-ый элемент"] = 3 * i + 1
print(dict)
