from flask import Flask, render_template, request, redirect, send_file
from so import so_get_jobs
from wwr import wwr_get_jobs, wwr_get_jobs_tr
from remoteok import remoteok_get_jobs
from so_exporter import so_save_to_file
from wwr_exporter import wwr_save_to_file
from remoteok_exporter import remoteok_save_to_file

app = Flask("webscraper")
db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      pass;
    else:
      db[word] = {}
      db[word]["so"] = so_get_jobs(word)
      db[word]["wwr"] = wwr_get_jobs(word)
      db[word]["remoteok"] = remoteok_get_jobs(word)
  else:
    redirect("/")
  temp = []
  [temp.append(i) for i in db[word]["wwr"].keys()]
  wwr_tr = wwr_get_jobs_tr(db[word]["wwr"])
  print(len(wwr_tr))
  return render_template("report.html", 
    searchingBy=word,
    so_resultsNumber=len(db[word]["so"]),
    wwr_resultsNumber=len(wwr_tr),
    remoteok_resultsNumber=len(db[word]["remoteok"]),
    so_jobs = db[word]["so"],
    wwr_jobs_keys = temp,
    wwr_jobs = wwr_tr,
    remoteok_jobs = db[word]["remoteok"]
  )

@app.route("/so_export")
def so_export():
  try:
    word = request.args.get('word')
    print("print"+word)
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    so_save_to_file(word, jobs["so"])
    return send_file(f"./data/so/so_{word}_jobs.csv")
  except:
    return redirect("/")
  
@app.route("/wwr_export")
def wwr_export():
  try:
    word = request.args.get('word')
    file = request.args.get('file')
    if not word or not file:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    wwr_save_to_file(word, jobs["wwr"])
    return send_file(f"./data/wwr/wwr_{word}_{file}.csv")
  except:
    return redirect("/")

@app.route("/remoteok_export")
def remoteok_export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    remoteok_save_to_file(word, jobs["remoteok"])
    return send_file(f"./data/remoteok/remoteok_{word}_jobs.csv")
  except:
    return redirect("/")






    
app.run(host="0.0.0.0")