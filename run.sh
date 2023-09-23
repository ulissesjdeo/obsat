cd /home/obsat/obsat || exit
python app.py
filename=data/$(find /sample_directory -type f -exec ls -t1 {} + | head -1)
python request.py "$filename"