from flask import Flask, render_template
import ai_paragraph

app = Flask(__name__)

@app.route('/')
def home():
    try:
      paragraph = ai_paragraph.generate()
      return render_template('index.html', my_gen_paragraph=paragraph)
    except Exception as e:
      print(e)
      return render_template('index.html', my_gen_paragraph="Something is wrong with the server, try again later")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
