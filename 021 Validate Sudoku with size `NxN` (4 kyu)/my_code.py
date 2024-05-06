class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        dimensionality = len(self.data)
        mini_squad_size = int(dimensionality ** 0.5)
        transp_object = [[] for i in range(dimensionality)]
        mini_squad_list = [[] for i in range(dimensionality)]
        try:
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    if type(self.data[i][j]) != int:
                        return False
                    if self.data[i][j] not in range(1, dimensionality + 1):
                        return False
                    transp_object[j].append(self.data[i][j])
                    current_mini_squad = (i // mini_squad_size) * mini_squad_size + (j // mini_squad_size)
                    mini_squad_list[current_mini_squad].append(self.data[i][j])
        except IndexError:
            return False

        for i in range(dimensionality):
            A = len(set(self.data[i]))
            B = len(set(transp_object[i]))
            C = len(set(mini_squad_list[i]))
            if A != dimensionality or B != dimensionality or C != dimensionality:
                return False
        return True
