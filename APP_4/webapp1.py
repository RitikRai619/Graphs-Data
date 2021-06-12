import justpy as jp

def app():
    wp=jp.QuasarPage()
    h1= jp.QDiv(a=wp,text="Analysis of Course Review",classes="text-h3 text-center q-pa-md" )
    p1=jp.QDiv(a=wp,text="Graph to show the review of given Data and input",classes="text-h6  q-pa-md")
    return wp

jp.justpy(app)