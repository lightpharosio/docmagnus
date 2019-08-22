from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return 'Allspark Manager says Hello'   

if __name__ == "__main__":
    app.run()
