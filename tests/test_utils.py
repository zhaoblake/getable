from pyquery import PyQuery as PyqElement

from tableparser.utils import is_visible


def test_is_visible():
    visible_element = PyqElement("<div></div>")
    assert is_visible(visible_element) is True

    display_none_element = PyqElement("<div style='display: none'></div>")
    assert is_visible(display_none_element) is False

    visibility_hidden_element = PyqElement("<div style='visibility: hidden'>")
    assert is_visible(visibility_hidden_element) is False
