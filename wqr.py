from flask import Flask, render_template, request

from qrr_c import QR, NegativeRootError

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            c = float(request.form.get('c'))

            solver = QR(a, b, c)
            roots = solver.roots()

            return render_template('index.html', roots=roots, error=None)

        except ValueError as ve:
            error_message = f"Error: {ve}"
            return render_template('index.html', error=error_message)

        except NegativeRootError as nre:
            error_message = f"Error: {nre}"
            return render_template('index.html', error=error_message)

        except ZeroDivisionError as zde:
            error_message = f"Error: {zde}"
            return render_template('index.html', error=error_message)

    return render_template('index.html', error=None)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

