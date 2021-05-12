from flask import Flask,redirect,url_for,render_template,request, make_response
import pymysql
# from db import mysql
import mysql.connector
# from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import uuid
import datetime
from functools import wraps
from flask_cors import CORS
#from werkzeug import generate_password_hash, check_password_hash
# from werkzeug.security import generate_password_hash, check_password_hash


app=Flask(__name__)

CORS(app, resources={ r"/*": {'origins': "*"}})

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))
	
 

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "lontchi"

app.config['MYSQL_DATABASE_PASSWORD'] = "1"
app.config['MYSQL_DATABASE_DB'] = "flaskcrud"
mysql.init_app(app)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({"message": "Token is missen!"}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({"message": "Token is invalid!"}),401

        return f( *args, **kwargs)

    return decorated

# users

@app.route('/api/users', methods=['GET'])

def get_all_users():


    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['email'] = user.email
        output.append(user_data)
    return jsonify({
        "users": output
    })

@app.route('/api/user/<public_id>', methods=['GET'])

def get_one_user( public_id):

    

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({
            "message": "no user found!"
        })
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['email'] = user.email

    return jsonify({
        "user": user_data
    })

@app.route('/api/user', methods=['POST'])

def create_user():
   
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        "message": "New user created"
    })



# @app.route('/user/<public_id>', methods=['PUT'])
# # @token_required
# def promote( public_id):

#     # if not current_user.admin:
#     #     return jsonify({'message': 'Cannot perform that function!'})

#     user = User.query.filter_by(public_id=public_id).first()

#     if not user:
#         return jsonify({
#             "message": "no user found!"
#         })
#     user.admin = True
#     db.session.commit()
    
#     return jsonify({
#         "message": "The user has been promoted"
#     })

@app.route('/api/user/<public_id>', methods=['DELETE'])

def delete_user( public_id):

    
    user = User.query.filter_by(public_id=public_id).first()
    print (user)

    if not user:
        return jsonify({
            "message": "no user found!"
        })
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({
        "message": "The user has been deleted successfully"
    })


# users end


# todos beginning

@app.route('/api/addtodo', methods=['POST'])
# @token_required
def add_todo():
	conn = None
	cursor = None
	try:
		_json = request.json
		_title = _json['title']
		_content = _json['content']
		# validate the received values
		if _title and _content and request.method == 'POST':
			
			sql = "INSERT INTO todos_flask(todo_title, todo_content) VALUES(%s, %s)"
			data = (_title, _content,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify({
				"message": "Todo added successfully!"
			})
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/api/todos', methods=['GET'])
# @token_required
def todos():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT todo_id id, todo_title title, todo_content content FROM todos_flask")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/api/todo/<int:id>')
# @token_required
def todo(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT todo_id id, todo_title title, todo_content content FROM todos_flask WHERE todo_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/api/update', methods=['PUT'])
# @token_required
def update_todo():
	conn = None
	cursor = None
	try:
		_json = request.json
		_id = _json['id']
		_title = _json['title']
		_content = _json['content']		
		# validate the received values
		if _title and _content and _id and request.method == 'PUT':
			
			sql = "UPDATE todos_flask SET todo_title=%s, todo_content=%s WHERE todo_id=%s"
			data = (_title, _content, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify({
				"message": "Todo updated successfully!"
			})
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/api/delete/<int:id>', methods=['DELETE'])
# @token_required
def delete_todo(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM todos_flask WHERE todo_id=%s", (id,))
		conn.commit()
		resp = jsonify({
			"message": "Todo deleted successfully!"
		})
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

 
@app.route('/api/login', methods=['POST'])

def login():
	return jsonify({
		"ok"
	})
    # auth = request.authorization

    # if not auth or not auth.username or not auth.password:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login requires!"'})

    # user = User.query.filter_by(name=auth.username).first()

    # if not user:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    # if check_password_hash(user.password, auth.password):
    #     token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

    #     return jsonify({'token' : token.decode('UTF-8')})

    # return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

		
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)





