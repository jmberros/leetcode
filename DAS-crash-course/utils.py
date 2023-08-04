from termcolor import colored


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
