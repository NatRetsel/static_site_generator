import unittest

from htmlnode import HTMLNODE, LeafNode, ParentNode

class TextHTMLNode(unittest.TestCase):
    def test_default_values(self):
        node = HTMLNODE()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_default_props_to_html(self):
        node = HTMLNODE()
        expected_str = ""
        actual_str = node.props_to_html()
        self.assertEqual(expected_str,actual_str)
    
    def test_props_to_html(self):
        node = HTMLNODE(props = {"href":"https://www.google.com", "target":"_blank"})
        expected_str = " href=\"https://www.google.com\" target=\"_blank\""
        actual_str = node.props_to_html()
        self.assertEqual(expected_str,actual_str)
    
    def test_tohtml_valueerror(self):
        leafnode = LeafNode("p",None,None)
        with self.assertRaises(ValueError) as cm:
            leafnode.to_html()
        self.assertEqual(str(cm.exception), "Leaf node value must not be null")
    
    def test_tohtml_positive(self):
        leafnode = LeafNode("p", "This is a paragraph of text.")
        leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leafnode.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leafnode2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    
    
    def test_parentnode_html(self):
        parentnode = ParentNode("p", [LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text")])
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        actual_output = parentnode.to_html()
        self.assertEqual(expected_output,actual_output)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )