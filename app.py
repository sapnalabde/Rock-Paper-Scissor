from flask import Flask
from flask import url_for
from flask import redirect
import webbrowser
from flask import request
from flask import render_template

app = Flask(__name__)




@app.route('/', methods=["POST", "GET"])
def get_data():
    if request.method == "POST":
        first_player = request.form['name_1']
        first_player_choice = request.form['choice_1']
        second_player = request.form['name_2']
        second_player_choice = request.form['choice_2']
        return redirect(
            url_for("play_game", choice_1=first_player_choice, choice_2=second_player_choice, first_name=first_player,
                    second_name=second_player))
    else:
        return render_template("index.html")


@app.route('/play_game/<choice_1>/<choice_2>/<first_name>/<second_name>', methods=["POST","GET"])
def play_game(choice_1, choice_2, first_name, second_name):
    if choice_1 == choice_2:
        return f"""<h1><center> Its a TIE!!!</h1> </center>"""
    elif choice_1 == "ROCK":
        if choice_2 == "SCISSORS":
            return f"""<h1><center>{first_name} Won!!!</h1> </center>"""
        else:
            return f"""<h1><center> {second_name} Won!!!</h1> </center>"""
    elif choice_1 == "PAPER":
        if choice_2 == "ROCK":
            return f"""<h1><center>{first_name} Won!!!</h1> </center>"""
        else:
            return f"""<h1><center>{second_name} Won!!!</h1> </center>"""
    elif choice_1 == "SCISSORS":
        if choice_2 == "PAPER":
            return f"""<h1><center>{first_name} Won!!!</h1> </center>"""
        else:
            return f"""<h1><center>{second_name} Won!!!</h1> </center>"""


if __name__ == '__main__':
    app.run(debug=True)
