# python3 hashtables/ex5/ex5_tests.py -v


def finder(files, queries):
    cache = {}
    
    for j in files:
        if j not in cache:
            for i in queries:
                if i == j[-len(i):]:
                    cache[j] = 1

    result = list(cache.keys())
                
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
