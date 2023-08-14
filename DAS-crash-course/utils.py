from termcolor import colored
from binarytree import build2, Node


TreeNode = Node  # Same naming as in leetcode


def run_test_cases(Solution, test_cases):
    methods = [
        attribute for attribute in dir(Solution)
        if not attribute.startswith("__")
        and callable(getattr(Solution, attribute))
    ]

    for method_name in methods:
        print(f"~~ Testing {method_name} ~~")
        method = getattr(Solution(), method_name)

        for *in_, exp in test_cases:
            in_ = tuple(in_)
            print(f"{in_ = }")
            out = method(**in_[0]) if isinstance(in_[0], dict) else method(*in_)
            if out != exp:
                out = colored(str(out), "red")
            else:
                out = colored(str(out), "green")
            print("out = " + out)
            print(f"{exp = }")
            print("--")


def isValidBST(root) -> bool:
    if isinstance(root, list):
        root = build2(root)

    # print(root)

    def validate(node, lb, ub):
        # Test if current node is within valid limits or raise
        if node.val <= lb or node.val >= ub:
            return False
        left_is_valid = (node.left is None) or validate(node.left, lb=lb, ub=node.val)
        right_is_valid = (node.right is None) or validate(node.right, lb=node.val, ub=ub)
        return left_is_valid and right_is_valid

    return validate(root, float("-inf"), float("+inf"))
