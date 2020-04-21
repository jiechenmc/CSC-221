from flask import Flask, render_template, request
app = Flask(__name__)


def calc(scores):
    """ Function calculates sum and average """
    total = sum(scores)
    average = total/len(scores)
    return total, average


scores_list = []
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("score"):
            scores_list.append(float(request.form.get("score")))
        name = request.form.get("name")

        if request.form.get("action") == "Calculate Grade":
            total, average = calc(scores_list)
            scores_list.clear()
            return render_template("results.html").format(name=name, total=total, average=average)

    if len(scores_list) == 0:
        scores = ""
    else:
        scores = ""
        for score in scores_list:
            scores += "&nbsp{}&nbsp".format(score)
    return render_template("index.html").format(scores=scores)


if __name__ == "__main__":
    app.run(debug=True)
