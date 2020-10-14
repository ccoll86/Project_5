from flask import Flask,jsonify, Response
import math
import hashlib

#instantiate the Flask object
app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome to the Project 5 API"

# mb5 hash converter
@app.route('/md5/<string:input>', methods=['GET'])
def get_md5(input):
	res = hashlib.md5(input.encode())
	return jsonify({'Hash': str(res.hexdigest())})


# Factorial endpoint
@app.route('/factorial/')
def factorial(resl = 'reslult'):
    num = int(input('Input a number to complete factorial: '))
    resl = math.factorial(num)
    return jsonify(
        f'Input: {num}', 
        f'Output: {resl}'

    )

# Fibonacci endpoint
@app.route('/fibonacci/<int:n>', methods=['GET'])
def get_fibonacci(n):
    a,b=0,1
    result1=[]

    while (a<=n):
        print(a,end=' ')
        a,b=b,a+b
        result1.append(print())
    if n<=0:
        print("Incorrect input, please put a positive number")
    
    else:

        return jsonify(
            f'Original Number:{n}',
            f'Fibonacci order:{result1}'
        )


#  prime check endpoint
@app.route('/is-prime/<int:n>')
def prime_check(n):
    if n > 1: 
        for i in range(2, n):
            if (n % i) == 0:
                x = "False"
                break
                
        else:
            x = "True"

        return jsonify(
            f"{x}"
            )



if __name__ == '__main__':
	app.run(debug=True)
