class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=set('+-*/')
        l=[]
        for c in tokens:
            if c=='+':
                l.append(l.pop()+l.pop())
            elif c=='-':
                a, b = l.pop(), l.pop()
                l.append(b-a)
            elif c=='*':
                l.append(l.pop()*l.pop())
            elif c=='/':
                b,a= l.pop(), l.pop()
                l.append(int(float(a)/b))
            else:
                l.append(int(c))
        
        return l.pop()