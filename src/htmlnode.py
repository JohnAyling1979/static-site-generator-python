
class HtmlNode:
    def __init__(self, tag = None, value = None, props = None, children = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join([f"{key}=\"{value}\"" for key, value in self.props.items()])
                
class LeafNode(HtmlNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props = props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required for leaf nodes")

        if self.tag is None:
            return self.value

        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, props, children)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required for parent nodes")
        if self.children is None:
            raise ValueError("Children are required for parent nodes")

        if self.props is None:
            return f"<{self.tag}>{self.children_to_html()}</{self.tag}>"

        return f"<{self.tag} {self.props_to_html()}>{self.children_to_html()}</{self.tag}>"

    def children_to_html(self):
        return "".join([child.to_html() for child in self.children])
