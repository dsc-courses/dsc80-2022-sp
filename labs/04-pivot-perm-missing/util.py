import inspect
import re


def check_loops(func):

    # check for loops in function
    src = inspect.getsource(func)
    src = re.sub('\s*#.*', '', src)
    src = src.replace("\n", "\t")
    src = re.sub('""".+"""', "", src)
   
    cond = False
    m = re.search(r"(?:for \S+ in )|(?:while \S+:)", src)
    if m is not None:
        msg = "Did you use a loop? You shouldn't!"
        print(msg)
        cond = True

    return cond
