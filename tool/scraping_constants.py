class XPathStringFunctions:
    CONTAINS_STRING = "contains"

class XPathTemplates:
    ATTRIBUTE_SELECTOR_BASE = './/{}[@{}="{}"]'
    ATTRIBUTE_SELECTOR_STRING_FUNCTIONS = './/{}[{}(@{}, "{}")]'

class HtmlTags:
    A_TAG = "a"
    DIV_TAG = "div"
    P_TAG = "p"
    SPAN_TAG = "span"
    INPUT_TAG = "input"
    # TODO: add values to scrape

class HtmlAttributes:
    CLASS = "class"
    TITLE = "title"
    ID = "id"
    # TODO: add values to scrape

class HTMLAttributeValues:
    # TODO: add values to scrape
    pass