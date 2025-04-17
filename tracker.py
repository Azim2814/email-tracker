from flask import Flask, request, send_file
from datetime import datetime
import csv
import os

app = Flask(__name__)

@app.route("/track/open", methods=["GET"])
def track_open():
    email = request.args.get("email", "unknown")
    uid = request.args.get("uid", "none")
    log_open(email, uid)
    return send_file("pixel.png", mimetype="image/png")

def log_open(email, uid):
    log_file = "open_log_test.csv"
    file_exists = os.path.isfile(log_file)

    try:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Timestamp", "Email", "UID", "Status"])
            writer.writerow([datetime.now().isoformat(), email, uid, "opened"])
        print(f"✅ Logged open for {email} | UID: {uid}")
    except Exception as e:
        print(f"❌ Failed to log open: {e}")

# === OPEN TRACKING ===
# @app.route("/track/open", methods=["GET"])
# def track_open():
#     email = request.args.get("email", "unknown")
#     log_open(email)
#     return send_file("pixel.png", mimetype="image/png")

# def log_open(email):
#     log_file = "open_log.csv"
#     file_exists = os.path.isfile(log_file)

#     try:
#         with open(log_file, "a", newline="") as f:
#             writer = csv.writer(f)
#             if not file_exists:
#                 writer.writerow(["Timestamp", "Email", "Status"])
#             writer.writerow([datetime.now().isoformat(), email, "opened"])
#         print(f"✅ Logged open for {email}")
#     except Exception as e:
#         print(f"❌ Failed to log open: {e}")
# def log_open(email):
#     log_file = "open_log_test.csv"  # <-- NEW FILE NAME
#     file_exists = os.path.isfile(log_file)

#     try:
#         with open(log_file, "a", newline="") as f:
#             writer = csv.writer(f)
#             if not file_exists:
#                 writer.writerow(["Timestamp", "Email", "Status"])
#             writer.writerow([datetime.now().isoformat(), email, "opened"])
#         print(f"✅ Logged open for {email}")
#     except Exception as e:
#         print(f"❌ Failed to log open: {e}")



# === CLICK TRACKING ===
@app.route("/track/click", methods=["GET"])
def track_click():
    email = request.args.get("email", "unknown")
    log_click(email)
    # Redirect to actual link after logging (optional)
    return "Thanks for clicking!"

def log_click(email):
    log_file = "click_log.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Email", "Status"])
        writer.writerow([datetime.now().isoformat(), email, "clicked"])

# === RUN SERVER ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
