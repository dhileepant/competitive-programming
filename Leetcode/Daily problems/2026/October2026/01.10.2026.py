class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in '({[':
                st.append(i)
            else:
                if not st:
                    return False
                if i == ')' and st[-1] != '(':
                    return False
                elif i == '}' and st[-1] != '{':
                    return False
                elif i == ']' and st[-1] != '[':
                    return False
                else:
                    st.pop()
        if st:
            return False
        return True
