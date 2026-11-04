"""Tiny Flask API used as the 'workload' for the CI/CD migration project."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    # Health endpoint: used later by load balancers, K8s probes and SLO checks.
    return jsonify(status="ok")


@app.get("/api/portfolio/<int:fund_id>")
def portfolio(fund_id: int):
    # Fake data - just something to test against.
    return jsonify(fund_id=fund_id, nav=round(100 + fund_id * 1.5, 2))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
