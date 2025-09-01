from textnode import TextNode, TextType
import re

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
            if (len(sections) % 2 == 0):
                raise ValueError("Invalid text node")
            
            is_text = True
            for section in sections:
                if (is_text):
                    new_nodes.append(TextNode(section, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(section, text_type))
                is_text = not is_text

            
    return new_nodes

"""
Extracts all the images from a text string.
"""
def extract_markdown_images(text):
    images = []
    for image in re.findall(r"!\[(.*?)\]\((.*?)\)", text):
        images.append(image)
    return images

def extract_markdown_links(text):
    links = []
    for link in re.findall(r"\[(.*?)\]\((.*?)\)", text):
        links.append(link)
    return links

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    pass
