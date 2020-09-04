# python3 hashtables/ex4/ex4_tests.py -v

def has_negatives(a):
    cache = {}
    for i in a:
        if i not in cache:
            cache[i] = abs(i)

    
    dict_ = {}
    for key1,value1 in cache.items():
        if key1 not in dict_:
            for key2,value2 in cache.items():
                if key2 not in dict_:
                    if value1 == value2:
                        if key1 != key2:
                            if key1 > key2:
                                # if key1 not in dict_:
                                dict_[key1] = 1
                            else:
                                dict_[key2] = 1
                            break
    
    result = list(dict_.keys())

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
