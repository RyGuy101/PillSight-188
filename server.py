import socketserver
from http.server import BaseHTTPRequestHandler

def some_function():
    print("some_function got called")

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/captureImage':
            # Insert your code here
            some_function()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(self.wfile)
        self.wfile.write(b"<html><head><title>Title goes here.</title></head>")
        self.wfile.write(b"<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(b"</body></html>")

httpd = socketserver.TCPServer(("", 8080), MyHandler)
httpd.serve_forever()
