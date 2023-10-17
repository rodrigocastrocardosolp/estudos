class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


def count_nodes(linked_list):
    count = 0
    current = linked_list.head
    while current:
        count += 1
        current = current.next
    return count


# Criando uma lista encadeada e adicionando elementos usando o método append
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Chamando a função count_nodes para contar o número de nós na lista
num_nodes = count_nodes(my_linked_list)

# Imprimindo a lista e o número de nós
current = my_linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

print(f"Número de nós na lista: {num_nodes}")
