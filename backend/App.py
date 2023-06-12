from flask import Flask, jsonify ,request
from flask_cors import CORS


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app,resources={r"/*":{'origins':"*"}})

@app.route('/',methods=['GET'])
def mainPage():
    return jsonify({
            "page": "MainPage"
        })

# TIC TAC TOE GAME 
from gameApps.TicTacToe import webGameTicTacToe
tictacetoe = webGameTicTacToe()

@app.route('/tictactoe',methods=['GET','POST'])
def tictactoe():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        userInput = post_data["index"]
        if userInput == 10:
            tictacetoe.reset()
            response_object['message'] = "Game Reset"
            response_object["Game"] = tictacetoe.gameForwardStep()
        else:
            response_object['message'] = "fetched"
            response_object["Game"] = tictacetoe.gameForwardStep(userInput)

    else:
        tictacetoe.reset()
        response_object["message"] = "Started"
        response_object["Game"] = tictacetoe.gameForwardStep()
    
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True)