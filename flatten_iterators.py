# https://techdevguide.withgoogle.com/resources/former-interview-question-flatten-iterators/#!

# Given an iterator of iterators, implement an interleaving iterator that takes in an iterator of iterators, 
# and emits elements from the nested iterators in interleaved order. That is, if we had the iterators i and j iterating over the elements [ia, ib, ic] 
# and [ja, jb] respectively, the order in which your interleaving iterator should emit the elements would be [ia, ja, ib, jb, ic].

# Your interleaving iterator should implement the Iterator interface, take in the iterator of iterators in its constructor, 
# and provide the next and hasNext methods. Assume that there are no additional methods offered by the iterator.

# Given the following three iterators put into an array of iterators build an “Interleaving Flattener” (IF), which works much like an iterator:

from collections import deque


arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7, 8, 9]
a = iter(arr1)
b = iter(arr2)
c = iter(arr3)
iterlist = [a, b, c]

# To assist you, here’s a skeleton for the class:

class IF:
    def __init__(self, iterlist):
        # TODO: implement with circular linked list or touple
        # a queue works logically, but adds unnecessary overhead when poping/adding to the back
        # instead of caching the entire data, just link the iterators
        self.queue = deque()
        temp_queues = deque()

        for i, iter in enumerate(iterlist):
            temp_queue = deque()
            for e in iter:
                temp_queue.append(e)
            temp_queues.append(temp_queue)
        
        while temp_queues:
            temp_queue = temp_queues.popleft()
            e = temp_queue.popleft()
            self.queue.append(e)
            if temp_queue:
                temp_queues.append(temp_queue)

    def next(self):
        return self.queue.popleft()

    def has_next(self):
        if self.queue: return True

# test
itfl = IF(iterlist)
while itfl.has_next():
    print(itfl.next())
