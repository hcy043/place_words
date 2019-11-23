def place_words(corpus):
    corpus = [x.upper() for x in corpus]
    N = len(corpus[0])
    M = len(corpus)
    grid = [None]*N
    working_index = 1
    grid[0],grid[1] = 0,0
    def is_valid():
        cut_corpus = [corpus[i][:working_index+1] for i in range(M)]
        for i in range(N):#sutun indexi
            curr_column = ""
            for j in range(working_index+1):#satir indexi
                curr_column += corpus[grid[j]][i]
            if curr_column not in cut_corpus: return False
        return True
    def go_to_next(working_index):
        if working_index == 0:
            if grid[working_index] == M-1: return False
            grid[0] += 1
            return True,1
        if grid[working_index] == None:
            grid[working_index] = 0
            return True, working_index
        if grid[working_index] + 1 == M:
            grid[working_index] = 0
            return go_to_next(working_index-1)
        grid[working_index] += 1
        return True, working_index
    while True:
        inc = go_to_next(working_index)
        if inc == False: return False
        else: working_index = inc[1]
        print grid
        if is_valid() == True: 
            if working_index == N - 1: 
                rows = [corpus[grid[i]] for i in range(N)]
                columns = [''.join([corpus[grid[x]][j] for x in range(working_index+1)]) for j in range(N)]
                combine = columns + rows
                flag = True
                for i in combine:
                    if combine.count(i) != 1: 
                        flag = False
                        break
                if flag == True: return [corpus[i] for i in grid]
            if working_index < N-1: working_index += 1
    return corpus
