from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        remaining_text = text
        result_nodes = []

        while delimiter in remaining_text:
            split_result = remaining_text.split(delimiter,1)
            before_delimiter = split_result[0]

            if before_delimiter:
                result_nodes.append(TextNode(before_delimiter, TextType.TEXT))

            remaining_text = split_result[1]
            if delimiter not in remaining_text:
                raise ValueError(f"opening delimiter '{delimiter}' has no closing delimiter")
            
            split_at_closing = remaining_text.split(delimiter, 1)
            delimiter_content = split_at_closing[0]

            result_nodes.append(TextNode(delimiter_content, text_type))

            remaining_text = split_at_closing[1]
        if remaining_text:
            result_nodes.append(TextNode(remaining_text, TextType.TEXT))

        new_nodes.extend(result_nodes)
    return new_nodes