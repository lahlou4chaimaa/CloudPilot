
import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 5001

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

class RemediationHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/webhook":
            self.send_error(404, "Endpoint not found")
            return

        try:
            content_length = int(
                self.headers.get("Content-Length", "0")
            )

            if content_length <= 0 or content_length > 1_000_000:
                self.send_error(400, "Invalid payload size")
                return

            raw_body = self.rfile.read(content_length)
            payload = json.loads(raw_body.decode("utf-8"))

            alerts = payload.get("alerts", [])

            for alert in alerts:
                name = alert.get("labels", {}).get(
                    "alertname", "UnknownAlert"
                )
                server = alert.get("labels", {}).get(
                    "server", "UnknownServer"
                )
                state = alert.get("status", "unknown")

                logging.info(
                    "Alerte recue | nom=%s | serveur=%s | etat=%s",
                    name,
                    server,
                    state,
                )

                if name == "ServerExporterDown" and state == "firing":
                    logging.warning(
                        "REMEDIATION SIMULEE | serveur=%s | "
                        "action=verification de disponibilite",
                        server,
                    )

            response = json.dumps({
                "status": "received",
                "alerts_processed": len(alerts),
            }).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        except (json.JSONDecodeError, UnicodeDecodeError, ValueError):
            self.send_error(400, "Invalid JSON payload")

    def log_message(self, format_string, *args):
        logging.info(
            "HTTP | " + format_string,
            *args,
        )

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), RemediationHandler)

    logging.info(
        "CloudPilot Remediation Worker demarre sur le port %s",
        PORT,
    )

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Arret du worker")
    finally:
        server.server_close()
