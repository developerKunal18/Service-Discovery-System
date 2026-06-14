from flask import Flask, request, jsonify

app = Flask(__name__)

# Service Registry
services = {}

# ---------- Register ----------
@app.route(
    "/register",
    methods=["POST"]
)
def register():

    data = request.get_json()

    services[
        data["service_name"]
    ] = data["address"]

    return jsonify({
        "message":
        "Service registered"
    })

# ---------- Discover ----------
@app.route(
    "/discover/<service_name>"
)
def discover(service_name):

    address = services.get(
        service_name
    )

    if not address:

        return jsonify({
            "message":
            "Service not found"
        }), 404

    return jsonify({
        "service_name":
        service_name,
        "address":
        address
    })

# ---------- List ----------
@app.route("/services")
def list_services():

    return jsonify(services)

if __name__ == "__main__":
    app.run(
        port=5000,
        debug=True
    )
