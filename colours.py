#To use, just do c.red("text")

#writes dark grey text
def grey(text):
    print("\033[1;30;48m" + str(text) + "\033[1;37;48m")

#writes red text
def red(text):
    print("\033[1;31;48m" + str(text) + "\033[1;37;48m")

#writes green text
def green(text):
    print("\033[1;32;48m" + str(text) + "\033[1;37;48m")

#writes yellow text
def yellow(text):
    print("\033[1;33;48m" + str(text) + "\033[1;37;48m")

#writes dark blue text
def blue(text):
    print("\033[1;34;48m" + str(text) + "\033[1;37;48m")

#writes magenta text
def pink(text):
    print("\033[1;35;48m" + str(text) + "\033[1;37;48m")

#writes cyan text
def cyan(text):
    print("\033[1;36;48m" + str(text) + "\033[1;37;48m")
