from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<job_id>")
def show_job(job_id):
    job = load_job_from_db(job_id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)

@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)