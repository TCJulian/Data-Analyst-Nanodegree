def question1(s, t):
    """Given two strings, determines whether t is an anagram of s.
    Returns a boolean"""
    if s == "" or t == "":
        return False
    if type(s) is not str or type(t) is not str:
        return False

    s_seq = list(s)
    t_seq = list(t)
    for char in t_seq:
        if char not in s_seq:
            return False
        else:
            s_seq.remove(char)
    return True

print question1("zebra", "bez")
# True
print question1("airplane", "nile")
# True
print question1("hat", "hater")
# False
print question1("racecar", "ceer")
# False
print question1("banana", "")
# False
print question1(1, 2)
# False

def question2(a):
    if type(a) is not str:
        return None
    for view_len in range(len(a), 1, -1):
        view_end = view_len
        view_start = 0
        while view_end <= len(a):
            text = a[view_start:view_end]
            if text == text[::-1]:
                return text
            else:
                view_end += 1
                view_start += 1
    return None

print question2("car")
# None
print question2("tree")
# "ee"
print question2("banana")
# "anana"
print question2("racecar")
# "racecar"
print question2("rodneypicklefoot")
# "oo"
print question2(1221)
# None
print question2("1221")
# "1221"

def question3(G):
    pass

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []

    def insert_node(self, node_value):
        new_node = Node(node_value)
        self.nodes.append(new_node)
        return new_node

    def insert_edge(self, new_edge_value, node_from_val, node_to_val):
        from_node = None
        to_node = None
        for node in self.nodes:
            if node_from_val == node.value:

            if node_to_val == node.value:
                node.edges.append(new_edge)



def question4(T, r, n1, n2):
    pass

def question5(ll, m):
    pass
