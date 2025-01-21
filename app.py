from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Lấy danh sách cặp từ form
        pairs = request.form.get("pairs").strip().split("\n")
        pairs = [tuple(pair.split(",")) for pair in pairs if "," in pair]

        # Chia đội
        team_a, team_b = [], []
        for pair in pairs:
            if random.choice([True, False]):
                team_a.append(pair[0])
                team_b.append(pair[1])
            else:
                team_a.append(pair[1])
                team_b.append(pair[0])

        return render_template("result.html", team_a=team_a, team_b=team_b)

    return render_template("index.html")
