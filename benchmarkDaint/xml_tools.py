import xml.dom.minidom
def read_config(filename):
    return xml.dom.minidom.parse(filename)


def set_in_xml(xml_node, path, value):
    split_path = path.split(".")

    for tag_name in split_path:
        xml_node = xml_node.getElementsByTagName(tag_name)[0]

    xml_node.firstChild.nodeValue = value

def get_in_xml(xml_node, path):
    split_path = path.split(".")

    for tag_name in split_path:
        xml_node = xml_node.getElementsByTagName(tag_name)[0]

    return str(xml_node.firstChild.nodeValue)

def get_xml_node(xml_node, path):
    split_path = path.split(".")
    for tag_name in split_path:
        xml_node = xml_node.getElementsByTagName(tag_name)[0]

    return xml_node
