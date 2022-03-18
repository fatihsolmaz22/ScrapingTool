# Scraping Tool

Welcome to a simple scraping tool.

## How to get html elements and its content
### Html
```html
<!DOCTYPE html>
<html>
<body>
  <section class="top">
    <p id="p_1">My first paragraph.</p>
    <button class="button" onclick="myFunction()">Click me</button>
  </section>
</body>
</html>
```
### What do we want?
We want the inner text of the paragraph with id = "p_1":

    My first paragraph.

### Python Code
```python
# First we need to import our ScrapingTool the constants like html tags ("p", "span", etc.)
from <enter_path_here>.scraping_constants import HtmlTags, HtmlAttributes, XPathStringFunctions
from <enter_path_here>.scraping_tool import ScrapingTool

# We want to get the whole html page first. We will call it the "main_page_element":
main_page_element = ScrapingTool.get_main_page_element(url="https://www.example.com")

# Next, we want to access the paragraph element.
p_element = ScrapingTool.get_html_elements_by_css_selector(
		html_element=main_page_element,   # html element you want to find the element on
		html_tag=HtmlTags.P_TAG,          # html tag 			--> "p", "span", etc.
		attribute_name=HtmlAttributes.ID, # attribute name 	--> "id", "class", etc.
		attribute_value="p_1",            # attribute value 	--> id="p_1"
		get_first_element=True)           # we only need 1 element
```
Now if we print out the inner text of the element:
```python
print(p_element.text)
> My first paragraph.
```
Or if we wanted, we could also get its class name:
```python
print(p_element..getAttribute(HtmlAttributes.CLASS))
> p_1
```
Check selenium docs for further extraction of element informations --> [Selenium Docs](https://www.selenium.dev/documentation/webdriver/elements/information/)

### We can also use the new elements as the new base
We have seen before how to get to the paragraph element directly. But what if we wanted the whole section and then the paragraph element?
```python
section_element = ScrapingTool.get_html_elements_by_css_selector(
		html_element=main_page_element,       # html element you want to find the element on
		html_tag=HtmlTags.SECTION_TAG,        # html tag 			--> "p", "span", etc.
		attribute_name=HtmlAttributes.CLASS,  # attribute name 	--> "id", "class", etc.
		attribute_value="top",                # attribute value 	--> id="p_1"
		get_first_element=True)               # we only have 1 section

p_element = ScrapingTool.get_html_elements_by_css_selector(
		html_element=section_element,         # html element you want to find the element on
		html_tag=HtmlTags.P_TAG,              # html tag 			--> "p", "span", etc.
		attribute_name=HtmlAttributes.ID,     # attribute name 	--> "id", "class", etc.
		attribute_value="p_1",                # attribute value 	--> class="top"
		get_first_element=True)               # we only need 1 element
```
And there we go. We have the paragraph element.
## How to click on elements
We use the example from above as frame..
### Click on an element
```python
ScrapingTool.click_element_on_page(
    html_element=main_page_element,
    html_tag=HtmlTags.BUTTON_TAG,
    attribute_name=HtmlAttributes.CLASS,
    attribute_value="button")
```
This clicks on the button and executes whatever the button is used for.

## Don't forget!
If some html tags / attributes don't exist in **scraping_constants.py**, you can add it anytime in there.
