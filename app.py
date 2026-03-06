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
