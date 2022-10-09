import os, sys
from plugins import SQL_injection as s

def main():
    myAttack = s.SQL_injector()
    myAttack.run()


if __name__ == "__main__":
    main()