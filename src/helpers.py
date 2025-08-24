from textnode import TextNode, TextType

"""
Splits a list of TextNodes into a list of TextNodes, where the delimiter is used to split the text of the TextNodes.
"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
        else:
            sections = node.text.split(delimiter)
            if (len(sections) != 3):
                raise ValueError("Invalid text node")
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(sections[1], text_type))
            new_nodes.append(TextNode(sections[2], TextType.TEXT))

    return new_nodes
