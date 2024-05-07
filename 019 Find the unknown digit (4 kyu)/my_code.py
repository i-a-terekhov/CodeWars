import re


def solve_runes(runes):
    for i in range(10):
        new_runes = runes.replace('?', str(i))
        expression_total = re.split("=", new_runes)
        char_between = re.findall("[-|+|*]", expression_total[0][1:])[0]
        char_between_ind = expression_total[0].find(char_between, 1)
        num_one = expression_total[0][:char_between_ind]
        num_two = expression_total[0][char_between_ind + 1:]
        char_valid = True
        for j in (num_one, num_two, expression_total[1]):
            if runes.find(str(i)) > -1:
                char_valid = False
                break
            if len(re.findall(r'(-0|\b0\d)', j)) > 0:
                char_valid = False
                break

        if char_valid:
            if eval(expression_total[0]) == eval(expression_total[1]):
                return i
    return -1
