from flask import Flask 
from controller.user import router as users

vote= Flask(__name__)

vote.secret_key = 'your_secret_key'

vote.register_blueprint(users)

if __name__ == "__main__" :
    vote.run(debug="true")