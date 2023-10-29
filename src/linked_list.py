class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.tail is None:
            self.tail = Node(data, None)
            self.head = self.tail
        else:
            node = self.tail
            self.tail = Node(data, None)
            node.next_node = self.tail

    def to_list(self):
        """Преобразует односвязный список в список типа list"""
        items = []
        node = self.head
        while node:
            items.append(node.data)
            node = node.next_node
        return items

    def get_data_by_id(self, data_id: int):
        """Возвращает элемент списка с заданным id"""
        for item in self.to_list():
            try:
                if item['id'] == data_id:
                    return item
            except TypeError:
                print("Данные не являются словарем или в словаре нет id")

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()
