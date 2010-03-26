def main(N):
  sum = 0
  for i in range(N):
    if (divisible(i, 3) or divisible(i, 5)):
      sum += i
  return sum


def divisible(dividend, divisor):
  if dividend % divisor == 0:
    return True
  else: 
    return False 

if __name__ == '__main__':
  N = 1000
  sum = main(N)
  print(sum)
