class Solution:
    def isValid(self, s: str) -> bool:
        
        st=[]

        for i in s:
            if i == '{' or i== '(' or i=='[':
                st.append(i)
            else:
                if len(st)==0:
                    return False
                lastElement=st[-1]
                if i=='}' and lastElement !='{':
                    return False
                elif i==')' and lastElement !='(':
                    return False
                elif i==']' and lastElement !='[':
                    return False
                st.pop()

        if len(st)>0:
            return False
        return True