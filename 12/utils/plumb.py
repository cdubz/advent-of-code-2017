def plumb(pipes, parent, connections, plumbed):
    connections.append(parent)
    plumbed.append(parent)
    for child in pipes[parent]:
        if child not in plumbed:
            connections.append(child)
            plumbed.append(child)
            plumb(pipes, child, connections, plumbed)
    return connections
