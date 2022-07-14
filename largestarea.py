def getMaxArea(w, h, isVertical, distance):
    iterations = len(isVertical) #guess isVertical same lenght as distance
    horizontal_lines = [0,h]
    vertical_lines =[0,w]
    list_areas = []
    for index in range(0,iterations):
        if isVertical[index] == 0: #horizontal
            horizontal_lines.append(distance[index])
        else:
            vertical_lines.append(distance[index])
        #calculate the differences
        horizontal_lines.sort()
        vertical_lines.sort()
        diff_horizontal =[]
        for index in range(1,len(horizontal_lines)):
            diff_horizontal.append(horizontal_lines[index]-horizontal_lines[index-1])
        diff_vertical = []
        for index in range(1,len(vertical_lines)):
            diff_vertical.append(vertical_lines[index]-vertical_lines[index-1])
        #convert to set and then back to remove repeated values
        
        areas = set()
        for diff_h in diff_horizontal:
            for diff_v in diff_vertical:
                areas.add(diff_h*diff_v)
        list_areas.append(max(areas))
        
    return list_areas