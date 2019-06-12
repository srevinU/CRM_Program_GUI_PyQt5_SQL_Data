from PyQt5.QtWidgets import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from App.SQLite_Database import add_mailing_data, nb_actions_data, add_actions_data
from datetime import datetime
import sqlite3
import smtplib


class EmailSupplier(QWidget):

    """THE EmailSupplier APPLICATION WINDOW.

                DISPLAY A WINDOW TO SEND AN EMAIL CAMPAIGN TO SUPPLIER FROM THE SQL DATA FILE data_suppliers.
                THE CAMPAIGN IS SET WITH TWO INPUT "COUNTRY" AND "PROVINCE", "ALL" CAN BE USED INSTEAD AS "PROVINCE".
                THE EMAIL ADDRESS (FROM) HAS TO BE SET IN THE CURRENT FILE, FUNCTION auto_email.
                SAVE ALL THE EMAILING IN FORMATIONS IN THE SQL FILE add_mailing_data and add_actions_data.
                POSSIBILITY TO ADD AN ATTACHED DOCUMENT.

                REMARK : THE SQL FILE HAS TO BE CREATED BEFORE TO PROCESS, RUN THE FUNCTION FROM A DIFFERENT FILE IN THE FOLDER.
                        YOU WILL FIND THE FUNCTION IN THE SQLite_Database.py.
                """

    def __init__(self, Crm):
        super(EmailSupplier, self).__init__()

        """SET THE EmailSupplier WINDOW AND Crm AS THE PARENT"""

        self.Crm = Crm

        self.setWindowTitle("E-MAILING SUPPLIER")

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.filename = False

        self.home()

    def home(self):

        """SET ALL THE WIDGETS OF THE EmailSupplier WINDOW"""

        label_supplier_address_country = QLabel("Country/Region:", self)
        self.grid.addWidget(label_supplier_address_country, 0, 0)
        self.box_supplier_address_country = QLineEdit(self)
        self.box_supplier_address_country.setClearButtonEnabled(True)
        self.grid.addWidget(self.box_supplier_address_country, 0, 1)

        label_supplier_address_province = QLabel("Province/Territory:", self)
        self.grid.addWidget(label_supplier_address_province, 1, 0)
        self.box_supplier_address_province = QLineEdit(self)
        self.box_supplier_address_province.setClearButtonEnabled(True)
        self.grid.addWidget(self.box_supplier_address_province, 1, 1)

        label_e_mail_subject = QLabel("Email subject:", self)
        self.grid.addWidget(label_e_mail_subject, 2, 0)
        self.box_e_mail_subject = QLineEdit(self)
        self.box_e_mail_subject.setClearButtonEnabled(True)
        self.box_e_mail_subject.setPlaceholderText("Enter your E-mail subject...")
        self.grid.addWidget(self.box_e_mail_subject, 2, 1)

        self.message_box = QTextEdit()
        self.message_box.setPlaceholderText("Enter your E-mail body...")
        self.grid.addWidget(self.message_box, 3, 0, 3, 2)

        self.btn_download_file = QPushButton("Download file", self)
        self.grid.addWidget(self.btn_download_file, 6, 0, 6, 2)
        self.btn_download_file.clicked.connect(self.btn_download)

        btn_send = QPushButton("Send", self)
        self.grid.addWidget(btn_send, 13, 0, 13, 2)
        btn_send.clicked.connect(self.btn_send_on)

    def btn_send_on(self):

        """TAKE ALL THE DATA INPUT IN VARIABLES"""

        country = self.box_supplier_address_country.text()
        province = self.box_supplier_address_province.text()
        self.e_mail_header = self.box_e_mail_subject.text()
        self.e_mail_body = self.message_box.toPlainText()

        self.auto_email()

    def btn_download(self):

        """GIVES THE POSSIBILITY TO DOWNLOAD A DOCUMENT"""

        file = QFileDialog.getOpenFileName(self, "Select File")
        self.filename = file[0]
        self.btn_download_file.setStyleSheet("background-color: green")

    def auto_email(self):

        """SEND THE EMAILS REGARDING THE COUNTRY AND THE PROVINCE AND STORE THE DATA IN THE SQL FILES.
                  REMARK : THE ADDRESS EMAIL (From) HAS TO BE SET, TAKE A LOOK IN THE FUNCTION AND THE '#' COMMENT"""

        self.date = datetime.today()
        self.count_email = 0

        conn = sqlite3.connect("data_suppliers.db")

        c = conn.cursor()

        self.btn_download_file.setStyleSheet("")

        with conn:

            for i in c.execute("SELECT c1_e_mail_address, country, province FROM data_suppliers"):

                if (i[1] == self.box_supplier_address_country.text().upper() and i[2] == self.box_supplier_address_province.text().upper())\
                        or (i[1] == self.box_supplier_address_country.text().upper() and self.box_supplier_address_province.text().upper() == "ALL"):

                    print(f"1:{i}")
                    print(f"2:{i[0]}")
                    print(f"3:{i[1]}")
                    print(f"3:{i[2]}")

                    message = MIMEMultipart()
                    message["from"] = "First name & Last name" #SET YOUR FIRST NAME AND LAST NAME
                    message["to"] = i[0]
                    message["subject"] = self.e_mail_header
                    message.attach(MIMEText(self.e_mail_body))

                    if self.filename:

                        attachment = open(self.filename, "rb")

                        part = MIMEBase("application", "octet_stream")
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header("Content-Disposition", "attachment: filename= " + self.filename)
                        message.attach(part)

                    else:
                        pass

                    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:  # 587 #25
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.login("Your address email", "Your Password") #SET YOUR ADDRESS EMAIL AND YOU PASSWORD AS A STRING
                        smtp.send_message(message)
                        self.count_email += 1
                        print(f"Email {self.count_email} sent...")

                else:
                    pass


            add_mailing_data(self.date, "SUPPLIER", self.box_supplier_address_country.text().upper(),
                             self.box_supplier_address_province.text().upper(), self.e_mail_header.upper(),
                             self.count_email)

            self.Crm.message_box.append(f"{self.count_email} emails have been send to supplier located "
                                        f"in the country {self.box_supplier_address_country.text().upper()} and "
                                        f"the province {self.box_supplier_address_province.text().upper()}")

            nb = nb_actions_data()

            add_actions_data(nb, "SUPPLIER EMAILING(" + str(self.count_email) + ")", self.date,
                             self.box_supplier_address_country.text().upper(),
                             self.box_supplier_address_province.text().upper())