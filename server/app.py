from flask import Flask,redirect,url_for,render_template,request
import pymysql
# from db import mysql
import mysql.connector
# from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from flask import jsonify
from flask import flash
from flask_cors import CORS, cross_origin
#from werkzeug import generate_password_hash, check_password_hash
# from werkzeug.security import generate_password_hash, check_password_hash


app=Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "lontchi"
app.config['MYSQL_DATABASE_PASSWORD'] = "1"
app.config['MYSQL_DATABASE_DB'] = "flaskcrud"
mysql.init_app(app)
CORS(app)

# query="SELECT user_id id, user_name name, user_email email, user_password pwd FROM tbl_user"
        	# if query !=0:
            #     resp = jsonify({
            #         "message": "User already exist!"
            #     })
            #     resp.status_code = 200
            #     return resp

# CREATE TABLE `todos_flask` (
#   `todo_id` bigint COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,
#   `todo_title` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   `todo_content` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   PRIMARY KEY (`todo_id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


@app.route('/addtodo', methods=['POST'])
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
		
@app.route('/todos', methods=['GET'])
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
		
@app.route('/todo/<int:id>')
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

@app.route('/update', methods=['PUT'])
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
		
@app.route('/delete/<int:id>', methods=['DELETE'])
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
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()



