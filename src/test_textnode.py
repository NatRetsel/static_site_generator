import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node: TextNode = TextNode("This is a text node", TextType.BOLD)
        node2: TextNode = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_print(self):
        node: TextNode = TextNode("This is a text node", TextType.CODE)
        expected_print: str = f"TextNode({node.text}, {node.text_type.value}, {node.url})"
        actual_print: str = node.__repr__()
        self.assertEqual(expected_print, actual_print)
    
    def test_texttype_noteq(self):
        node: TextNode = TextNode("This is a text node", TextType.BOLD)
        node2: TextNode = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_url_noteq(self):
        node: TextNode = TextNode("This is a text node", TextType.BOLD)
        node2: TextNode = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        self.assertNotEqual(node, node2)
 
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")   

if __name__ == "__main__":
    unittest.main()