import re


def conver_to_list(original_phrase):
    print(original_phrase)
    if re.search(r'^\d+$', original_phrase):
        return ['+', '0', '0']
    if re.search(r'^x$', original_phrase):
        return ['+', 'x', '0']
    match1 = re.search(r'(?<=^\()[^ ]+(?= )', original_phrase)
    match2 = re.search(
        r'(?<=^ )\([^ ]+[ ]?[^ ]+[ ]?[^ ]+\)(?= \(|\)$| \d| )|(?<=^ )[^ ]+(?= |\))',
        original_phrase[match1.end():]
    )
    match3 = re.search(r'.*', original_phrase[match1.end() + match2.end() + 1:-1])

    list_of_phrase = [match1[0], match2[0]]
    if len(match3[0]) > 0:
        list_of_phrase.append(match3[0])

    for i in range(len(list_of_phrase)):
        if re.match(r'\([^ ]*[ ]+', list_of_phrase[i]):
            list_of_phrase[i] = conver_to_list(list_of_phrase[i])

    return list_of_phrase


def definition_of_the_diff_method(list_of_phrase):
    a = list_of_phrase[1]
    diff_a = simple_diff(list_of_phrase[1])

    if len(list_of_phrase) == 3:
        opp = list_of_phrase[0]
        b = list_of_phrase[2]
        diff_b = simple_diff(list_of_phrase[2])

        addition = re.match(r'^[+-]', list_of_phrase[0])
        multiplication = re.match(r'^\*', list_of_phrase[0])
        division = re.match(r'^/', list_of_phrase[0])
        degree = re.match(r'^\^', list_of_phrase[0])

        if addition:
            list_diff_of_phrase = [opp, diff_a, diff_b]
        if multiplication:
            list_diff_of_phrase = ['+', ['*', b, diff_a], ['*', a, diff_b]]
        if division:
            list_diff_of_phrase = ['/', ['-', ['*', diff_a, b], ['*', diff_b, a]], ['^', b, 2]]
        if degree:
            list_diff_of_phrase = ['*', b, ['^', a, ['-', b, '1']]]

    if len(list_of_phrase) == 2:
        sin = re.match(r'^sin', list_of_phrase[0])
        cos = re.match(r'^cos', list_of_phrase[0])
        tan = re.match(r'^tan', list_of_phrase[0])
        exp = re.match(r'^exp', list_of_phrase[0])
        ln = re.match(r'^ln', list_of_phrase[0])

        if sin:
            list_diff_of_phrase = ['*', diff_a, ['cos', a]]
        if cos:
            list_diff_of_phrase = ['*', diff_a, ['*', '-1', ['sin', a]]]
        if tan:
            list_diff_of_phrase = ['/', diff_a, ['^', ['cos', a], '2']]
        if exp:
            list_diff_of_phrase = ['*', diff_a, ['exp', a]]
        if ln:
            list_diff_of_phrase = ['/', '1', a]
    return list_diff_of_phrase


def simple_diff(phrase_element):
    if type(phrase_element) == list:
        return definition_of_the_diff_method(phrase_element)
    else:
        return transformatio_into_a_derivative(phrase_element)


def transformatio_into_a_derivative(phrase_element):
    if re.match(r'^[\d-]+$', phrase_element):
        phrase_element = 'number'
    dict_of_derivatives = {
        'number': '0',
        'x': '1'
    }
    if phrase_element in dict_of_derivatives:
        return dict_of_derivatives[phrase_element]
    else:
        print('not found in the dictionary of derivatives')


def simplifying_a_list_phrase(list_of_phrase):
    simplification_detector = 2
    while simplification_detector > 0 and len(list_of_phrase) > 1:
        simplification_detector -= 1

        list_detector = 0
        for i in range(len(list_of_phrase)):
            if type(list_of_phrase[i]) == list:
                list_of_phrase[i] = simplifying_a_list_phrase(list_of_phrase[i])
                list_detector += 1

        if len(list_of_phrase) == 3:
            b, c = False, False
            if list_detector == 0:
                b = re.match(r'^-?[\d]+$', str(list_of_phrase[1]))
                c = re.match(r'^-?[\d]+$', str(list_of_phrase[2]))
            if b and c:
                list_of_phrase = str(eval(b[0] + str(list_of_phrase[0]).replace('^', '**') + c[0]))
                simplification_detector += 1

        if len(list_of_phrase) == 3:
            simple_dictionary = {
                ('*', '1', str(list_of_phrase[2])): list_of_phrase[2],
                ('*', str(list_of_phrase[1]), '1'): list_of_phrase[1],
                ('*', '0', str(list_of_phrase[2])): '0',
                ('*', str(list_of_phrase[1]), '0'): '0',
                ('+', '0', str(list_of_phrase[2])): list_of_phrase[2],
                ('+', str(list_of_phrase[1]), '0'): list_of_phrase[1],
                ('^', str(list_of_phrase[1]), '1'): list_of_phrase[1],
                ('^', str(list_of_phrase[1]), '0'): '1',
                ('^', '0', str(list_of_phrase[2])): '0'
            }
            if simple_dictionary.get(
                (str(list_of_phrase[0]),
                 str(list_of_phrase[1]),
                 str(list_of_phrase[2]))):
                simplification_detector += 1
            list_of_phrase = simple_dictionary.get(
                (str(list_of_phrase[0]),
                 str(list_of_phrase[1]),
                 str(list_of_phrase[2])), list_of_phrase
            )
    return list_of_phrase


def conver_to_str(list_of_phrase):
    if type(list_of_phrase) == str and re.search(r'^\d+[.]?\d+$', list_of_phrase):
        return list_of_phrase

    answer_phrase = ''
    for i in range(len(list_of_phrase)):
        if type(list_of_phrase[i]) == list:
            answer_phrase += conver_to_str(list_of_phrase[i])
        elif type(list_of_phrase[i]) == str or type(list_of_phrase[i]) == int:
            answer_phrase += str(list_of_phrase[i])
        if i < len(list_of_phrase) - 1:
            answer_phrase += ' '
    if re.search(r' ', answer_phrase):
        answer_phrase = '(' + answer_phrase + ')'
    print(answer_phrase)
    return answer_phrase


def diff(s):
    return conver_to_str(simplifying_a_list_phrase(definition_of_the_diff_method(conver_to_list(s))))

