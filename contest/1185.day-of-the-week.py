class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        wd = {0: "Sunday", 
              1: "Monday", 
              2: "Tuesday", 
              3: "Wednesday", 
              4: "Thursday", 
              5: "Friday", 
              6: "Saturday"}
        t = [ 0, 3, 2, 5, 0, 3, 
              5, 1, 4, 6, 2, 4 ] 
        y -= m < 3
        return wd[(( y + int(y / 4) - int(y / 100) 
                 + int(y / 400) + t[m - 1] + d) % 7)]
