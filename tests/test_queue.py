from unittest import TestCase

from src.queue import Queue


class TestQueue(TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_enqueue(self):
        self.assertEqual(self.queue.head.data, "data1")
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertIsNone(self.queue.tail.next_node)
        with self.assertRaises(AttributeError):
            data = self.queue.tail.next_node.data

    def test_dequeue(self):
        data = self.queue.dequeue()
        self.assertEqual(data, 'data1')
        self.assertEqual(self.queue.head.data, 'data2')

    def test_str(self):
        self.assertEqual(str(self.queue), "data1\ndata2\ndata3")

