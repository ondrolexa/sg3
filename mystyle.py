from IPython.core.display import HTML
def css_styling():
    styles = open("./css/sg3.css", "r").read()
    return HTML(styles)

