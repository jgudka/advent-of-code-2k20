from typing import List, Set, Tuple

ACTIVE = '#'
INACTIVE = '.'


class PocketDimension:
    def __init__(self, initialState: List[List[str]]):
        self._currentActiveCubes: Set[Tuple[int, int, int, int]] = set()
        self._previousActiveCubes: Set[Tuple[int, int, int, int]] = set()
        self._bounds = [(-1, len(initialState) + 1), (-1, len(initialState[0]) + 1), (-1, 2), (-1, 2)]
        self._initialiseState(initialState)
    
    def countActiveCubes(self):
        return len(self._currentActiveCubes)
    
    def simulateCycles(self, cycles):
        for i in range(cycles):
            self._simulateCycle()
            self._increaseBounds()
    
    def _initialiseState(self, initialState: List[List[str]]):
        for i in range(len(initialState)):
            for j in range(len(initialState[0])):
                if initialState[i][j] == ACTIVE:
                    self._currentActiveCubes.add((i, j, 0, 0))
    
    def _simulateCycle(self):
        self._copyCurrentActiveCubes()
        for i in range(self._bounds[0][0], self._bounds[0][1]):
            for j in range(self._bounds[1][0], self._bounds[1][1]):
                for k in range(self._bounds[2][0], self._bounds[2][1]):
                    for l in range(self._bounds[3][0], self._bounds[3][1]):
                        self._applyRules((i,j,k,l))
    
    def _applyRules(self, position: Tuple[int, int, int, int]):
        if position in self._previousActiveCubes and self._getSurroundingActiveCubeCount(position) not in [2, 3]:
            self._currentActiveCubes.remove(position)
        elif position not in self._previousActiveCubes and self._getSurroundingActiveCubeCount(position) == 3:
            self._currentActiveCubes.add(position)
    
    def _getSurroundingActiveCubeCount(self, position: Tuple[int, int, int, int]) -> int:
        surroundingActiveCubes = 0
        for i in range(position[0] - 1, position[0] + 2):
            for j in range(position[1] - 1, position[1] + 2):
                for k in range(position[2] - 1, position[2] + 2):
                    for l in range(position[3] - 1, position[3] + 2):
                        if (i, j, k, l) != position and (i, j, k, l) in self._previousActiveCubes:
                            surroundingActiveCubes += 1
        return surroundingActiveCubes
    
    def _increaseBounds(self):
        self._bounds = [
            (self._bounds[0][0] - 1, self._bounds[0][1] + 1),
            (self._bounds[1][0] - 1, self._bounds[1][1] + 1),
            (self._bounds[2][0] - 1, self._bounds[2][1] + 1),
            (self._bounds[3][0] - 1, self._bounds[3][1] + 1),
        ]
    
    def _copyCurrentActiveCubes(self):
        self._previousActiveCubes = self._currentActiveCubes.copy()
    
