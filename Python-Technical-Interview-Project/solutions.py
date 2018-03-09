import pprint

######################
##### Question 1 #####
######################

def question1(s, t):
    """
    Given two strings, returns Boolean whether 't' is an anagram of 's'.

    Arguments:
    s -- string. The string being checked for the anagram.
    t -- string. The potential anagram.
    """
    if s == "" or t == "":
        return False
    if type(s) is not str or type(t) is not str:
        raise TypeError("Variable 's' or 't' is not a string.")

    s_seq = list(s)
    t_seq = list(t)
    for char in t_seq:
        if char not in s_seq:
            return False
        else:
            s_seq.remove(char)
    return True

print "\nQuestion 1:"
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


######################
##### Question 2 #####
######################

def question2(a):
    """
    Find and return the first palindromic substring found in a string.

    Arguments:
    a -- string
    """
    if type(a) is not str:
        raise TypeError("Variable 'a' is not a string.")

    for view_len in range(len(a), 1, -1):
        view_end = view_len
        view_start = 0
        while view_end <= len(a):
            text = a[view_start:view_end].lower()
            if text == text[::-1]:
                return text
            else:
                view_end += 1
                view_start += 1
    return None

print "\nQuestion 2:"
print question2("aa")
# "aa"
print question2("car")
# None
print question2("tree")
# "ee"
print question2("banana")
# "anana"
print question2("BaNaNa")
# "anana"
print question2("racecar")
# "racecar"
print question2("Rodney Picklefinger")
# None
print question2("12321")
# "12321"
print question2(
"abcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzbcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyzabcdfghijklmnopqrstuvwxyz"
)
# None


######################
##### Question 3 #####
######################

def question3(G):
    """
    Create a graph from an adjacency list and find/print the minimum spanning tree.

    Arguments:
    G -- An adjacency list.
    """
    graph = Graph()
    graph.build(G)
    mst = graph.Kruskal_mst()
    pprint.pprint(mst.adjacency_list(), width=60)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node1, node2):
        self.value = value
        self.connections = [node1, node2]

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = self.retrieve_node_names(self.nodes)
        self.edge_names = self.retrieve_edge_names(self.edges)

    def insert_node(self, node_name):
        """Create a node and insert it into graph"""
        new_node = Node(node_name)
        self.nodes.append(new_node)
        self.node_names[node_name] = new_node
        return new_node

    def insert_edge(self, new_edge_value, node1_name, node2_name):
        """
        Create an edge and insert it into graph. If the nodes at the end of the edge do not exist, create them.

        Arguments:
        new_edge_value   -- int/float. The weight-value of the edge.
        node1_name       -- string. The identifier for the first node.
        node2_name       -- string. The identifier for the second node.
        """
        node1 = None
        node2 = None

        # check if nodes with input values exist
        if node1_name in self.node_names:
            node1 = self.node_names[node1_name]
        if node2_name in self.node_names:
            node2 = self.node_names[node2_name]

        # if they don't, create them
        if not node1:
            node1 = self.insert_node(node1_name)
        if not node2:
            node2 = self.insert_node(node2_name)

        # cnsure edge between nodes doesn't already exist
        for edge in self.edges:
            if node1 in edge.connections and node2 in edge.connections:
                return None

        # if edge doesn't exist, create it
        new_edge = Edge(new_edge_value, node1, node2)
        self.edges.append(new_edge)
        self.edge_names[node1.value + node2.value] = new_edge
        node1.edges.append(new_edge)
        node2.edges.append(new_edge)

    def build(self, adj_list):
        """
        Add nodes and edges to graph from adjacency list.

        Expected adjacency list format:
        {'node_name': [(connected_node, edge weight)]}

        Example:
            {'A': [('B', 2)],
             'B': [('A', 2), ('C', 5)],
             'C': [('B', 5)]}
        """
        for node, edges in adj_list.items():
            if len(edges) > 0:
                for edge in edges:
                    self.insert_edge(edge[1], node, edge[0])
            else:
                self.insert_node(node)
        return None

    def remove_edge(self, edge_name):
        """Remove edge from graph"""
        edge = self.edge_names[edge_name]
        node1, node2 = edge.connections
        try:
            self.edges.remove(edge)
            node1.edges.remove(edge)
            node2.edges.remove(edge)
            del self.edge_names[edge_name]
            return True
        except KeyError:
            print "Key Error detected. Can't remove edge."
            raise

    def retrieve_node_names(self, nodes):
        """Create node-name to node dictionary from a list of Node objects"""
        names = {}
        for node in nodes:
            names[node.value] = node
        return names

    def retrieve_edge_names(self, edges):
        """Create edge-name to edge dictionary from a list of Edge objects"""
        names = {}
        for edge in edges:
            node1 = edge.connections[0].value
            node2 = edge.connections[1].value
            names[node1 + node2] = edge
        return names

    def adjacency_list(self):
        """Create an adjacency list of graph"""
        adj_list = {}
        for node in self.nodes:
            edge_list = []
            for edge in node.edges:
                for connection in edge.connections:
                    if connection != node:
                        edge_list.append((connection.value, edge.value))
            adj_list[node.value] = edge_list
        return adj_list

    def clear_visits(self):
        """Reset all node visits to False"""
        for node in self.nodes:
            node.visited = False
        return None

    def dfs(self, start_node):
        """
        Perform a Depth First Search through the graph. Returns a list of nodes seen and if any cycles were detected.

        Arguments:
        start_node -- Node. Starting point for search.
        """
        self.clear_visits()
        seen_list, is_cycle = self.dfs_helper(start_node)
        return seen_list, is_cycle

    def dfs_helper(self, start_node, parent=None, is_cycle=False):
        """
        Recursive function for 'dfs'.

        Description:
        Iterates over all edges in start node, checking if surrounding nodes have been visited or if any cycles are present. Returns a list of nodes seen and if a cycle has been found.

        Arguments:
        start_node  -- Node. Starting point for search.
        parent      -- Node. Parent of start_node. Used to check for cycles.
        is_cycle    -- Boolean. Is only True if cycle present.
        """
        seen_list = [start_node.value]
        start_node.visited = True
        for edge in start_node.edges:
            for connection in edge.connections:
                if connection != start_node:
                    if connection.visited == False:
                        temp_list, is_cycle = self.dfs_helper(connection, start_node, is_cycle)
                        for value in temp_list:
                            seen_list.append(value)
                    else:
                        # Any visited node that's not a parent results in cycle
                        if connection != parent:
                            is_cycle = True
        return seen_list, is_cycle

    def Kruskal_mst(self):
        """Find the minimum spanning tree using Kruskal's algorithm"""
        # Create table of edges sorted by value
        edge_table = [(edge.value, name) for name, edge in self.edge_names.items()]
        edge_table = sorted(edge_table)

        # Create new graph with fresh nodes and no edges
        forest = Graph()
        for node in self.nodes:
            forest.insert_node(node.value)

        # Iterate over table, creating new edges in graph until all nodes
        # are connected or table is empty.
        while len(edge_table) != 0:
            current_edge = edge_table.pop(0)
            node1 = forest.node_names[current_edge[1][0]]
            node1_name, node2_name = current_edge[1]
            forest.insert_edge(current_edge[0], node1_name, node2_name)

            seen_list, is_cycle = forest.dfs(node1)

            if is_cycle == True:  # Remove edge if it creates cycle
                forest.remove_edge(current_edge[1])
            elif len(seen_list) == len(self.nodes):
                break
        return forest

