def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    d={}

    for i in range(len(weights)):
      if weights[i] in d and weights[i]*2==limit:
        return (i,d[weights[i]])

      d[weights[i]]=i

    for j in d:
      if limit - j in d:
        return (d[limit-j],d[j])
    return None






# weights_3 = [4, 6, 10, 15, 16]

# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)


# print(answer_3)