
class Solution:

    def dayOfYear(self, da: str) -> int:

        def is_leap_year(year):
            if year % 100 == 0:
                return year % 400 == 0
            return year % 4 == 0
        
        Y, M, D = int(da.split('-')[0]), int(da.split('-')[1]), int(da.split('-')[2])

        if is_leap_year(Y):
            K = 1
        else:
            K = 2
        N = int((275 * M) / 9.0) - K * int((M + 9) / 12.0) + D - 30
        return N