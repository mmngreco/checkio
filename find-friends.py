

def check_connection(network, first, second):
    pairs = [n.split('-') for n in list(network)]
    queue = [first]
    tree = []
    stack = None

    while queue:
        stack = queue.pop(0)

        for i, p in enumerate(pairs):
            if not stack in p: continue
            queue.extend(p)
            tree.extend(pairs.pop(i))
    tree = list(set(tree))

    return second in tree

if __name__ == '__main__':
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."