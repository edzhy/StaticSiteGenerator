from textnode import *
from leafnode import LeafNode
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != 'text':
            result.append(old_node)
            continue
        if text_type == TextType.CODE:
            count = 0
            for letter in old_node.text:
                if letter == '`':
                    count += 1
            if count % 2 != 0:
                raise Exception('The initial input contains invalid Markdown syntax')
            sub_nodes = old_node.text.split('`')

            for i in range(1,len(sub_nodes)+1,1):
                if i % 2 == 1:
                    result.append(TextNode(sub_nodes[i-1],text_type=TextType.TEXT))
                else:
                    result.append(TextNode(sub_nodes[i-1],text_type=TextType.CODE))
        if text_type == TextType.BOLD:
            count = old_node.text.count('**')
            if count % 2 != 0:
                raise Exception('The initial input contains invalid Markdown syntax')
            sub_nodes = old_node.text.split('**')

            for i in range(1,len(sub_nodes)+1,1):
                if i % 2 == 1:
                    result.append(TextNode(sub_nodes[i-1],text_type=TextType.TEXT))
                else:
                    result.append(TextNode(sub_nodes[i-1],text_type=TextType.BOLD))
        if text_type == TextType.ITALIC:
            count = old_node.text.count('*')
            if count % 2 != 0:
                raise Exception('The initial input contains invalid Markdown syntax')
            sub_nodes = old_node.text.split('*')

            for i in range(1,len(sub_nodes)+1,1):
                if i % 2 == 1:
                    result.append(TextNode(sub_nodes[i-1],text_type=TextType.TEXT))
                else:
                    result.append(TextNode(sub_nodes[i-1],text_type=TextType.ITALIC))

    return result


nodes = [TextNode("This is text with a `code block` word. ", TextType.TEXT),
        TextNode("This is text with a *italic block* word. ", TextType.TEXT),
        TextNode("This is text with a `code block` word. ", TextType.TEXT),
        TextNode("This is text with a **bold block** word. ", TextType.TEXT)]
text_type_dict = {
    TextType.CODE : '`',
    TextType.BOLD : '**',
    TextType.ITALIC : '*'
}
for tt, deli in text_type_dict.items():
    #print(nodes, deli, tt)
    nodes = split_nodes_delimiter(nodes, deli, tt)
print(nodes)
final = ''
for node in nodes:
    final += (node.text_node_to_html_node().to_html())
print(final)
