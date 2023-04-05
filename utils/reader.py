def reader(path):
    dict = {}
    with open(path) as f:
        content = f.readlines()
        nrNodes = int(content[0])
        adj_matrix = []
        for i in range(0, nrNodes):
            adj_matrix.append([int(x) for x in content[i+1].strip("\n").split(",")])
        start = int(content[nrNodes + 1])
        end = int(content[nrNodes + 2])
    dict['noNodes'] = nrNodes
    dict['matrix'] = adj_matrix
    dict['start'] = start
    dict['end'] = end

    return dict


