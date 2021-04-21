import os


class Commander:

    def __init__(self):
        self.command_list = []
        self.create_command_list()

    @staticmethod
    def command(command):
        os.system(command)

    def create_command_list(self):
        filename = "commander/associations.txt"
        file = open(filename, "r", encoding="UTF-8")
        res = file.read().split("\n")
        for data in res:
            data = data.split("@")
            self.command_list.append([data[1], data[0].split(",")])

    def get_command(self, inp):
        for data in self.command_list:

            if inp in data[1]:
                return data[0]

        return None

    def do(self, user_input):
        command = self.get_command(user_input)

        if command is None:
            return "Неверная команда,сука 🤬 не пиши так больше, понял?😎"
        else:
            os.system(command)
            return "Done!"

    @staticmethod
    def compare(name: str, array: list, upper: bool = True) -> bool:
        """
        Сравнивает значение переданного слова со значениями массива. Так же учитваются возможные опечатки,
        но только позиционно. То есть каждая позиция проверяется с соответвующей.

        :param name: проверяемое слово
        :param array: массив, где хранятся возможные значения слова
        :param upper: если истина, то не обращает внимания на регистр, иначе различает
        :return: если хотя бы одно значение с массива совпадает со словом, возращает True, иначе False
        """
        if upper:
            name = name.upper()
            for i in range(len(array)):
                array[i] = array[i].upper()

        for i in array:
            k = 0  # считывание разницы в символах (посимвольно, позиционно)
            if len(i) > len(name):
                for j in range(len(name)):
                    if name[j] == i[j]:
                        pass
                    else:
                        k = k + 1
            else:
                for j in range(len(i)):
                    if i[j] == name[j]:
                        pass
                    else:
                        k = k + 1

            k = k + abs(len(i) - len(name))  # добавление разницы в недостающих символах

            # Обработка возможной опечатки
            if 7 > len(name) > 4 and k < 3:
                return True
            elif 7 <= len(name) < 12 and k < 5:
                return True
            elif len(name) > 11 and k < 7:
                return True
            elif len(name) <= 4 and k < 1:
                return True

        return False

