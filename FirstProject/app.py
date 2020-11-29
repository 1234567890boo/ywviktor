from flask import Flask,render_template
app=Flask("First Venv Project")

@app.route('/')
def index():
    return render_template('test.html')

if __name__=='__main__':
    app.run(debug=True)

#do flask 2