from dash.dependencies import Input, Output, State
from pages import home, test
from index import app
# router
@app.callback(
    Output('page-content','children'),
    [Input('url','pathname')]
)
def router(url):
    if url=='/home':
        return home.container
    elif url=='/test':
        return test.container

    else:
        return test.container