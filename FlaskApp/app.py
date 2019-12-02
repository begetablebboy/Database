from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# instantiate an object for MySQL
mysql = MySQL(app)

# GET request- display orm to the user
# POSt request - store details onto the database
@app.route("/", methods=['GET','POST'])
def index():
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form
		name = userDetails['name']
		book_title = userDetails['book_title']
		review = userDetails['review']
		summary = userDetails['summary']
		overall = request.form.get('overall')
		reviewTime= request.form.get('reviewTime')
		unixReviewTime= userDetails ['unixReviewTime']
		cur = mysql.connection.cursor()
		# Create a database called test and create necessary tables
		cur.execute("INSERT INTO test(reviewerName,booktitle,reviewText,summary,overall,reviewTime,unixReviewTime) VALUES(%s, %s, %s,%s,%s,%s,%s)"
                            ,(name,book_title,review,summary,overall,reviewTime,unixReviewTime))
		# Save changes into the database
		mysql.connection.commit()
		cur.close()
		return 'update successful'
		# return redirect('/users')
	return render_template('home.html')


@app.route('/users')
# Display data onto the web browser
def users():
	cur = mysql.connection.cursor()
	# display = cur.execute("SELECT reviewerName FROM kindle_reviews LIMIT 2")
	# newtbl = cur.execute('''CREATE TABLE test1(id int UNIQUE AUTO_INCREMENT,reviewerName varchar(80),booktitle varchar(30),reviewText text(32767),asin varchar(10),reviewTime int(10),overall int(1))''')
	# cur.execute('''INSERT INTO test1(reviewerName, booktitle, reviewText, asin, reviewTime, overall) VALUES ('Ariel', 'Little Mermaid', 'Ariel is pretty', 'B006784SZQ', 05092019, 4)''')
	# mysql.connection.commit()
	cur.execute('''SELECT * FROM test 1''')
	return cur.fetchall()
	# if display > 0:
	# userDetails = cur.fetchall()
	# print(userDetails)
	# return render_template('users.html', userDetails=userDetails)


if __name__ == "__main__":
	app.run(debug=True)
