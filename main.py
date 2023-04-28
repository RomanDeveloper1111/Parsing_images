import re


def search_img_links(html_str):
    reg = r'<img [^>]* src="(.*?)"'
    return re.finditer(reg, html_str)


