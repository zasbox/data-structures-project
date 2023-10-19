"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from unittest import TestCase

from src.linked_list import LinkedList


class TestLinkedList(TestCase):
    def setUp(self) -> None:
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})

        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.tail.data, {'id': 1})

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 2})
        self.assertEqual(self.ll.tail.data, {'id': 2})

        self.ll.insert_at_end({'id': 3})
        self.assertEqual(self.ll.tail.data, {'id': 3})

    def test_str(self):
        self.assertEqual(str(self.ll), "None")

        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})

        self.assertEqual(str(self.ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
