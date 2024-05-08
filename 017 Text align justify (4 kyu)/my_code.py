def justify(text, width):
    ## breaking down into strings:
    worlds_set = text.split()
    list_new_line = []
    current_substring = ''
    for world in worlds_set:
        if len(current_substring) + 1 + len(world) <= width:
            current_substring = ' '.join([current_substring, world]).lstrip()
        else:
            list_new_line.append(current_substring)
            current_substring = world
    list_new_line.append(current_substring)  ## attaching the last line

    ## consider the length of base spaces and the quantity of extra spaces
    ## the last line - exception
    line_num = 0
    for line in list_new_line[:len(list_new_line) - 1]:
        gaps_in_line = line.count(' ')
        extra_symb_quantity = width - len(line)
        if gaps_in_line != 0:
            base_space_length = 1 + extra_symb_quantity // gaps_in_line
            extra_space_quantity = extra_symb_quantity % gaps_in_line
        else:
            base_space_length = 0
            extra_space_quantity = 0

        ## get the base gap
        base_space = ''
        for i in range(base_space_length):
            base_space += ' '
        extra_space = base_space + ' '

        ## replacing spaces
        list_new_line[line_num] = list_new_line[line_num].replace(' ', base_space)
        list_new_line[line_num] = list_new_line[line_num].replace(base_space, extra_space, extra_space_quantity)

        line_num += 1

    final_text = '\n'.join(list_new_line)
    return final_text
