class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def add(a, b): return a + b
        def sub(a, b): return a - b
        def mul(a, b): return a * b
        def div(a, b): return int(a / b)

        op = {
            "+":add,
            "-":sub,
            "*":mul,
            "/":div
        }
        st = []

        for c in tokens:
            if c in op:
                b = int(st.pop())
                a = int(st.pop())
                val = op[c](a, b)
                print(val)
                st.append(val)
            else:
                st.append(int(c))
        
        return st.pop()