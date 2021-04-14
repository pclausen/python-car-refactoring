class Tire:

    def __init__(self, brand:str, serialno: str):
        self.serialno = serialno
        self.brand = brand

    def getPressure(self) -> float:
        return 2.4

    def getProfile(self) -> float:
        return 1.7