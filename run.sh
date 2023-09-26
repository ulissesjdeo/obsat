cd /home/obsat/obsat || exit
python app.py
filename=data/$(find data/ -type f -exec ls -t1 {} + | head -1)
filename=$(echo "$filename" | sed -e 's/data\///')
python request.py "$filename"