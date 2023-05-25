from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Oklahoma City, OK',
    'Salary': 'USD $145,000'
  },
  {
    'id': 2,
    'title': 'QA Specialist',
    'location': 'Charlotte, NC',
    'Salary': 'USD $95,0000'
  },
  {
    'id': 3,
    'title': 'Data scientist',
    'location': 'Dallas, TX',
    'Salary': 'USD 155,000'
  },
  {
    'id': 4,
    'title': 'Front End Engineer',
    'location': 'Remote',
    'Salary': 'USD $125,000'
  },
  {
    'id': 5,
    'title': 'Backend Engineer',
    'location': 'San Francisco, CA',
    'Salary': 'USD $130,0000'
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
