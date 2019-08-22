from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return 'Allspark ITSM says Hello'   

if __name__ == "__main__":
    app.run()