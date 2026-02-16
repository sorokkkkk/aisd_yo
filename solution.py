from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        need = [0] * n

        l_max = 0
        i = 0
        while i < n:
            cur_h = height[i]

            if cur_h > l_max:
                l_max = cur_h

            need[i] = l_max - cur_h
            i += 1

        total_water = 0
        r_max = 0

        j = n - 1
        while j >= 0:
            cur_h = height[j]

            if cur_h > r_max:
                r_max = cur_h

            r_cont = r_max - cur_h

            if need[j] < r_cont:
                add_water = need[j]
            else:
                add_water = r_cont

            if add_water > 0:
                total_water += add_water

            j -= 1

        return total_water
