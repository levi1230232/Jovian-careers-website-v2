from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result:
            job = {
                'id': row[0],
                'title': row[1],
                'location': row[2],
                'salary': row[3],
                'currency': row[4],
                'responsibilities': row[5],
                'requirement': row[6]
            }
            jobs.append(job)
    return jobs


def load_job_from_db(job_id):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE id = :job_id")
        result = conn.execute(query, {"job_id": job_id})
        # row = result.all()
        job = result.fetchone()
        if job:
            job_dict = {
                'id': job[0],  # First column (index 0)
                'title': job[1],  # Second column (index 1)
                'location': job[2],  # Third column (index 2)
                'salary': job[3],  # Fourth column (index 3)
                'currency': job[4],  # Fifth column (index 4)
                'responsibilities': job[5],  # Sixth column (index 5)
                'requirement': job[6]  # Seventh column (index 6)
            }
            return job_dict
        else:
            return None

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

        params = {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        }

        conn.execute(query, params)


