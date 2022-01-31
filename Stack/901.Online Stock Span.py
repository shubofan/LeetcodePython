class StockSpanner:

    def __init__(self):
        self.stack = []

    # monotone stack, price decreasing. Tuple (price, most span at that moment)
    def next(self, price: int) -> int:
        span = 1
        if not self.stack:
            self.stack += [(price, span)]
        else:
            while self.stack and self.stack[-1][0] <= price:
                span += self.stack.pop()[1]
            self.stack += [(price, span)]
        return span

    # for  example: [[],[100],[80],[60],[70],[60],[75],[85]]

    '''
    |       |
    |(60, 1)|
    |(80, 1)|
    |(100,1)|
    |_______|
    
    -> put 70 in stack, pop top of stack
    |       |
    |(70, 2)|
    |(80, 1)|
    |(100,1)|
    |_______|

    |(60, 1)|
    |(70, 2)|
    |(80, 1)|
    |(100,1)|
    |_______|
    
    -> put 75 in stack, before en-stack pop top of stack until top price >75 
    |(75, 4)|
    |(80, 1)|
    |(100,1)|
    |_______|

    -> put 85 in stack, before en-stack pop top of stack until top price > 85
    |(85, 6)|
    |(100,1)|
    |_______|
    
    '''


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
