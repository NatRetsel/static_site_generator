from typing import List, Dict, Optional

class HTMLNODE:
    def __init__(self, tag: Optional[str] = None, 
                 value: Optional[str] = None, 
                 children: Optional[List['HTMLNODE']] = None, 
                 props: Optional[Dict[str, str]] = None) -> 'HTMLNODE':
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        htmlstr = ""
        if self.props:
            add_to_string = []
            for k,v in self.props.items():
                add_to_string.append(f"{k}=\"{v}\"")
            htmlstr = " " + " ".join(add_to_string)
        return htmlstr
    
    def __repr__(self) -> str:
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props = None) -> 'LeafNode':
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Leaf node value must not be null")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, value: {self.value}, {self.props})"

class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props = None) -> 'ParentNode':
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Tag cannot be empty")
        if not self.children:
            raise ValueError("Children cannot be empty")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        
        
    