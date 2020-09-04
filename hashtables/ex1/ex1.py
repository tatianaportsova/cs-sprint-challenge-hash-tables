# python3 hashtables/ex1/ex1_tests.py -v

def get_indices_of_item_weights(weights, length, limit):
    if length == 1:
        return None

    cache = {}
    for i in range(len(weights)):
      for j in range(len(weights)):
        key1 = tuple([weights[i],weights[j]])
        key2 = tuple([weights[j],weights[i]])
        if key1 and key2 not in cache:
            cache[key1] = weights[i] + weights[j]
   
    result = []
    for key in cache:
        if cache[key] == limit:
            w1 = key[0]
            w2 = key[1]

    for i in range(len(weights)):
        if weights[i] == w1:
            indx1 = i
            i+=1
        if weights[i] == w2:
            indx2 = i
            break

    if indx1 > indx2:
        result.append(indx1)
        result.append(indx2)
    else:
        result.append(indx2)
        result.append(indx1)
    tuple(result)

    return result

# weights = [ 4, 6, 10, 15, 16 ]
# length = 5
# limit = 21

# print(get_indices_of_item_weights(weights, length, limit))
