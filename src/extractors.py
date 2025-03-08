import re

def extract_markdown_images(input_line):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", input_line)

def extract_markdown_links(input_line):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", input_line)
