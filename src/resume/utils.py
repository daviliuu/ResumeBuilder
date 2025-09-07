import resume.constants as const

def create_heading(header: str):
    return f"""
    #set align(left)
    #text({const.HEADER})[{header}]
    #block(spacing: 0.3cm)[
        #line(length: 100%, stroke: 1pt)
    ]
    """

