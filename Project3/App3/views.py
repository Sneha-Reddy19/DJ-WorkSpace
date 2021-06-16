from django.http import HttpResponse

def ShowIndex(http_request):
    message = '''
            <html>
                <body bgcolor="white">                    
                    <h1 style = "color:blue">
                        <font size="10">                            
                                Welcome to Django Example                            
                        </font>
                    </h1>
                    <h2 style = "color:yellow">
                                Example3 is Practice3
                    </h2>
                    <h3 style = "color:red">
                                Example3 is about adding a html code in views file
                    </h3> 
                </body>
            </html>'''
    return HttpResponse(message)
