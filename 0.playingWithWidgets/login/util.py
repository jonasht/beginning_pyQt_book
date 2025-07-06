PRIMARY = 'primary'
SECONDARY = 'secondary'
SUCCESS = 'success'
DANGER = 'danger'
INFO = 'info'
WARNING = 'warning'
LINK = 'link'

import textwrap

class Text:
    title = textwrap.dedent("""
        color: white;
        font-weight: 200;
        font-size: 20px;
        background-color: #0dcaf0;
        padding: 6px 24px;
        border-bottom-left-radius: 24px;
        border-bottom-right-radius: 24px;
    """).strip()
        
def get_style():
    with open('./styleV3.css', 'r') as file:
        return file.read()

class Colors:
    primary = "#0d6efd"
    secondary = "#6c757d"
    success = "#198754"
    danger = "#dc3545"
    warning = "#ffc107"
    info = "#0dcaf0"
    dark = "#212529"
    light = "#f8f9fa"
    white = "#fff"
    black = "#000"

if __name__ == '__main__':
    # teste
    print(Colors.primary)
