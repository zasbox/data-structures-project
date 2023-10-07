import pytest

from src.stack import Stack


@pytest.fixture
def stack():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    return stack


def test_push(stack):
    assert stack.top.data == "data3"
    assert stack.top.next_node.data == "data2"
    assert stack.top.next_node.next_node.data == "data1"
    assert stack.top.next_node.next_node.next_node is None
    with pytest.raises(AttributeError):
        data = stack.top.next_node.next_node.next_node.data


def test_pop(stack):
    data = stack.pop()
    assert data == "data3"
    assert stack.top.data == "data2"

