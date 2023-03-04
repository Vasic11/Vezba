import http.server as srv
import urllib
import urllib.parse as parse

class Hendler(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        super().do_GET()
    def do_POST(self):

        duzina = int(self.headers["Content-Lenght"])                            
        podaci = self.rfile.read(duzina).decode()
        parametri = dict(parse.parse_qsl(podaci))
        print(parametri)
        prvi_broj = int(parametri["prvibroj"])
        drugi_broj = int(parametri["drugibroj"])
        rezultat = ""
        if "sabiranje" in parametri:
            rezultat += "saniranje" + str(prvi_broj + drugi_broj) + " "
        if "oduzimanje" in parametri:
            rezultat += "saniranje" + str(prvi_broj + drugi_broj) + " "
        rezultat = prvi_broj + drugi_broj  
        odgovor = f"HTTP/1.1 200 Ok\r\nContetn-type: text/html\r\n\r\nRezultat je {rezultat}" 
        self.wfile.write(odgovor.encode())                                                   
        #super().do_GET()


srv.HTTPServer(("0.0.0.0",8000),Hendler).serve_forever()