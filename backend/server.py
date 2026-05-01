import http.server
import socketserver
import json
import os

PORT = 8080

# Определяем путь к папке frontend относительно этого файла
# Это гарантирует, что файл найдется всегда
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Формируем точный путь к index.html
            self.path = '/index.html'

        # Говорим серверу искать файлы в папке frontend
        os.chdir(FRONTEND_DIR)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/api/hello':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"message": "Привет! Бэкенд на связи!"}
            self.wfile.write(json.dumps(response).encode())


print(f"Сервер запущен на http://localhost:{PORT}")
# Запускаем сервер
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    httpd.serve_forever()