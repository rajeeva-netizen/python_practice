def swappos(list, pos1, pos2):
  length = len(list)

  if ((pos1 > length-1) or (pos2 > length-1)) :
    return "wrong positions"
  else:
      list[pos1], list[pos2] = list[pos2], list[pos1]

  return list



result = swappos([1,2,4,5,6], 1, 3)

print(result)