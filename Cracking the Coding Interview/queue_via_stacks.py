# Question 3.4

# class methods: add (to the tail), remove (from the head)

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def __repr__(self) -> str:
        string_builder = []
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        while len(self.stack2) > 0:
            temp = self.stack2.pop()
            string_builder.append(temp)
            self.stack1.append(temp)

        return "".join(string_builder)

    
    def add(self, input):
        if len(self.stack2) > 0:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())

        self.stack1.append(str(input))

    def remove(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
        else:
            return self.stack2.pop()

        return self.stack1.pop()


test_queue = Queue()
test_queue.add(1)
test_queue.add(2)
test_queue.add(3)
test_queue.add(4)
x = test_queue.remove()
test_queue.add(5)
assert x == "1", f"x: {x}"
assert test_queue == "2345", f"test_queue: {test_queue}"  # TODO: why does this throw an error?
