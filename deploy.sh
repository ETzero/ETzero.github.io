echo '--------upload files start--------'

python3 pre_deploy.py

# git init
git add .
git status
git commit -m 'auto update NoteBook'
echo '--------commit successfully--------'

git push -u https://github.com/ETzero/ETzero.github.io.git master
echo '--------push to GitHub successfully--------'

