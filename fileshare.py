import http.server
import socketserver
import socket
import qrcode
Machine_ip = socket.gethostbyname(socket.gethostname())
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


def QRCode(IP: str, PORT):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=30,
        border=1
    )
    addr = "http://" + IP + ":" + str(PORT)
    print("print the url into the browser: ", addr)
    qr.add_data(addr)
    qr.make(fit=True)
    img = qr.make_image()
    img.show()


QRCode(Machine_ip, PORT)


def shutdown_server():
    str = input("print exit to exit the program")
    if (str == 'exit'):
        httpd.shutdown()

try:
    httpd = socketserver.TCPServer((Machine_ip, PORT), Handler)
    print("serving at port", PORT)
    print("use ctrl + c to exit the program")
    httpd.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    httpd.shutdown()
