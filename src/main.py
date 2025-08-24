from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from helpers import split_nodes_delimiter

def main():
    node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("This is bold text", TextType.BOLD)
    
    new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
    print(new_nodes)


if __name__ == "__main__":
    main()