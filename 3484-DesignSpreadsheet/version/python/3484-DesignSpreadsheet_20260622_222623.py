# Last updated: 6/22/2026, 10:26:23 PM
1class Spreadsheet:
2
3    r = 0
4
5    def __init__(self, rows: int):
6        self.cells = {}
7
8    def setCell(self, cell: str, value: int) -> None:
9        self.cells[cell] = value
10
11    def resetCell(self, cell: str) -> None:
12        self.cells.pop(cell, None)
13    
14    def value(self, s: str):
15        if s[0].isalpha(): # check if the first element of cel
16            return self.cells.get(s, 0)
17        else:
18            return int(s) # its a non negative integer
19
20    def getValue(self, formula: str) -> int:
21        a,b = a, b = formula[1:].split("+") # split with +
22        return self.value(a) + self.value(b)
23
24
25# Your Spreadsheet object will be instantiated and called as such:
26# obj = Spreadsheet(rows)
27# obj.setCell(cell,value)
28# obj.resetCell(cell)
29# param_3 = obj.getValue(formula)