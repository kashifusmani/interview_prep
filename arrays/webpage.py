class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = [homepage]
        self.current_index = 0
        print(self.history)
        print(self.current_index)


    def visit(self, url: str) -> None:
        if self.current_index +1 < len(self.history):
            for i in range(self.current_index+1, len(self.history)):
                del self.history[len(self.history)-1]
        self.history.append(url)
        self.current_index += 1
        print(self.history)
        print(self.current_index)

    def back(self, steps: int) -> str:
        ind = self.current_index
        if steps > ind:
            ind = 0
        else:
            ind = ind - steps
        self.current_index = ind

        print(self.history)
        print(self.current_index)
        return self.history[self.current_index]


    def forward(self, steps: int) -> str:
        ind = self.current_index
        if steps > len(self.history) -1 - ind:
            ind = len(self.history) - 1
        else:
            ind = ind + steps
        self.current_index = ind
        print(self.history)
        print(self.current_index)
        return self.history[self.current_index]


if __name__ == '__main__':

    #["forward","back","back"]
    #[[2],[2],[7]]
# Your BrowserHistory object will be instantiated and called as such:
    obj = BrowserHistory("leetcode.com")
    obj.visit("google.com")
    obj.visit("facebook.com")
    obj.visit("youtube.com")
    obj.back(1)
    obj.back(1)
    obj.forward(1)
    obj.visit("linkedin.com")
    obj.forward(2)
    obj.back(2)
    obj.back(7)

# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)