import sys
def add_numbers(a, b):
 return a + b
if __name__ == "__main__":
 num1 = int(sys.argv[1])
 num2 = int(sys.argv[2])
 result = add_numbers(num1, num2)
 print("=================================")
 print("Addition Result")
 print("=================================")
 print(f"First Number : {num1}")
 print(f"Second Number: {num2}")
 print(f"Sum : {result}")


pipeline {
 agent any
 parameters {
 string(name: 'BRANCH_NAME',
 defaultValue: 'main',
 description: 'Git branch')
 string(name: 'NUM1',
 defaultValue: '10',
 description: 'First Number')
 string(name: 'NUM2',
 defaultValue: '20',
 description: 'Second Number')
 }
 stages {
 stage('Checkout') {
 steps {
 git branch: "${params.BRANCH_NAME}",
 url: 'https://github.com/sumedhachowdary/random1.git'
 }
 }
 stage('Addition Build') {
 steps {
 bat "python add.py ${params.NUM1} ${params.NUM2}"
 }
 }
 }
}

git config --global user.name "Ramitha0275"
git config --global user.email "ramitha.s2023@vitstudent.ac.in"

mkdir git-experiment
cd git-experiment
git init
echo 'print("Hello World")' > app.py
git status
git add app.py
git commit -m "Initial commit: Added greeting application"

git remote add origin https://github.com/Ramitha0275/simple-gitapp.git
git branch -M main
git push -u origin main

echo 'print("Hello Worlds")' > app.py
git checkout -b feature/add-greeting
git add app.py
git commit -m "Added additional greeting message"
git checkout main
git merge feature/add-greeting
git push origin main

git branch
git branch -d feature/add-greeting

git clone https://github.com/Sairamitha/simple-git-app.git
cd simple-git-app

git checkout -b feature/your-name
echo 'print("Hello Worldsyyyyy")' > app.py
git add app.py
git commit -m "Member contribution: Added specific feature"

git checkout main
git pull origin main
