def filter_list(l):  # noqa: E741
    list = []
    
    for element in l:
        if type(element) is not str:
            list.append(element)
            
    return list