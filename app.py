from flask import Flask, request, render_template
from updatejson import HandleJson
import os
from emailapi import EmailAPI
from handleexcel import HandleExcel
app = Flask(__name__)

handle_json = HandleJson()
send_mail = EmailAPI()
handle_excel = HandleExcel()
class Main:

    @app.route('/')

    def index():
        return render_template('form.html')

    @app.route('/submit-form', methods =['POST'])
    def submit_form():
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        data = {
            'firstname': firstname,
            'lastname': lastname
        }
        handle_json.update_json(form_details_to_update=data, current_json_file='formdetails.json')
        form_details_path = os.path.join(os.getcwd(), 'formdetails.json')
        handle_excel.form_details_to_excel(form_details_path)
        send_mail.send_email_with_attachment('formdetailsexcel.xlsx')

        
        return 'submited successfully'
        

        
    

if __name__ =='__main__':
    app.run(debug=True)