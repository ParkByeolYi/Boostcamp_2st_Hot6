# 1541번 | 잃어버린 괄호 | 실버 2

data = input().split('-')
result = 0

for i in range(len(data)):
  # '+'가 있으면 값을 더해서 넣어준다
  data[i] = sum(map(int, data[i].split('+')))
  
  if i > 0:
    result -= data[i]
  elif i == 0:
    result += data[i]

print(result)
