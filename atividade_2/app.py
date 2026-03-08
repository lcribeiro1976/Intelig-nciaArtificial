from flask import Flask, request, jsonify, render_template_string
import joblib, numpy as np

app = Flask(__name__)
modelo        = joblib.load("modelo/modelo_evasao.pkl")
scaler        = joblib.load("modelo/scaler.pkl")
encoders      = joblib.load("modelo/encoders.pkl")
feature_names = joblib.load("modelo/feature_names.pkl")

HTML = open("template.html", encoding="utf-8").read()

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/prever", methods=["POST"])
def prever():
    try:
        dados = request.json
        linha = []
        for feat in feature_names:
            val = dados[feat]
            if feat in encoders:
                val = encoders[feat].transform([str(val)])[0]
            linha.append(float(val))
        X_in = np.array(linha).reshape(1, -1)
        X_sc = scaler.transform(X_in)
        pred = int(modelo.predict(X_sc)[0])
        prob = float(modelo.predict_proba(X_sc)[0][1])
        return jsonify({"evasao": bool(pred), "probabilidade": prob})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
