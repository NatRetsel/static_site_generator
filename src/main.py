from textnode import TextNode, TextType

def main():
    dummy_text_node = TextNode("This is a dummy text node", TextType.ITALIC, "https:://www.boot.dev")
    print(dummy_text_node)
    
if __name__ == "__main__":
    main()