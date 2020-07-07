# -*- coding: utf-8 -*-
from twilio.rest import Client
import os
import csv

"""Sends grades to students via Whatsapp based on csv input"""
class AssessmentSender:
    def __init__(self, filename):
        """Global Variables"""
        self.filename = filename
        self.data = []
        self.filepath = os.path.dirname(os.path.abspath(__file__))
        """Whatsapp API init"""
        account_sid = 'AC690f4022ae33c9e22e1b2daf11fb6b84'
        auth_token = '4a5d557f842f0b68d9a42954c35db340'
        self.client = Client(account_sid, auth_token)
        self.from_whatsapp_number='whatsapp:+14155238886'
        self.to_whatsapp_number='whatsapp:+573006756717'
        """Main methods"""
        self.import_data_from_csv()
        # print self.data[0]
        self.send_data_via_whatsapp()

    def import_data_from_csv(self):
        with open('{}/data/{}.txt'.format(self.filepath, self.filename), mode='rb') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            count = 0
            for row in reader:
                if count != 0:
                    dict = {}
                    dict['id'] = row[0]
                    dict['last_name1'] = row[1]
                    dict['last_name2'] = row[2]
                    dict['first_name1'] = row[3]
                    dict['first_name2'] = row[4]
                    dict['email'] = row[5]
                    dict['phone'] = row[6]
                    if not row[7]:
                        dict['integradas'] = "No reportado"
                    else:
                        dict['integradas'] = row[7]
                    if not row[8]:
                        dict['integradas_obs'] = "Ninguna"
                    else:
                        dict['integradas_obs'] = row[8]
                    if not row[9]:
                        dict['naturales'] = "No reportado"
                    else:
                        dict['naturales'] = row[9]
                    if not row[10]:
                        dict['naturales_obs'] = "Ninguna"
                    else:
                        dict['naturales_obs'] = row[10]
                    if not row[11]:
                        dict['sociales'] = "No reportado"
                    else:
                        dict['sociales'] = row[11]
                    if not row[12]:
                        dict['sociales_obs'] = "Ninguna"
                    else:
                        dict['sociales_obs'] = row[12]
                    if not row[13]:
                        dict['ingles'] = "No reportado"
                    else:
                        dict['ingles'] = row[13]
                    if not row[14]:
                        dict['ingles_obs'] = "Ninguna"
                    else:
                        dict['ingles_obs'] = row[14]
                    if not row[15]:
                        dict['matematicas'] = "No reportado"
                    else:
                        dict['matematicas'] = row[15]
                    if not row[16]:
                        dict['matematicas_obs'] = "Ninguna"
                    else:
                        dict['matematicas_obs'] = row[16]
                    if not row[17]:
                        dict['castellano'] = "No reportado"
                    else:
                        dict['castellano'] = row[17]
                    if not row[18]:
                        dict['castellano_obs'] = "Ninguna"
                    else:
                        dict['castellano_obs'] = row[18]
                    self.data.append(dict)
                count += 1
            self.n_students = count-1

    def send_data_via_whatsapp(self):
        # Iterate through imported data and send corresponding template message
        for i in range(30, self.n_students):
            print("Sending message via whatsapp...")
            self.client.messages.create(body=
                    "Señor padre de familia,\n\n" +
                    "El presente comunicado tiene como finalidad informarle sobre " +
                    "los avances o pendientes que el estudiante {} {} {} {} tiene en "
                        .format(self.data[i]['first_name1'],
                        self.data[i]['first_name2'],
                        self.data[i]['last_name1'],
                        self.data[i]['last_name2']) +
                    "cada una de las áreas, según el reporte de cada docente. En caso " +
                    "de dudas, por favor comuníquese por medio interno con el profesor " +
                    "correspondiente de cada área.\n\n" +
                    "ÁREAS INTEGRADAS: {}. Observaciones: {}.\n"
                        .format(self.data[i]['integradas'],
                        self.data[i]['integradas_obs']) +
                    "CIENCIAS NATURALES: {}. Observaciones: {}.\n"
                        .format(self.data[i]['naturales'],
                        self.data[i]['naturales_obs']) +
                    "CIENCIAS SOCIALES: {}. Observaciones: {}.\n"
                        .format(self.data[i]['sociales'],
                        self.data[i]['sociales_obs']) +
                    "MATEMÁTICAS: {}. Observaciones: {}.\n"
                        .format(self.data[i]['matematicas'],
                        self.data[i]['matematicas_obs']) +
                    "CASTELLANO: {}. Observaciones: {}.\n"
                        .format(self.data[i]['castellano'],
                        self.data[i]['castellano_obs']) +
                    "INGLES: {}. Observaciones: {}.\n\n"
                        .format(self.data[i]['ingles'],
                        self.data[i]['ingles_obs']) +
                    "Por favor recordar que el periodo termina el 12 de Julio. Esperamos " +
                    "se pongan al día con los pendientes para la fecha.\n\n" +
                    "Mireya Manchola\nAsesora de grado 604",
                from_=self.from_whatsapp_number,
                to=self.to_whatsapp_number)

def main():
    course = "604"
    sender = AssessmentSender(course)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("User interruption: {}".format(e))
        sys.stdout.close()
