def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num) + args[i]
    print(str)
p(",", 3, "♡", "*")
p("a", 2, "♡", "*", "/")
p("_", 3, "♡", "*", "/", "/")
