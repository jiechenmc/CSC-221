from flask import Flask, request
from processing import do_calculation
app = Flask(__name__)

# User inputs 2 number that they want to add together
# The program will then add the 2 numbers and print the total to the page


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        # request.form["input name"] to get value
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number2"])

        if number1 is not None and number2 is not None:
            result = do_calculation(number1, number2)
            # Return the result to the page
            return '''
                    <html>
                        <body>
                            <p>The result is {result}</p>
                            <p><a href="/">Click here to calculate again</a>
                        </body>
                    </html>
                '''.format(result=result)

    # Initial startup page
    return '''
        <html>
            <body>
                {errors}
                Jie Chen <br>
                <p>Enter your numbers:</p>
                <form method="post" action=".">
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)


if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()
