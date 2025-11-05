from color import color


def stat_title(title, buffer):
    print(f"{color.GREEN + color.BOLD}{"=":=<{buffer}}{title}{"=":=<{buffer}}{color.END}")


def list_stat(name, stat, int):
    print(f"{name}{stat.rjust(int, ' ')}")
