def is_leap(x):
  if(x % 400 == 0):
    return True
  elif((x % 4 == 0) and (x % 100 != 0)):
    return True
  else:
    return False


year = int(input())
print(is_leap(year))