# problem statement
"""
detect a loop in a linked list

maintain a dict -> visited
visited -> (data, next)

for every element in linked_list:
    check if present in visited
        true:
            check if node.next.data = visited.get(node.data)
             -> Loop detected

"""
from insertion import LinkedList


def approach_1(lst: LinkedList):
    curr_node = lst.get_head()
    visited = {}
    if curr_node is None:
        return False
    while curr_node:
        if curr_node.data in visited:
            return True
        visited[curr_node.data] = 1
        curr_node = curr_node.next_element
    return False


ll = LinkedList()
ll.insert_at_head(6)
ll.insert_at_head(4)
ll.insert_at_head(7)
ll.insert_at_head(6)
res = approach_1(ll)
print(res)


def floyds_cycle_finding_algorithm(lst):
    onestep = lst.get_head()
    twostep = lst.get_head()

    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element
        twostep = twostep.next_element.next_element

        if onestep == twostep:
            return True
    return False


# Adding a loop
head = ll.get_head()
node = ll.get_head()

for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(floyds_cycle_finding_algorithm(ll))
# print(floyds_cycle_finding_algorithm(ll))
