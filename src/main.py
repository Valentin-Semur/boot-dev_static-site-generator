from textnode import TextNode
from htmlnode import HTMLNode

def main():
    test = HTMLNode(tag="a", value="fasefasf", props={
    "href": "https://www.google.com", 
    "target": "_blank",
    })
    print(test.props_to_html())
    print(test)


main()