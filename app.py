from flask import Flask,render_template,redirect,url_for,request
from dsa_encryptions import dec1,dec2,dec3,dec4,dec5,dec6,dec7,dec8,dec9,getVigKey
from caesar import caesar_encrypt,caesar_decrypt
from vignere import generateKey
import time

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')
 

@app.route('/output',methods=['POST'])
def background_process():
	which_btn=request.form["decide"]

	if(which_btn=="reset"):
		return redirect(url_for('index'))
	else:
		input_string=request.form["usr_inp"]
		input_key=request.form["usr_inp_key"]
		input_decrypt_key=request.form["usr_inp_dec_key"]
		
		perform=request.form["methods"]

		if(input_string=="" or input_key=="" or input_decrypt_key=="" or perform=="empty"):
			return redirect(url_for('index'))

		# exectime=0
		if(perform=="modvig"):
			vigkey=getVigKey(input_string,input_key)
			vigdeckey=getVigKey(input_string,input_decrypt_key)
			method_encryption=dec1(input_string,vigkey)
			dsa_encryption=dec2(method_encryption)
			original_input=dec3(dsa_encryption,vigdeckey)
			# exectime=execution_time()
			# memused=memory_used()

		elif(perform=="caesar"):
			for i in input_key:
				ascii=ord(i)
				if(ascii<=57 and ascii>=48):
					pass
				else:
					return redirect(url_for('index'))
				
			for i in input_decrypt_key:
				ascii=ord(i)
				if(ascii<=57 and ascii>=48):
					pass
				else:
					return redirect(url_for('index'))

			method_encryption=dec4(input_string,input_key)
			dsa_encryption=dec5(method_encryption)
			original_input=dec6(dsa_encryption,input_decrypt_key)
			# exectime=execution_time()

		elif(perform=="vig"):
			vigkey=generateKey(input_string,input_key)
			vigdeckey=generateKey(input_string,input_decrypt_key)
			method_encryption=dec7(input_string,vigkey)
			dsa_encryption=dec8(method_encryption)
			original_input=dec9(dsa_encryption,vigdeckey)
			# exectime=execution_time()

		
		return render_template('output.html',input_string=input_string,input_key=input_key,input_decrypt_key=input_decrypt_key,method_encryption=method_encryption,dsa_encryption=dsa_encryption,original_input=original_input)

			


if __name__ == '__main__':
    app.run()

