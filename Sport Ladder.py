class Repetition:
    def __init__(self):
        self.repetition = 0
        self.repetition_max = 0

    def get_repetition(self):
        self.repetition = int(input('Введите максимум: '))

    def repetition_calculate(self):
        for i in range(1, self.repetition+1):
            while True:
                next_repetition = input(f'Сейчас нужно сделать: {i}\nВведите точку, чтобы продолжить: ')
                if next_repetition == '.':
                    self.repetition_max += i
                    break
                else:
                    print('Введите точку')
            

        for i in range(self.repetition, 0, -1):
            while True:
                next_repetition = input(f'Сейчас нужно сделать: {i}\nВведите точку, чтобы продолжить: ')
                if next_repetition == '.':
                    self.repetition_max += i
                    break
                else:
                    print('Введите точку')

    def repetition_print(self):
        print(f'Сделано: {self.repetition_max}')

if __name__ == '__main__':
    app = Repetition()
    app.get_repetition()
    app.repetition_calculate()
    app.repetition_print()