print "\nQuestion 3:"
question3({'A': [('B', 2)],
           'B': [('A', 2), ('C', 5)],
           'C': [('B', 5)]})

#         {'A': [('B', 2)],
#          'C': [('B', 5)],
#          'B': [('A', 2), ('C', 5)]}


question3({'A': [('B', 1), ('C', 2)],
           'B': [('A', 1), ('D', 3)],
           'C': [('A', 2), ('D', 4)],
           'D': [('B', 3), ('C', 4)]})

#         {'A': [('B', 1), ('C', 2)],
#          'C': [('A', 2)],
#          'B': [('A', 1), ('D', 3)],
#          'D': [('B', 3)]}


question3({'D': [('E', 4), ('F', 5), ('I', 3)],
           'E': [('D', 4), ('I', 6)],
           'F': [('I', 3), ('D', 5), ('H', 2)],
           'G': [('I', 9)],
           'H': [('F', 2)],
           'I': [('F', 3), ('G', 9), ('E', 6), ('D', 3)]})

#         {'D': [('I', 3), ('E', 4)],
#          'E': [('D', 4)],
#          'F': [('H', 2), ('I', 3)],
#          'G': [('I', 9)],
#          'H': [('F', 2)],
#          'I': [('D', 3), ('F', 3), ('G', 9)]}


question3({'A': [('B', 5), ('C', 4), ('D', 5), ('G', 7)],
           'B': [('A', 5), ('C', 1)],
           'C': [('A', 4), ('B', 1), ('D', 7)],
           'D': [('A', 5), ('C', 7), ('E', 4)],
           'E': [('D', 4), ('F', 8)],
           'F': [('E', 8), ('G', 3)],
           'G': [('A', 7), ('F', 3)],
           'H': [('I', 3)],
           'I': [('H', 3)],
           'J': []})

