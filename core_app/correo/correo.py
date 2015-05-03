# -*- coding: utf-8 -*- 
import smtplib 
from email.mime.text import MIMEText
from core_app.correo.sms_sender import SMS_Sender
import mimetypes

#from email.MIMEText import MIMEText
#from email.Encoders import encode_base64

 
class myCorreo:

# Construimos el mensaje simple
    mensaje = MIMEText("""Correo electronico de pruebas
    Verificacion de envio exitosa. Por favor No contestar""")
    mensaje['From']="mysmarthome4101@gmail.com"
    mensaje['To']="ing.rojas.m@gmail.com" #
    mensaje['Subject']="Correo de pruebas"

    def setRemitente(self,remitente):
        self.mensaje['From']=remitente

    def setDestinatario(self,dest):
        self.mensaje['To']=dest

    def enviarGmail(self,tipo_alarma,destinatario,activo):
        
        miMensaje= self.mensaje
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()        
        mailServer.starttls()
        
        mailServer.ehlo()
        
        mailServer.login(self.mensaje['From'],"zvjktuetqawucpqk")

        miMensaje = MIMEText("Correo electronico generado por el activo " + activo +
        ". Verificacion de envio exitosa. Por favor No contestar")
        miMensaje['From']=self.mensaje['From']
        miMensaje['To']=destinatario

        print("enviado a : "+ miMensaje['To'])

        if tipo_alarma == "2" or tipo_alarma == 2:
            miMensaje['Subject']="Alerta critica registrada"
        elif tipo_alarma == "1" or tipo_alarma == 1:
            miMensaje['Subject']="Alerta de Seguridad registrada"
        elif tipo_alarma == "0" or tipo_alarma == 0:
            miMensaje['Subject']="Notificacion de evento registrado"
        
        #print (mailServer.ehlo())

        # Envio del mensaje
        mailServer.sendmail(miMensaje['From'],
	                miMensaje['To'],
                     miMensaje.as_string())
        
        # Envio del sms
        my_sms_client = SMS_Sender(testing_mode=False)
        response = my_sms_client.send_sms(miMensaje.as_string(), "+573202192431")

        # Cierre de la conexion
        mailServer.close()
