from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('urlInput')
        # Process the form data here (if needed)
        return redirect(url_for('display_url', url=url))  # Redirect to a different endpoint
    else:
        return render_template('home.html')


@app.route("/display_url/<path:url>", methods=['GET', 'POST'])
def display_url(url=None):
    if url:
        if request.method == 'POST':
            url2 = request.form.get('urlInput')
            # Process the form data here (if needed)
            return redirect(url_for('display_url', url=url2))
        else:
            return render_template('home.html', url=url)
    else:
        return redirect(url_for('home'))
