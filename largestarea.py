def getMaxArea(w, h, isVertical, distance):
    iterations = len(isVertical) #guess isVertical same lenght as distance
    horizontal_lines = {0,h}
    vertical_lines = {0,w}
    for index in range(0,iterations):
        if isVertical[index] == 0: #horizontal
            horizontal_lines.add(distance[index])
        else:
            vertical_lines.add(distance[index])
        #calculate the differences
        difference = {}
        for index in range(1,len(horizontal_lines)):
            difference.add(horizontal_lines[index]-horizontal_lines[index-1])