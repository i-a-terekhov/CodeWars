def justify(text, width):
    '''
    Iterates through text, calculating 'n' words at a time that would fit in a line.
    Caluculates 'extra' remaining characters that would fit and spreads them throughout the line.
    '''
    text = text.split()
    lengths = [len(word) for word in text]

    output = ''  # end output of text
    while text:
        line_output = ''  # output of text for each line

        n = 1  # number of words in line
        while sum(lengths[0:n + 1]) + n <= width and n < len(text):
            n += 1  # adds more words to line if they would fit and if its not the last word

        extra = width - (sum(lengths[0:n]))  # remaining space in line

        line = [text.pop(0) for _ in range(n)]  # list of words in line, pop used to remove them from text
        del lengths[0:n]  # deletes lengths of used words

        line_output += line[0]  # adds the first word in line
        if len(line) > 1 and text:

            base_space = extra // (len(line) - 1)  # minimum space between words
            n_extra_space = extra % (len(line) - 1)  # number of words with extra space

            # list with spaces between each word in order
            spaces = [' ' * base_space if space >= n_extra_space \
                          else ' ' * (base_space + 1) for space in range(len(line) - 1)]

            for i, space in enumerate(spaces):
                line_output += space + line[i + 1]  # adds remaining words with space in between them

        elif len(line) > 1:
            line_output = ' '.join(line)  # if last line, spacing is normal

        if text:
            line_output += '\n'  # if not last line, add '\n' to end of line

        output += line_output

    return output
