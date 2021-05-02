import os


def repo_root(file):
    return os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), file)
