class Node:
    def __init__(self, square, parent):
        self.parent = parent
        self.square = square
        self.branches = []

    def add_branch(self, new_branch):
        node = Node(new_branch, self)

        repeated = self.is_repeated(new_branch.sqr_id)
        already_added = self.was_already_added(new_branch.sqr_id)

        if not repeated and not already_added:
            self.branches.append(node)

    def is_repeated(self, branch_id):
        parents = [self.square.sqr_id]
        element = self.parent

        while element is not None:
            parents.append(element.square.sqr_id)
            element = element.parent

        for sqr_id in parents:
            if sqr_id == branch_id:
                return True

        return False

    def was_already_added(self, branch_id):
        for branch in self.branches:
            if branch.square.sqr_id == branch_id:
                return True

        return False
