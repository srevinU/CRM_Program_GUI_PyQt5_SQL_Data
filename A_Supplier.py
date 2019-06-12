from PyQt5.QtWidgets import *
from App.SQLite_Database import add_supplier_data, nb_actions_data, add_actions_data
from datetime import datetime


class NewSupplier(QWidget):

    """THE NewSupplier APPLICATION WINDOW.

        DISPLAY A WINDOW TO REGISTER ALL THE SUPPLIER INFORMATION AND SAVE IT IN THE SQL FILE data_suppliers AND
        IN THE MAIN SQL FILE FOR ALL THE ACTIONS EXECUTED

        REMARK : THE SQL FILE HAS TO BE CREATED BEFORE TO PROCESS, RUN THE FUNCTION FROM A DIFFERENT FILE IN THE FOLDER.
                YOU WILL FIND THE FUNCTION IN THE SQLite_Database.py.
        """

    def __init__(self, Crm):
        super(NewSupplier, self).__init__()

        """SET THE NewClient WINDOW AND Crm AS THE PARENT"""

        self.Crm = Crm

        self.setWindowTitle("ADD SUPPLIER")

        self.grid = QGridLayout()

        self.setLayout(self.grid)

        self.home()

    def home(self):

        """SET ALL THE WIDGETS OF THE NewClient WINDOW"""

        label_supplier_name = QLabel("Supplier name:")
        self.grid.addWidget(label_supplier_name, 0, 0)
        self.box_supplier_name = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_name, 0, 1)

        label_supplier_siret = QLabel("SIRET/INSEE number:")
        self.grid.addWidget(label_supplier_siret, 1, 0)
        self.box_supplier_siret = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_siret, 1, 1)

        label_supplier_activity = QLabel("Supplier Activity:")
        self.grid.addWidget(label_supplier_activity, 2, 0)
        self.box_supplier_activity = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_activity, 2, 1)

        label_supplier_address = QLabel("Supplier address:", self)  # SUPPLIER ADDRESS INFO
        self.grid.addWidget(label_supplier_address, 3, 0)

        label_supplier_address_country = QLabel("Country/Region:", self)
        self.grid.addWidget(label_supplier_address_country, 4, 1)
        self.box_supplier_address_country = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_address_country, 4, 2)

        label_supplier_address_street = QLabel("Street address:", self)
        self.grid.addWidget(label_supplier_address_street, 5, 1)
        self.box_supplier_address_street = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_address_street, 5, 2)

        label_supplier_address_city = QLabel("City:", self)
        self.grid.addWidget(label_supplier_address_city, 6, 1)
        self.box_supplier_address_city = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_address_city, 6, 2)

        label_supplier_address_province = QLabel("Province/Territory:", self)
        self.grid.addWidget(label_supplier_address_province, 7, 1)
        self.box_supplier_address_province = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_address_province, 7, 2)

        label_supplier_address_postal = QLabel("Postal code:", self)
        self.grid.addWidget(label_supplier_address_postal, 8, 1)
        self.box_supplier_address_postal = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_address_postal, 8, 2)

        label_supplier_contact1 = QLabel("Contact 1:") # CONTACT 1 INFO
        self.grid.addWidget(label_supplier_contact1, 9, 0)

        label_supplier_contact1_f_name = QLabel("First name:")
        self.grid.addWidget(label_supplier_contact1_f_name, 10, 1)
        self.box_supplier_contact1_f_name = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact1_f_name, 10, 2)

        label_supplier_contact1_l_name = QLabel("Last name:")
        self.grid.addWidget(label_supplier_contact1_l_name, 11, 1)
        self.box_supplier_contact1_l_name = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact1_l_name, 11, 2)

        label_supplier_contact1_position = QLabel("Position:")
        self.grid.addWidget(label_supplier_contact1_position, 12, 1)
        self.box_supplier_contact1_position = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact1_position, 12, 2)

        label_supplier_contact1_mobile_phone = QLabel("Mobile phone:")
        self.grid.addWidget(label_supplier_contact1_mobile_phone, 13, 1)
        self.box_supplier_contact1_mobile_phone = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact1_mobile_phone, 13, 2)

        label_supplier_contact1_company_phone = QLabel("Company phone:")
        self.grid.addWidget(label_supplier_contact1_company_phone, 14, 1)
        self.box_supplier_contact1_company_phone = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact1_company_phone, 14, 2)

        label_supplier_contact1_e_mail = QLabel("Email:")
        self.grid.addWidget(label_supplier_contact1_e_mail, 15, 1)
        self.box_supplier_contact1_e_mail = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact1_e_mail, 15, 2)

        label_supplier_contact2 = QLabel("Contact 2:") # CONTACT 2 INFO
        self.grid.addWidget(label_supplier_contact2, 16, 0)

        label_supplier_contact2_f_name = QLabel("First name:")
        self.grid.addWidget(label_supplier_contact2_f_name, 17, 1)
        self.box_supplier_contact2_f_name = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact2_f_name, 17, 2)

        label_supplier_contact2_l_name = QLabel("Last name:")
        self.grid.addWidget(label_supplier_contact2_l_name, 18, 1)
        self.box_supplier_contact2_l_name = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact2_l_name, 18, 2)

        label_supplier_contact2_position = QLabel("Position:")
        self.grid.addWidget(label_supplier_contact2_position, 19, 1)
        self.box_supplier_contact2_position = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact2_position, 19, 2)

        label_supplier_contact2_mobile_phone = QLabel("Mobile phone:")
        self.grid.addWidget(label_supplier_contact2_mobile_phone, 20, 1)
        self.box_supplier_contact2_mobile_phone = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact2_mobile_phone, 20, 2)

        label_supplier_contact2_company_phone = QLabel("Company phone:")
        self.grid.addWidget(label_supplier_contact2_company_phone, 21, 1)
        self.box_supplier_contact2_company_phone = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact2_company_phone, 21, 2)

        label_supplier_contact2_e_mail = QLabel("Email:")
        self.grid.addWidget(label_supplier_contact2_e_mail, 22, 1)
        self.box_supplier_contact2_e_mail = QLineEdit(self)
        self.grid.addWidget(self.box_supplier_contact2_e_mail, 22, 2)

        self.btn_supplier_add = QPushButton("Add", self)
        self.grid.addWidget(self.btn_supplier_add, 23, 0, 23, 3)
        self.btn_supplier_add.clicked.connect(self.btn_add_on)

    def btn_add_on(self):

        """GET ALL THE DATA AND IMPLEMENT IT IN THE SQL FILE"""

        date = datetime.today()

        add_supplier_data(self.box_supplier_name.text().upper(),
                          self.box_supplier_siret.text().upper(),
                          self.box_supplier_activity.text().upper(),
                          self.box_supplier_address_country.text().upper(),
                          self.box_supplier_address_street.text().upper(),
                          self.box_supplier_address_city.text().upper(),
                          self.box_supplier_address_province.text().upper(),
                          self.box_supplier_address_postal.text().upper(),

                          self.box_supplier_contact1_f_name.text().upper(),
                          self.box_supplier_contact1_l_name.text().upper(),
                          self.box_supplier_contact1_position.text().upper(),
                          self.box_supplier_contact1_mobile_phone.text(),
                          self.box_supplier_contact1_company_phone.text(),
                          self.box_supplier_contact1_e_mail.text(),

                          self.box_supplier_contact2_f_name.text().upper(),
                          self.box_supplier_contact2_l_name.text().upper(),
                          self.box_supplier_contact2_position.text().upper(),
                          self.box_supplier_contact2_mobile_phone.text(),
                          self.box_supplier_contact2_company_phone.text(),
                          self.box_supplier_contact2_e_mail.text())

        self.Crm.message_box.append(f"The supplier {self.box_supplier_name.text().upper()} "
                                    f"has been added the {date}")

        nb = nb_actions_data()

        add_actions_data(nb, "SUPPLIER ADDED", date, self.box_supplier_name.text().upper(),
                         self.box_supplier_siret.text().upper())
