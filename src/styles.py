def getStyles(style_to_give: str) -> str:
    """Return a style based on the argument type"""

    if style_to_give == "main-window":
        return "background-color: #777;\n""color: whitesmoke;"
    elif style_to_give == "v-line":
        return "background-color: black;"
    elif style_to_give == "push-btn":
        return "color: whitesmoke;\n""border: 1px solid #9f9f9f;\n""padding: 3px;\n""border-radius: 1px;"
    else:
        return TypeError("Expected: main-window, or v-line, or push-btn")
