import http.server as srv
import urllib as parse
model = {
    1:"Prvi strip o Naruto",
    5:"Ovo je neki strip"
}

class Handler(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.send_response(200)
        if self.path == "/unos":
            self.wfile.write(open("unos.html","rv").read())

        else:
            izlaz = ""
            self.end_headers()
            for broj,naslov in model.items():
                izlaz += f"<div> style='border:1px solid red; padding:4pxmarginh:4px;'>{broj} : {naslov}"
            self.wfile.write(izlaz.encode())

    def do_POST(self):
        duzina = int(self.headers["Content-Lenght"])                            
        sadrzaj = self.rfile.read(duzina).decode()
        parametri = dict(parse.parse_qsl(sadrzaj))
        print(parametri)
        broj = int(parametri["broj"])
        naslov = parametri["naslov"]
        model[broj] = naslov



srv.HTTPServer(("0.0.0.0", 8000),Handler).serve_forever()