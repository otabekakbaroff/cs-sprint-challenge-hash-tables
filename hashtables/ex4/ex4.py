def has_negatives(a):
    """
        YOUR CODE HERE
    """
    result=[]
    # Your code here
    a.sort()
    negatives={}
    for i in range(len(a)):
      if a[i] not in negatives and a[i] < 0:
        negatives[a[i]]=i
      elif a[i]*-1 in negatives:
        result.append(a[i])

    return result
#change is here
a
if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
