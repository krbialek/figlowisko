

git add -A
git commit -m "Sync tafla"
git push

cp tafla.py /bin/
sudo systemctl restart tafla
