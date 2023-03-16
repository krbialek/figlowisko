

git add -A
git commit -m "Sync tafla"
git push

sudo cp tafla.py /bin/
sudo systemctl restart tafla
