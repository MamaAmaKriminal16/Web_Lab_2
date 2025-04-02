from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        text = "Скальський Марк, група КП-21".encode("utf-8")
        self.send_header('Content-Length', str(len(text)))
        self.end_headers()
        self.wfile.write(text)

host = "localhost"
port = 8443

httpd = HTTPServer((host,port),MyHandler)

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2
ssl_context.maximum_version = ssl.TLSVersion.TLSv1_3

ssl_context.set_ciphers('AES256-SHA256:AES256-SHA')

ssl_context.load_cert_chain(certfile='/Users/marksospisos/localhost.pem',
                            keyfile='/Users/marksospisos/localhost-key.pem')
httpd.socket = ssl_context.wrap_socket(httpd.socket,server_side=True)

print(f"Сервер запущено на https://{host}:{port}")
httpd.serve_forever()