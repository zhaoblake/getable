from pyquery import PyQuery as PyqElement


def is_visible(element: PyqElement) -> bool:
    style = element.attr("style")
    if style is not None:
        style = style.replace(" ", "")
        if "display:none" in style or "hidden" in style:
            return False
    return True
