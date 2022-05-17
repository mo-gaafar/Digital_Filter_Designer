import dash_html_components as html
from apps.navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to page 3!')


def create_page_3():
    layout = html.Div([
        nav,
        header,
    ])
    return layout