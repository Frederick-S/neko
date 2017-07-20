import os
import http.server


def serve(site_path, port):
    os.chdir(site_path)

    http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,
                     port=port, bind='')
