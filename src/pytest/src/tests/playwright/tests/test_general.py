from playtest import read_title, get_element_inner_text_by_class_name

def test_correct_title_read():
    title = read_title()
    assert title == "Test Page Selenium"


def test_inner_text_by_class_name():
    inner_text = get_element_inner_text_by_class_name("websites", 2)
    print(inner_text)
    assert inner_text == "DevHops.ru"
