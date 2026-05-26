from enum import Enum

from textnode import *


def main():
    textnode = Textnode("Hello, World!", Texttype["Plain"], None)
    print(textnode)


main()
