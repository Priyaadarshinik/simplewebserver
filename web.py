from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>TOP SOFTWARE COMPANIES</title>
    </head>
    <BODY>
        <table border="2" cellspacing="10" cellpadding="5" width="500" height="500">
        <caption>REVENUE OF SOFTWARE COMPANIES </caption>
            <tr>
                <th bgcolor="pink"><B>RANK</B></th>
                <th bgcolor="pink">NAME OF THE COMPANY</th>
                <th bgcolor="pink">REVENUE(in $)</th>
            </tr>
            <tr>
                <td bgcolor="sky blue">1</td>
                <td>APPLE</td>
                <td>1859</td>
            </tr>
            <tr>
                <td bgcolor="sky blue">2</td>
                <td>FACEBOOK</td>
                <td>1621</td>
            </tr>
            <tr>
                <td bgcolor="sky blue">5</td>
                <td>VISA</td>
                <td>1062</td>
            </tr>
            <tr>
                <td bgcolor="sky blue">10</td>
                <td>MICROSOFT</td>
                <td>748</td>
            </tr>
            <tr>
                <td bgcolor="sky blue">18</td>
                <td>INTEL</td>
                <td>560</td>
            </tr>
            </table>
        </BODY>
</html>
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