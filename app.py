from flask import Flask,render_template,redirect,url_for,request
from dsa_encryptions import dec1,dec2,dec3,getVigKey,execution_time
import time

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')
 

@app.route('/output',methods=['POST'])
def background_process():
	input_string=request.form["usr_inp"]
	input_key=request.form["usr_inp_key"]
	input_decrypt_key=request.form["usr_inp_dec_key"]
	which_btn=request.form["decide"]

	vigkey=getVigKey(input_string,input_key)
	vigdeckey=getVigKey(input_string,input_decrypt_key)
	vignere_encryption=dec1(input_string,vigkey)
	dsa_encryption=dec2(vignere_encryption)
	original_input=dec3(dsa_encryption,vigdeckey)
	exectime=execution_time()
	
	if(which_btn=="encrypt"):	
		return render_template('output.html',exectime=exectime,input_string=input_string,input_key=input_key,input_decrypt_key=input_decrypt_key,vignere_encryption=vignere_encryption,dsa_encryption=dsa_encryption,original_input=original_input)
	else:
		return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
