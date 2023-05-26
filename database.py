from sqlalchemy import create_engine, text

connection_string = "mysql+pymysql://9lw9g504c1c5nc6uben8:pscale_pw_IE5cXzc5AdAfTFJMRCQxTNAKtBT2nruNdKFESrpdxtZ@aws.connect.psdb.cloud:3306/jobstill"
engine = create_engine(connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs
