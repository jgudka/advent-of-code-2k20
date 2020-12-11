EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


class SeatingArrangment2:
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
        surroundingVisibleSeats = self._getSurroundingVisibleSeats(row, col)
        if seat == EMPTY and surroundingVisibleSeats.count(OCCUPIED) == 0:
            self._currentSeats[row][col] = OCCUPIED
        elif seat == OCCUPIED and surroundingVisibleSeats.count(OCCUPIED) >= 5:
            self._currentSeats[row][col] = EMPTY
        else:
            self._currentSeats[row][col] = seat
    
    def _getSurroundingVisibleSeats(self, row, col):
        directionVectors = [
            [-1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
        ]
        return [self._findSeatInDirection(row + direction[0], col + direction[1], direction) for direction in directionVectors]
    
    def _findSeatInDirection(self, row, col, direction):
        seat = FLOOR
        while seat == FLOOR and self._seatIsInBounds(row, col):
            seat = self._previousSeats[row][col]
            row += direction[0]
            col += direction[1]

        return seat
    
    def _seatIsInBounds(self, row, col):
        return 0 <= row <= self._rowCount - 1 and 0 <= col <= self._columnCount -1
    
    def _copyCurrentSeats(self):
        self._previousSeats = [row[:] for row in self._currentSeats]
    
    def _stateChanged(self):
        return self._currentSeats != self._previousSeats
