from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Oklahoma City, OK',
    'Salary': 'Rs 15,00, 000'
  },
  {
    'id': 2,
    'title': 'Data scientist',
    'location': 'Dallas, TX',
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
  return render_template('home.html', jobs=JOBS, company_name='Jobstill')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
