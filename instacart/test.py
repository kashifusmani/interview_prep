def add(c,k):
    c.test = c.test + 1
    k = k+1

class Plus:
    def __init__(self):
        self.test = 0

def main():
    p = Plus()
    index = 0
    for i in range(0, 25):
        add(p, index)
    print("p.test=", p.test)
    print("index=", index)

if __name__ == '__main__':
    x = ['ab', 'bc']
    x.insert(1, 'x')
    print(x)

