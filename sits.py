# Модуль для вычисления количества приседаний
from scrollLabel import ScrollLabel

class Sits(ScrollLabel):
    def __init__(self, total, **params):
        self.current = 0
        self.total = total
        text = "Осталось приседаний " +str(self.total)

        super().__init__(text, **params)

    def next(self, *args):
        self.current +=1
        remain = max(0, self.total - self.current)
        text = "осталось приседаний " +str(remain)

        super().set_text(text)