class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def stat_title(title, buffer):
    print(f"{color.GREEN + color.BOLD}⊰{'Ξ' * buffer}{title}{'Ξ' * buffer}⊱{color.END}")
    #Unicode U+22B1 character for the ⊱ symbol and greek symbol Xi for Ξ which is U+039E

def list_stat(name, stat, int):
    print(f"{name}{stat.rjust(int, ' ')}")
