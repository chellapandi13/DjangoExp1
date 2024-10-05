# myapp/views.py

from django.http import HttpResponse

def welcome(request):
    html_content = """
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    text-align: center;
                    padding-top: 50px;
                }
                h1 {
                    color: #4CAF50;
                    font-size: 36px;
                }
                p {
                    color: #555555;
                    font-size: 24px;
                }
            </style>
        </head>
        <body>
            <h1>Kamaraj College Of Engineering & Technology</h1>
            <p>TR Chellapandi 22UIT072</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)

def about(request):
    html_content = """
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    text-align: center;
                    padding-top: 50px;
                }
                h1 {
                    color: #4CAF50;
                    font-size: 36px;
                }
                p {
                    color: #555555;
                    font-size: 24px;
                }
            </style>
        </head>
        <body>
            <h1><b>This is the About Page</b></h1>
            <p>I am Balajee, an undergraduate student in the Department of Information Technology at Kamaraj College of Engineering and Technology.</p>
            <p>I am passionate about coding. My areas of interest are Machine Learning, Deep Learning, IoT, Security, and Networks.</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)
