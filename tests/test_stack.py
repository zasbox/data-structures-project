import unittest

from src.stack import Stack


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')

    def test_push(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertIsNone(self.stack.top.next_node.next_node.next_node)
        with self.assertRaises(AttributeError):
            data = self.stack.top.next_node.next_node.next_node.data

    def test_pop(self):
        data = self.stack.pop()
        self.assertEqual(data,  "data3")
        self.assertEqual(self.stack.top.data, "data2")
