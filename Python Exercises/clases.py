class Galleta():
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta")
    def chocolatear(self):
        self.chocolate = True

una_galleta = Galleta()
una_galleta.chocolatear()
print(una_galleta.chocolate)
