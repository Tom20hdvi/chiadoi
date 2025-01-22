from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Lấy danh sách cặp từ form
            pairs_input = request.form.get("pairs", "").strip()
            if not pairs_input:
                raise ValueError("Danh sách cặp không được để trống!")

            # Tách các cặp và kiểm tra định dạng
            pairs = [tuple(pair.split(",")) for pair in pairs_input.split("\n") if "," in pair]
            if not pairs:
                raise ValueError("Danh sách cặp không đúng định dạng (phải có dấu phẩy giữa các tên).")

            # Chia đội
            team_a, team_b = [], []
            for pair in pairs:
                if random.choice([True, False]):
                    team_a.append(pair[0].strip())
                    team_b.append(pair[1].strip())
                else:
                    team_a.append(pair[1].strip())
                    team_b.append(pair[0].strip())

            return render_template("result.html", team_a=team_a, team_b=team_b)
        
        except ValueError as e:
            # Trả về lỗi nếu người dùng nhập sai
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    # Lấy cổng từ biến môi trường (dùng cho Render) hoặc mặc định là 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
