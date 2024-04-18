# Музичний інструмент
class MusicalInstrument:
    def name(self):
        pass


###


# Бубон
class Trumpet(MusicalInstrument):
    def name(self):
        return "Бубон"


# Барабан
class Drum(MusicalInstrument):
    def name(self):
        return "Барабан"


# Тромбон
class Tambourine(MusicalInstrument):
    def name(self):
        return "Тромбон"


# Флейта
class Flute(MusicalInstrument):
    def name(self):
        return "Флейта"


# Орган
class Organ(MusicalInstrument):
    def name(self):
        return "Орган"


# Гармоніка
class Harmonica(MusicalInstrument):
    def name(self):
        return "Гармоніка"


# Баян
class Banjo(MusicalInstrument):
    def name(self):
        return "Баян"


# Рояль
class Harp(MusicalInstrument):
    def name(self):
        return "Рояль"


###


# Ударні
class Strike(Trumpet, Drum):
    pass


# Духові
class Percussion(Tambourine, Flute, Organ):
    pass


# Клавішні
class Keyboard(Harmonica, Banjo, Harp):
    pass


###

# Виведе "Бубон", тому що Trumpet є першим класом від якого наслідується Strike
print(Strike().name())

# Виведе "Тромбон", тому що Tambourine є першим класом від якого наслідується Percussion
print(Percussion().name())

# Виведе "Гармоніка", тому що Harmonica є першим класом від якого наслідується Keyboard
print(Keyboard().name())
