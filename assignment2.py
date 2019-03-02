from random import randint


def solve_csp(nodes, arcs, max_steps):
    node_values = min_conflict(nodes, arcs, max_steps)
    return node_values


def min_conflict(nodes, arcs, max_steps):
    num_conflicts = []
    current = initialize_list(nodes)
    for step in range(1, max_steps+1):
        if is_solution(nodes, arcs, current):
            print('Total Steps: ' +str(step))
            return current
        var = rand_select_cspnode(nodes, arcs, current)
        for v in range(10):
            if not v == current[var]:
                v_conflict = conflicts(var, v, current, nodes, arcs)
                num_conflicts.append(v_conflict)
        value = num_conflicts.index(min(num_conflicts))
        current[var] = value
        num_conflicts = []
    return "Wasn't able to find solution within max_steps"


def conflicts(var, v, current, nodes, arcs):
    temp = [c for c in current]
    temp[var] = v
    num_c_violated = 0
    neighbors = find_neighbors(var, arcs)
    neighbors.append(var)
    for neighbor in neighbors:
        if temp[var] == 0:
            num_c_violated += 1
        if nodes[neighbor] == 'T':
            if not check_t(var, arcs, temp):
                num_c_violated += 1
        elif nodes[neighbor] == 'S':
            if not check_s(var, arcs, temp):
                num_c_violated += 1
        elif nodes[neighbor] == 'P':
            if not check_p(var, arcs, temp):
                num_c_violated += 1
        elif nodes[neighbor] == 'H':
            if not check_h(var, arcs, temp):
                num_c_violated += 1
    return num_c_violated


def find_neighbors(var, arcs):
    neighbors = []
    for arc in arcs:
        if arc[0] == var:
            neighbors.append(arc[1])
        elif arc[1] == var:
            neighbors.append(arc[0])
    return neighbors


def is_solution(nodes, arcs, current):
    bool = True
    for node in nodes:
        if node == 'T':
            bool = check_t(nodes.index(node), arcs, current)
            if not bool:
                break
        elif node == 'S':
            bool = check_s(nodes.index(node), arcs, current)
            if not bool:
                break
        elif node == 'P':
            bool = check_p(nodes.index(node), arcs, current)
            if not bool:
                break
        elif node == 'H':
            bool = check_h(nodes.index(node), arcs, current)
            if not bool:
                break
    if bool:
        return True
    else:
        return False


def check_t(var, arcs, current):
    product = 1
    neighbors = find_neighbors(var, arcs)
    for neighbor in neighbors:
        product = product*current[neighbor]
    number = str(product)
    l_digit = int(number[0])
    if l_digit == current[var]:
        return True
    else:
        return False


def check_s(var, arcs, current):
    product = 1
    neighbors = find_neighbors(var, arcs)
    for neighbor in neighbors:
        product = product*current[neighbor]
    r_digit = product % 10
    if r_digit == current[var]:
        return True
    else:
        return False


def check_p(var, arcs, current):
    sum = 0
    neighbors = find_neighbors(var, arcs)
    for neighbor in neighbors:
        sum = sum+current[neighbor]
    r_digit = sum % 10
    if r_digit == current[var] :
        return True
    else:
        return False


def check_h(var, arcs, current):
    sum = 0
    neighbors = find_neighbors(var, arcs)
    for neighbor in neighbors:
        sum = sum+current[neighbor]
    number = str(sum)
    l_digit = int(number[0])
    if l_digit == current[var]:
        return True
    else:
        return False


def rand_select_cspnode(nodes, arcs, current):
    cspnode = []
    for node in nodes:
        if node == 'T':
            bool = check_t(nodes.index(node), arcs, current)
            if not bool:
                cspnode.append(node)
        elif node == 'S':
            bool = check_s(nodes.index(node), arcs, current)
            if not bool:
                cspnode.append(node)
        elif node == 'P':
            bool = check_p(nodes.index(node), arcs, current)
            if not bool:
                cspnode.append(node)
        elif node == 'H':
            bool = check_h(nodes.index(node), arcs, current)
            if not bool:
                cspnode.append(node)
    node = randint(0, len(cspnode))
    return node


def initialize_list(nodes):
    shapes = list(nodes)
    values = []
    for shape in shapes:
        value = randint(1, 9)
        values.append(value)
    return values


nodes = 'CHTPS'
arcs = [(0,1), (0,2), (1,2), (1,3), (1,4), (2,3), (2,4)]
max_steps = 1000
print(solve_csp(nodes, arcs, max_steps))
