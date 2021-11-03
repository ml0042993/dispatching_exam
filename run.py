from flask import Flask, render_template,g,request,jsonify
from flask_bootstrap import Bootstrap
from Core_Mongodb import MongodbClient
app = Flask(__name__)

bootstrap = Bootstrap(app)
def get_conn():
	if not hasattr(g,'mongo'):
		g.mongo = MongodbClient()
	return g.mongo

@app.route('/',methods=["GET","POST"])
def index():
	conn = get_conn()

	if request.method == "POST":
		data = request.get_json()

		print(data)
		if data:
			# time = data
			search = int(data.get("num"))

			message = list(conn.read_Nosql(search))[0]
			print(message)
			""" 
			添加一个新的jinja模板，在得到ajax的post信息后，向前端发送此代码片段，并将这部分jinja模板替换之前的代码
			原因为，浏览器会先渲染jinja模板后执行JavaScript命令，所有将渲染好的代码直接传递给母模板可解决问题
			"""
			return render_template('other.html', message=message)
	else:
		num = 1
		# message = conn.read_Nosql(search)
		message = list(conn.read_Nosql(num))[0]
		return render_template('index.html', message=message)






# @app.route('/user/<string:name>')
# def user(name):
# 	return render_template('user.html', name=name)

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.run(port=5555,debug=True)