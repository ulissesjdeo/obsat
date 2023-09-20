cd /home/obsat/obsat
python app.py
filename=data/`ls -Art data/ | tail -n 1`
python request.py $filename