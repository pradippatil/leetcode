# -*- coding: utf-8 -*-

"""Circular Queue
https://leetcode.com/problems/design-circular-queue/

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.

"""


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.q[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.q[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == -1 and self.rear == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.size <= 0:
            return True
        return self.front == (self.rear + 1) % self.size


if __name__ == '__main__':
    cq = MyCircularQueue(3)
    print(cq.enQueue(1))  # // return true
    print(cq.__dict__)
    print(cq.enQueue(2))  # // return true
    print(cq.__dict__)
    print(cq.enQueue(3))  # // return true
    print(cq.__dict__)
    print(cq.enQueue(4))  # // return false, the queue is full
    print(cq.__dict__)
    print(cq.Rear())  # // return 3
    print(cq.isFull())  # // return true
    print(cq.deQueue())  # // return true
    print(cq.__dict__)
    print(cq.Front())
    print(cq.enQueue(4))  # // return true
    print(cq.__dict__)
    print(cq.Rear())  # // return 4

