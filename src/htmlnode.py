from typing import List, Dict, Optional

class HTMLNode():
    def __init__(
            self,
            tag: Optional[str] = None,
            value: Optional[str] = None,
            children: Optional[List["HTMLNode"]] = None,
            props: Optional[Dict[str, str]] = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            value: str,
            props: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(
            tag=tag,
            value=value,
            props=props
        )

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: List["HTMLNode"],
            props: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(
            tag=tag,
            children=children,
            props=props
        )

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            return ValueError("Invalid HTML: no children")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"