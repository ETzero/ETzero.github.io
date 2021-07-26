
echo '--------pre deploy start--------'
python3 pre_deploy.py
echo '--------pre deploy end--------'

echo '--------upload files start--------'
# git init
git add .
git status
git commit -m 'auto update NoteBook'
echo '--------commit successfully--------'

git push -u origin master
#git push -u https://github.com/ETzero/ETzero.github.io.git master
echo '--------push to GitHub successfully--------'

