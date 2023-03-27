from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список всех страниц на сайте



@app.route('/')
def hi():
    return "Ку"

@app.route('/about')
def about():
    return "абоба"

@app.route('/contact')
def contact():
    return "позвоните хоть куда, мои службы перехватят телефонный разговор"

@app.errorhandler(404)
def page_not_found(e):
    urls = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and rule.endpoint!="static":
            urls.append({"url": rule.rule, "name": rule.endpoint})
    return render_template('404.html', pages=urls), 404

if __name__ == '__main__':
    app.run(debug=True)
