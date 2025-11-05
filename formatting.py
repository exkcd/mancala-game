from color import color


def stat_title(title, buffer):
    print(f"{color.GREEN + color.BOLD}⊰{'Ξ' * buffer}{title}{'Ξ' * buffer}⊱{color.END}")
    #Unicode U+22B1 character for the ⊱ symbol and greek symbol Xi for Ξ which is U+039E

def list_stat(name, stat, int):
    print(f"{name}{stat.rjust(int, ' ')}")