#         {'A': [('C', 4), ('D', 5), ('G', 7)],
#          'B': [('C', 1)],
#          'C': [('B', 1), ('A', 4)],
#          'D': [('E', 4), ('A', 5)],
#          'E': [('D', 4)],
#          'F': [('G', 3)],
#          'G': [('F', 3), ('A', 7)],
#          'H': [('I', 3)],
#          'I': [('H', 3)],
#          'J': []}


######################
##### Question 4 #####
######################

def question4(T, r, n1, n2):
    """
    Build binary search tree and find the lowest common ancestor (lca) between two nodes.

    Arguments:
    T   --  Tree matrix.
    r   --  Value of the root Node.
    n1  --  Value of first node for lca.
    n2  --  Value of second node for lca.
    """
    tree = Tree(r)
    tree.build(T, r)
    print tree.LCA(n1, n2)

class Node(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

class Tree(object):
    def __init__(self, root):
        self.nodes = {}
        self.root = self.insert_node(root)

    def insert_node(self, data):
        """Insert node with no parents"""
        new_node = Node(data)
        self.nodes[new_node.data] = new_node

    def insert_left(self, data, parent):
        """Insert node to the left of parent"""
        new_node = Node(data, parent=parent)
        parent.left = data
        self.nodes[new_node.data] = new_node

    def insert_right(self, data, parent):
        """Insert node to the right of parent"""
        new_node = Node(data, parent=parent)
        parent.right = data
        self.nodes[new_node.data] = new_node

    def build(self, m, r):
        """Create binary search tree from tree matrix"""
        self.build_helper(m, r)
        for index, value in enumerate(m): # check for rows with no connections
            if index not in self.nodes.keys():
                self.insert_node(index)

    def build_helper(self, m, val, p=None):
        """
        Recursive build function for 'build'

        Description:
        Iterates over tree matrix to build tree. If current node has a parent, insert it left/right from parent based off BST properties.

        Arguments:
        m   -- Tree matrix.
        val -- Value of the current node.
        p   -- Value of the parent node, if it exists.
        """
        if p or p == 0:
            if val < p:
                self.insert_left(val, self.nodes[p])
            else:
                self.insert_right(val, self.nodes[p])
        for index, value in enumerate(m[val]):
            if value == 1:
                self.build_helper(m, index, val)
        return None

    def LCA(self, n1, n2):
        """
        Find the least common ancestor between two nodes

        Arguements:
        n1 -- Value of first node.
        n2 -- Value of second node.
        """
        n1_parents = self.find_ancestors(self.nodes[n1])
        return self.match_ancestors(self.nodes[n2], n1_parents)

    def find_ancestors(self, node):
        """Create a list of all the ancestors of a node"""
        ancestor_list = []
        if node.parent:
            ancestor_list.append(node.parent)
            for value in self.find_ancestors(node.parent):
                ancestor_list.append(value)
        return ancestor_list

    def match_ancestors(self, node, ancestor_list):
        """Return matching ancestor between node and ancestor list"""
        if node.parent:
            if node.parent not in ancestor_list:
                return self.match_ancestors(node.parent, ancestor_list)
            else:
                return node.parent.data
        return None

print "\nQuestion 4:"
question4([[0, 0, 0],
           [1, 0, 1],
           [0, 0, 0]],
          1,
          0,
          2)
# 1

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
# 3

question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
          7,
          0,
          5)
# 2


######################
##### Question 5 #####
######################

def question5(ll, m):
    """
    Given a LinkedList, find the value 'm' elements away from the last element in the list.

    Arguments:
    ll -- A LinkedList object.
    m  -- integer. Number of elements from the end of the linked list.
    """
    print ll.find_element(m)

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(object):
    def __init__(self, values=None):
        self.nodes = []
        self.head = None
        if values:
            self.build(values)

    def build(self, values):
        """Create a linked list from a list of values"""
        self.head = Node(values[0])
        self.nodes.append(self.head.data)
        prev = self.head
        for element in values[1:]:
            new_node = Node(element)
            self.nodes.append(new_node.data)
            prev.next = new_node
            prev = new_node

    def find_element(self, pos):
        """Return element 'pos' elements from end of list"""
        current_pos = 1
        wanted_pos = len(self.nodes) - (pos - 1)
        node_current = self.head
        while current_pos != wanted_pos:
            node_current = node_current.next
            current_pos += 1
        return node_current.data

print "\nQuestion 5:"
question5(LinkedList([1, 2, 3]), 1)
# 3

question5(LinkedList(["A", "B", "C", "D", "E", "F"]), 4)
# 'C'

question5(LinkedList([None, 2, "A", None]), 4)
# None
