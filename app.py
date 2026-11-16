from flask import Flask, render_template, request
from student_manager import calculate_average, get_mention, is_admitted, validate_grades

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    context = {"average": None, "mention": None, "admitted": None, "error": None}
    if request.method == "POST":
        raw = request.form.get("grades", "").strip()
        if not raw:
            context["error"] = "Veuillez saisir au moins une note."
            return render_template("index.html", **context)
        try:
            grades = [float(x.strip()) for x in raw.split(",") if x.strip() != ""]
        except ValueError:
            context["error"] = "Format invalide."
            return render_template("index.html", **context)
        
        if not validate_grades(grades):
            context["error"] = "Notes invalides : chaque note doit être entre 0 et 20."
            return render_template("index.html", **context)
        
        avg = calculate_average(grades)
        context["average"] = round(avg, 2)
        context["mention"] = get_mention(avg)
        context["admitted"] = "Oui" if is_admitted(avg) else "Non"
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)