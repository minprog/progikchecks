import check50
import check50.uva.python as python
import re

PUZZLE1 = [[7,9,0,0,0,0,3,0,1],
    [0,0,0,0,0,6,9,0,0],
    [8,0,0,0,3,0,0,7,6],
    [0,0,0,0,0,5,0,0,2],
    [0,0,5,4,1,8,7,0,0],
    [4,0,0,7,0,0,0,0,0],
    [6,1,0,0,9,0,0,0,8],
    [0,0,2,3,0,0,0,0,0],
    [0,0,9,0,0,0,0,5,4]]

@check50.check()
def notebook_exists():
    """sudoku.ipynb exists"""
    check50.exists("sudoku.ipynb")
    python.convert_notebook("sudoku.ipynb")

@check50.check(notebook_exists)
def load_exists():
    """contains load function"""
    python.load("sudoku.py").has("load")

@check50.check(load_exists)
def loads_puzzle1():
    """loads puzzle1 correctly"""
    result = python.load("sudoku.py").call("load", "puzzle1.sudoku").return_value
    if result != PUZZLE1:
        raise python.Mismatch(PUZZLE1, result)

@check50.check(loads_puzzle1)
def show_exists():
    """contains show function"""
    python.load("sudoku.py").has("show")

@check50.check(show_exists)
def shows_puzzle1():
    """shows puzzle1 correctly"""
    expect_str = \
        "7 9 _   _ _ _   3 _ 1\n" +\
        "_ _ _   _ _ 6   9 _ _\n" +\
        "8 _ _   _ 3 _   _ 7 6\n" +\
        "\n" +\
        "_ _ _   _ _ 5   _ _ 2\n" +\
        "_ _ 5   4 1 8   7 _ _\n" +\
        "4 _ _   7 _ _   _ _ _\n" +\
        "\n" +\
        "6 1 _   _ 9 _   _ _ 8\n" +\
        "_ _ 2   3 _ _   _ _ _\n" +\
        "_ _ 9   _ _ _   _ 5 4"

    # allow for arbitrary whitespace at end of line
    expect_regex = "".join(f"({line})[ \t]*\n" for line in expect_str.split("\n"))
    expect_regex = re.compile(expect_regex, re.MULTILINE)

    out = python.load("sudoku.py").call("show", PUZZLE1).stdout
    if not re.match(expect_regex, out):
        raise python.Mismatch(expect_str, out)
