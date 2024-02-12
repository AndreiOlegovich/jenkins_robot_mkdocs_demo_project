from typing import List
from playwright.sync_api import sync_playwright

class WebObject:
    def __init__(self, all_inner_texts):
        self.all_inner_texts = all_inner_texts
        print("WebObject created!")




def read_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://www.eth1.ru/i/selenium/basic_test/")
        result = page.title()
        print(page.title())        
        browser.close
    return result


def find_elements_by_class_name(class_name = "default"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://www.eth1.ru/i/selenium/basic_test/")
        search_parameter = f"[class={class_name}]"
        elements = page.locator(search_parameter)
        web_object = WebObject(elements.all_inner_texts())
        all_inner_texts = web_object.all_inner_texts
        for tx in all_inner_texts:
            print(tx)
        print(f"\n\n elements all_inner_texts\n -----------------\n"
              f"{elements.all_inner_texts()}\n----------------\n")
    return web_object 


def find_element_by_class_name(class_name = "default", el_index = 0):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://www.eth1.ru/i/selenium/basic_test/")
        search_parameter = f"[class={class_name}]"
        
        attr = page.get_attribute('.websites', 'text')
        print(f"\n\nattr: {attr}\n\n")

        elements = page.locator(search_parameter)

        # print(f"\n\n elements:\n -----------------\n{elements}
        # \n----------------\n")
        # print(f"\n\n type(elements):\n -----------------\n
        # {type(elements)}\n----------------\n")
        # print(f"\n\n dir(elements):\n -----------------\n
        # {dir(elements)}\n----------------\n")
        # print(f"\n\n elements all_inner_texts\n -----------------\n
        # {elements.all_inner_texts()}\n----------------\n")
        el_texts = elements.all_inner_texts()
        print(f"\n\nel_texts: {el_texts}\n")
        print(f"\ntype(el_texts): {type(el_texts)}\n")

        # elements = page.query_selector_all(search_parameter)
        result = elements[el_index]
        print(f"\n\n-----------------\n{result}\n----------------\n")
        print(f"\n\n=================\n{result.inner_text()}\n=============\n")
        browser.close
    return result


def get_element_inner_text_by_class_name(class_name = "default",
                                         el_index = 0) -> str:
    elements = find_elements_by_class_name(class_name)
    text = elements.all_inner_texts[el_index]
    return text


def find_elements_by_class_name2(class_name = "default") -> List[str]:
    elements = ["a", "b"]
    # elements = 2

    if isinstance(elements, list):
        return elements
    else:
        raise TypeError("Not valid elements data type. Expecting list")
        return None


if __name__ == "__main__":
    # read_title()
    # r = find_elements_by_class_name("websites")
    # print(r)
    r2 = get_element_inner_text_by_class_name("websites", 2)
    print(r2)
