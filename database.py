from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os

engine = create_engine(os.getenv("DB_STRING"))


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), val=id)

  rows = result.all()
  if len(rows) == 0:
    return None
  else:
    return dict(rows[0])


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )

    conn.execute(query,
                 job_id=job_id,
                 full_name=data['full_name'],
                 email=data['email'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'],
                 linkedin_url=data['linkedin_url'])
