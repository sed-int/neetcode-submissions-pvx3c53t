class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        st = []

        for i, t in enumerate(temps):
            while st and t > st[-1][0]:
                stT, stI = st.pop()
                res[stI] = i - stI
            st.append((t, i))
        return res
