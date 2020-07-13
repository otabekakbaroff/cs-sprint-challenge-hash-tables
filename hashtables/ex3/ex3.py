def intersection(arrays):
  obj={}
  result=[]
  for i in range(len(arrays)):
    for j in range(len(arrays[i])):
      if arrays[i][j] not in obj:
        obj[arrays[i][j]]=1
      else:
        obj[arrays[i][j]]=obj[arrays[i][j]]+1

      if obj[arrays[i][j]]==len(arrays):
        result.append(arrays[i][j])
    

  return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
