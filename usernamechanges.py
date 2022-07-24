def possibleChanges(usernames):
    # iterate over the whole list of usernames
    results = []
    for name in usernames:
        length_str = len(name)
        condition = False
        results.append("NO")
        for i,char in enumerate(name[0:length_str-1]):
            for char_compare in name[i+1:length_str]:
                if char_compare < char:
                    results[-1]="YES"
                    condition = True
                    break
            if condition == True:
                break
    return results