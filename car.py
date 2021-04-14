from typing import Dict, List
from tire import Tire


class Car:

    er: bool = False
    seats: Dict[str, bool] = {}
    owner: str
    allTire: List[Tire]

    engineContolLempOil: bool
    engineType: str = 'GASOLINE'
    engineControlLampPreIgnited: bool

    def __init__(self):
        pass

    def se(self) -> bool:
        if self.engineContolLempOil == False and (self.engineType == 'DIESEL' and self.engineControlLampPreIgnited == True) or self.engineType == 'GASLOINE':
            self.er = True
        else:
            self.er = False

        return self.er

    def state(self) -> str:
        message = 'ready for use'
        if not self.er:
            return 'not ' + message
        else:
            return message

    def occupySeat(self, string: str, buddy: str):
        seatIsOccupiedUpFromNow = True
        self.seats[string] = seatIsOccupiedUpFromNow

    def numberOfPassengers(self) -> int:
        a = 0
        for seat, seatState in self.seats:
            if seatState:
                a+=1
        return a

    def setOwner(self, string: str):
        self.occupySeat("Driverseat", string)
        return True

    def changeTireWhereIntPMeansPositionSeenFromLeftFrontClockwise(self, newTire: Tire, p: int):
        self.allTire[p] = newTire

    def getTire(self, position: str) -> Tire:
        if position == "left front":
            return self.allTire[0]
        return None

    def checkTire(self, tire: str) -> str:
        return "OK" if self._isTirePressureOk(self.getTire(tire)) and self.getTire(tire).getProfile() > 1.5 else "NOK"

    def _isTirePressureOk(self, tire: Tire) -> bool:
        return tire.getPressure() == 2.4
