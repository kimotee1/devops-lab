from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"Request received: {self.path}")
        logging.warning("This is a warning example")
        logging.error("This is an error example")

        if self.path == "/" or self.path == "/login":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Page found!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page not found!")


server = HTTPServer(("0.0.0.0", 8000), MyHandler)

print("Server is running on port 8000")
server.serve_forever()
