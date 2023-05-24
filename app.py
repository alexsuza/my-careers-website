from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengalaru, India',
    'Salary': 'Rs 15,00, 000'
  },
  {
    'id': 2,
    'title': 'Data scientist',
    'location': 'Delhi, India',
    'Salary': ''
  },
  {
    'id': 3,
    'title': 'Front End Engineer',
    'location': 'Remote',
    'Salary': 'Rs. 15,00, 000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, CA',
    'Salary': 'usd. 120,0000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Alex')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
