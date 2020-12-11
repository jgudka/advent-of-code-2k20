EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


class SeatingArrangment:
    def __init__(self, seats):
        self._currentSeats = seats
        self._previousSeats = []
        self._rowCount = len(seats)
        self._columnCount = len(seats[0])
    
    def simulate(self):
        while self._stateChanged():
            self._modelRound()

    def countOccupiedSeats(self):
        return sum(''.join(row).count(OCCUPIED) for row in self._currentSeats)
    
    def _modelRound(self):
        self._copyCurrentSeats()
        for row in range(self._rowCount):
            for col in range(self._columnCount):
                self._applyRules(row, col)
    
    def _applyRules(self, row, col):
        seat = self._previousSeats[row][col]
        surroundingSeats = self._getSurroundingSeats(row, col)
        if seat == EMPTY and surroundingSeats.count(OCCUPIED) == 0:
            self._currentSeats[row][col] = OCCUPIED
        elif seat == OCCUPIED and surroundingSeats.count(OCCUPIED) >= 4:
            self._currentSeats[row][col] = EMPTY
        else:
            self._currentSeats[row][col] = seat
    
    def _getSurroundingSeats(self, row, col):
        topRow = row - 1
        bottomRow = row + 1
        leftCol = col - 1
        rightCol = col + 1
        surroundingSeats = list()
        for i in range(max(0, topRow), min(self._rowCount - 1, bottomRow) + 1):
            for j in range(max(0, leftCol), min(self._columnCount - 1, rightCol) + 1):
                if not(i == row and j == col):
                    surroundingSeats.append(self._previousSeats[i][j])
        return surroundingSeats
    
    def _copyCurrentSeats(self):
        self._previousSeats = [row[:] for row in self._currentSeats]
    
    def _stateChanged(self):
        return self._currentSeats != self._previousSeats
