import resume.constants as const
import re as regex

def create_heading(header: str):
    return f"""
    #set align(left)
    #text({const.HEADER})[{header}]
    #block(spacing: 0.3cm)[
        #line(length: 100%, stroke: 1pt)
    ]
    """

def convert_bold(text: str):
    """
    Converts **foo bar** to #emph()[foo bar]
    """
    pattern = r"\*\*(.*?)\*\*"
    replacement = r"""#text(weight: "bold")[\1]"""
    return regex.sub(pattern, replacement, text)
