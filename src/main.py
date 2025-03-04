from textnode import *

def main():
    testNode = TextNode("Test text", TextType.LINK, "https://boot.de")
    print(testNode.__repr__())

main()
