from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
	<head>
        <title>Device Specifications</title>
    </head>
    <body bgcolor="pink">

        <h1 align="center">Device Specifications(Dharsheni 24006589)</h1>
       
        <ol type="1">
            <li>DEVICE NAME :DESKTOP-MOHHBTU</li>
            <li>PROCESSOR :TM i5-1335U   1.30 GHz</li>
            <li>INSTALLED RAM :16.0 GB (15.7 GB usable)</li>
            <li>DEVICE ID :15EEA3B2-7EF5-4DEC-903D-577382C3C005</li>
            <li>PRODUCT ID :00342-42708-33509-AAOEM</li>

        </ol>
        <ul>
            <li>Windows 11 Home Single Language</li>
            <li>24H2</li>
            <li>os build</li>
        </ul>
    </body>
	
	
</html
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()