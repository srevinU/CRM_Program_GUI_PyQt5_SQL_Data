from PyQt5.QtWidgets import *
from App.SQLite_Database import add_client_data, add_actions_data, nb_actions_data
from datetime import datetime


class NewClient(QWidget):

    """THE NewClient APPLICATION WINDOW.

    DISPLAY A WINDOW TO REGISTER ALL THE CLIENT INFORMATION AND SAVE IT IN THE SQL FILE data_clients AND
    IN THE MAIN SQL FILE FOR ALL THE ACTIONS EXECUTED

    REMARK : THE SQL FILE HAS TO BE CREATED BEFORE TO PROCESS, RUN THE FUNCTION FROM A DIFFERENT FILE IN THE FOLDER.
            YOU WILL FIND THE FUNCTION IN THE SQLite_Database.py.
    """

    def __init__(self, Crm):
        super(NewClient, self).__init__()

        """SET THE NewClient WINDOW AND Crm AS THE PARENT"""

        self.Crm = Crm

        self.setWindowTitle("ADD CLIENT")

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.home()

    def home(self):

        """SET ALL THE WIDGETS OF THE NewClient WINDOW"""

        label_client_f_name = QLabel("Client first name:", self)
        self.grid.addWidget(label_client_f_name, 0, 0)
        self.box_client_f_name = QLineEdit(self)
        self.grid.addWidget(self.box_client_f_name, 0, 1)

        label_client_l_name = QLabel("Client last name:", self)
        self.grid.addWidget(label_client_l_name, 1, 0)
        self.box_client_l_name = QLineEdit(self)
        self.grid.addWidget(self.box_client_l_name, 1, 1)

        label_client_email = QLabel("Client email:", self)
        self.grid.addWidget(label_client_email, 2, 0)
        self.box_client_email = QLineEdit(self)
        self.grid.addWidget(self.box_client_email, 2, 1)

        label_client_phone_mobile = QLabel("Client mobile phone:", self)
        self.grid.addWidget(label_client_phone_mobile, 3, 0)
        self.box_client_phone_mobile = QLineEdit(self)
        self.grid.addWidget(self.box_client_phone_mobile, 3, 1)

        label_client_phone_home = QLabel("Client home phone:", self)
        self.grid.addWidget(label_client_phone_home, 4, 0)
        self.box_client_phone_home = QLineEdit(self)
        self.grid.addWidget(self.box_client_phone_home, 4, 1)

        label_client_address = QLabel("Client address:", self)
        self.grid.addWidget(label_client_address, 5, 0)

        label_client_address_country = QLabel("Country/Region:", self)
        self.grid.addWidget(label_client_address_country, 6, 1)
        self.box_client_address_country = QLineEdit(self)
        self.grid.addWidget(self.box_client_address_country, 6, 2)

        label_client_address_street = QLabel("Street address:", self)
        self.grid.addWidget(label_client_address_street, 7, 1)
        self.box_client_address_street = QLineEdit(self)
        self.grid.addWidget(self.box_client_address_street, 7, 2)

        label_client_address_city = QLabel("City:", self)
        self.grid.addWidget(label_client_address_city, 8, 1)
        self.box_client_address_city = QLineEdit(self)
        self.grid.addWidget(self.box_client_address_city, 8, 2)

        label_client_address_province = QLabel("Province/Territory:", self)
        self.grid.addWidget(label_client_address_province, 9, 1)
        self.box_client_address_province = QLineEdit(self)
        self.grid.addWidget(self.box_client_address_province, 9, 2)

        label_client_address_postal = QLabel("Postal code:", self)
        self.grid.addWidget(label_client_address_postal, 10, 1)
        self.box_client_address_postal = QLineEdit(self)
        self.grid.addWidget(self.box_client_address_postal, 10, 2)

        label_client_option = QLabel("Client option:", self)
        self.grid.addWidget(label_client_option, 11, 0)

        self.check_client_option_news_letter = QCheckBox("News letter", self)
        self.grid.addWidget(self.check_client_option_news_letter, 11, 1)

        self.check_client_option_other = QCheckBox("Other", self)
        self.grid.addWidget(self.check_client_option_other, 11, 2)

        self.btn_client_add = QPushButton("Add", self)
        self.grid.addWidget(self.btn_client_add, 12, 0, 12, 3)
        self.btn_client_add.clicked.connect(self.btn_add_on)

    def btn_add_on(self):

        """GET ALL THE DATA AND IMPLEMENT IT IN THE SQL FILE"""

        date = datetime.today()

        if self.check_client_option_news_letter.isChecked():
            news_letter = "True"
        else:
            news_letter = "False"

        if self.check_client_option_other.isChecked():
            option = "True"
        else:
            option = "False"

        choice = QMessageBox.question(self, "Execute", "Do you want to add this client ?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if choice == QMessageBox.Yes:

            add_client_data(self.box_client_f_name.text().upper(),
                            self.box_client_l_name.text().upper(),
                            self.box_client_email.text().lower(),
                            self.box_client_phone_mobile.text().upper(),
                            self.box_client_phone_home.text().upper(),
                            self.box_client_address_country.text().upper(),
                            self.box_client_address_street.text().upper(),
                            self.box_client_address_city.text().upper(),
                            self.box_client_address_province.text().upper(),
                            self.box_client_address_postal.text().upper(),
                            news_letter,
                            option)

            self.Crm.message_box.append(f"The client {self.box_client_f_name.text().upper()} "
                                        f"{self.box_client_l_name.text().upper()} has been added the "
                                        f"{date}")

            nb = nb_actions_data()

            add_actions_data(nb, "CLIENT ADDED", date, self.box_client_f_name.text().upper(), self.box_client_l_name.text().upper())

        else:
            pass

