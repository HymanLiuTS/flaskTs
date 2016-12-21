from flask_mail import Message  
class MyMessage(Message):  
    def __init__(self,subject,sender,recipients):  
        super(MyMessage,self).__init__(subject,sender=sender,recipients=recipients)  
        body='text body'  
  
  
msg=MyMessage('mysubject','879651072@qq.com',['879651072@qq.com'])  
msg.body='text body'  
msg.html='<b>HTML</b> body' 
