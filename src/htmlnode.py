class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise (NotImplementedError("to_html method is not implemented"))

    def props_to_html(self):
        if self.props is None:
            return ""
        HTML_props = ""
        for key in self.props:
            HTML_props += f" {key}='{self.props[key]}'"
        return HTML_props

    def __repr__(self) -> str:
        return f"<{self.tag} {self.props_to_html()}> {self.value}, {self.children} </{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value cannot be None")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"leafnode({self.tag} {self.value} [{self.props}])"


class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, prop=None):
        super().__init__(tag, children=children, props=prop)

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tags")
        if self.children is None:
            raise ValueError("no children")

        return f"<{self.tag}>{self.call_child_to_html()}</{self.tag}>"

    def call_child_to_html(self):
        child_string = ""
        for i in self.children:
            child_string += i.to_html()
        return child_string
