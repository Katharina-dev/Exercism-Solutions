def rectangles(strings):
    count = 0
    for a in range(len(strings)):
        for b in range(len(strings[0])):
            if strings[a][b] == "+":
                for c in range(a+1,len(strings)):
                    if strings[c][b] =="+":
                        for d in range(b+1,len(strings[0])):
                            if strings[a][d] == "+" and strings[c][d] == "+":
                                    sides_vert1 = [strings[i][b] for i in range(a,c)]
                                    sides_vert2 = [strings[i][d] for i in range(a,c)]
                                    sides_hor1 = [strings[a][i] for i in range(b,d)]
                                    sides_hor2 = [strings[c][i] for i in range(b,d)]
                                    sides_vert = [i for i in sides_vert1 + sides_vert2 if i in ' -']
                                    sides_hor = [i for i in sides_hor1 + sides_hor2 if i in ' |']
                                    if not sides_vert and not sides_hor:
                                        count += 1
    return count


