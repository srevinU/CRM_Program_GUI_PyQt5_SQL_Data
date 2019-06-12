import sqlite3


def create_client_data():

    """CREATE THE CLIENT SQL FILE"""

    conn = sqlite3.connect("data_clients.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE data_clients(
               f_name text,
               l_name text,
               e_mail text,
               mobile_num text,
               home_num text,
               country text,
               street text,
               city text,
               province text,
               postal_code text,
               news_letter text,
               other text
                )""")


def add_client_data(f_name, l_name, e_mail, mobile_num,
                    home_num, country, street, city, province,
                    postal_code, news_letter, other):

    """ADD ALL THE CLIENT INFORMATION IN CLIENT SQL FILE"""

    conn = sqlite3.connect("data_clients.db")

    c = conn.cursor()

    with conn:
        c.execute(("INSERT INTO data_clients VALUES"
                   "(:f_name, "
                   ":l_name, "
                   ":e_mail, "
                   ":mobile_num, "
                   ":home_num, "
                   ":country, "
                   ":street, :city, "
                   ":province, :postal_code, "
                   ":news_letter, "
                   ":other)"),

                  {'f_name': f_name,
                   'l_name': l_name,
                   'e_mail': e_mail,
                   'mobile_num': mobile_num,
                   'home_num': home_num,
                   'country': country,
                   'street': street,
                   'city': city,
                   'province': province,
                   'postal_code': postal_code,
                   'news_letter': news_letter,
                   'other': other})

    conn.commit()
    print(f"{f_name} {l_name} added")


def check_all_client_data():

    """GIVES ALL THE CLIENT DATA"""

    conn = sqlite3.connect("data_clients.db")

    c = conn.cursor()

    with conn:
        for i in c.execute("SELECT * FROM data_clients"):
            print(i)


def check_data_client_selected(l_name):

    """GIVES THE INFORMATION FOR ONLY ONE CLIENT"""

    conn = sqlite3.connect("data_clients.db")

    c = conn.cursor()

    c.execute("SELECT * FROM data_clients WHERE l_name = :l_name", {'l_name': l_name})

    return c.fetchall()


def delete_client_data(f_name, l_name):

    """DELETE THE DATA FOR ONE CLIENT REGARDING HIS FIRST AND LAST NAME"""

    conn = sqlite3.connect("data_clients.db")

    c = conn.cursor()

    with conn:
        c.execute("DELETE from data_clients WHERE f_name = :f_name AND l_name = :l_name",
                  {'f_name': f_name, 'l_name': l_name})

    conn.commit()
    print(f"{f_name} {l_name} has been deleted")


def create_supplier_data():

    """CREATE THE SUPPLIER SQL FILE"""

    conn = sqlite3.connect("data_suppliers.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE data_suppliers(
                name text,
                siret text,
                activity text,
                country text,
                street text,
                city text,
                province text,
                postal_code text,
                
                c1_f_name text,
                c1_l_name text,
                c1_position text,
                c1_mobile_num text,
                c1_company_num text,
                c1_e_mail_address text,
                
                c2_f_name text,
                c2_l_name text,
                c2_position text,
                c2_mobile_num text,
                c2_company_num text,
                c2_e_mail_address text)""")


def add_supplier_data(name, siret, activity, country, street, city,
                      province, postal_code, c1_f_name, c1_l_name,
                      c1_position, c1_mobile_num, c1_company_num,
                      c1_e_mail_address, c2_f_name, c2_l_name, c2_position,
                      c2_mobile_num, c2_company_num, c2_e_mail_address):

    """ADD ALL THE SUPPLIER INFORMATION IN THE SUPPLIER SQL FILE"""

    conn = sqlite3.connect("data_suppliers.db")

    c = conn.cursor()

    with conn:
        c.execute(("INSERT INTO data_suppliers VALUES"
                   "(:name, "
                   ":siret, "
                   ":activity, "
                   ":country, "
                   ":street, "
                   ":city, "
                   ":province, "
                   ":postal_code, "
                   ":c1_f_name, "
                   ":c1_l_name, "
                   ":c1_position, "
                   ":c1_mobile_num, "
                   ":c1_company_num,"
                   ":c1_e_mail_address, "
                   ":c2_f_name, "
                   ":c2_l_name, "
                   ":c2_position, "
                   ":c2_mobile_num, "
                   ":c2_company_num,"
                   ":c2_e_mail_address)"),

                  {'name': name,
                   'siret': siret,
                   'activity': activity,
                   'country': country,
                   'street': street,
                   'city': city,
                   'province': province,
                   'postal_code': postal_code,
                   'c1_f_name': c1_f_name,
                   'c1_l_name': c1_l_name,
                   'c1_position': c1_position,
                   'c1_mobile_num': c1_mobile_num,
                   'c1_company_num': c1_company_num,
                   'c1_e_mail_address': c1_e_mail_address,
                   'c2_f_name': c2_f_name,
                   'c2_l_name': c2_l_name,
                   'c2_position': c2_position,
                   'c2_mobile_num': c2_mobile_num,
                   'c2_company_num': c2_company_num,
                   'c2_e_mail_address': c2_e_mail_address})

        conn.commit()
        print(f"{name} added as supplier.")


def check_all_supplier_data():

    """GIVES ALL THE CLIENT DATA"""

    conn = sqlite3.connect("data_suppliers.db")

    c = conn.cursor()

    with conn:
        for i in c.execute("SELECT * from data_suppliers"):
            print(i)


def delete_supplier_data(name):

    """DELETE THE DATA FOR ONE SUPPLIER REGARDING ITS NAME"""

    conn = sqlite3.connect("data_suppliers.db")

    c = conn.cursor()

    with conn:
        c.execute("DELETE from data_suppliers WHERE name = :name", {"name": name})

    conn.commit()
    print(f"The supplier {name} has been deleted.")


def create_order_data():

    """CREATE THE ORDER SQL FILE"""

    conn = sqlite3.connect("data_orders.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE data_orders(
            ref_order,
            f_name text,
            l_name text,
            c_company text,
            c_f_name text,
            c_l_name text,
            c_ref_num text,
            o_date text,
            ord_ref_p_1 text,
            ord_ref_p_1_qty INTEGER,
            ord_ref_p_2 text,
            ord_ref_p_2_qty INTEGER,
            ord_ref_p_3 text,
            ord_ref_p_3_qty INTEGER,
            ord_ref_p_4 text,
            ord_ref_p_4_qty INTEGER,
            ord_ref_p_5 text,
            ord_ref_p_5_qty INTEGER
    )""")

    print("Data created...")


def add_order_data(ref_order, f_name, l_name, c_company, c_f_name, c_l_name, c_ref_num,
                   o_date, ord_ref_p_1, ord_ref_p_1_qty, ord_ref_p_2, ord_ref_p_2_qty,
                   ord_ref_p_3, ord_ref_p_3_qty, ord_ref_p_4, ord_ref_p_4_qty,
                   ord_ref_p_5, ord_ref_p_5_qty):

    """ADD ALL THE ORDER INFORMATION IN THE ORDER SQL FILE"""

    conn = sqlite3.connect("data_orders.db")

    c = conn.cursor()

    with conn:
        c.execute(("INSERT INTO data_orders VALUES"
                    "(:ref_order, "
                   ":f_name, "
                    ":l_name, "
                    ":c_company, "
                    ":c_f_name, "
                    ":c_l_name, "
                    ":c_ref_num, "
                    ":o_date, "
                    ":ord_ref_p_1, "
                    ":ord_ref_p_1_qty, "
                    ":ord_ref_p_2, "
                    ":ord_ref_p_2_qty, "
                    ":ord_ref_p_3, "
                    ":ord_ref_p_3_qty, "
                    ":ord_ref_p_4, "
                    ":ord_ref_p_4_qty, "
                    ":ord_ref_p_5, "
                    ":ord_ref_p_5_qty)"),

                    {'ref_order': ref_order,
                     'f_name': f_name,
                     'l_name': l_name,
                     'c_company': c_company,
                     'c_f_name': c_f_name,
                     'c_l_name': c_l_name,
                     'c_ref_num': c_ref_num,
                     'o_date': o_date,
                     'ord_ref_p_1': ord_ref_p_1,
                     'ord_ref_p_1_qty': ord_ref_p_1_qty,
                     'ord_ref_p_2': ord_ref_p_2,
                     'ord_ref_p_2_qty': ord_ref_p_2_qty,
                     'ord_ref_p_3': ord_ref_p_3,
                     'ord_ref_p_3_qty': ord_ref_p_3_qty,
                     'ord_ref_p_4': ord_ref_p_4,
                     'ord_ref_p_4_qty': ord_ref_p_4_qty,
                     'ord_ref_p_5': ord_ref_p_5,
                     'ord_ref_p_5_qty': ord_ref_p_5_qty})

    conn.commit()
    print(f"Order {ref_order} has been added by {f_name} {l_name}.")


def check_all_orders_data():

    """DISPLAY ALL THE ORDER DATA"""

    conn = sqlite3.connect("data_orders.db")

    c = conn.cursor()

    with conn:
        for i in c.execute("SELECT * FROM data_orders"):
            print(i)

def check_order_data_before_del(ref_order):

    """DISPLAY ONE ORDER DATA REGARDING ITS REFERENCE NUMBER"""

    conn = sqlite3.connect("data_orders.db")

    c = conn.cursor()

    with conn:

        for i in c.execute("SELECT * FROM data_orders"):
            if i[0] == ref_order:
                return True
            else:
                return False


def delete_order_data(ref_order):

    """DELETE THE DATA FOR THE ORDER SELECTED WITH ITS REFERENCE NUMBER"""

    conn = sqlite3.connect("data_orders.db")

    c = conn.cursor()

    with conn:

        for i in c.execute("SELECT * FROM data_orders"):
            if i[0] == ref_order:
                c.execute(f"DELETE from data_orders WHERE :ref_order = ref_order", {'ref_order': ref_order})
                conn.commit()
                print(f"The order {ref_order} has been deleted.")


def create_order_deleted_data():

    """CREATE THE ORDER DELETED SQL FILE"""

    conn = sqlite3.connect("data_order_deleted.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE data_order_deleted(
    ord_ref text,
    reason text,
    f_name text,
    l_name text,
    date text
    )""")


def add_delete_order_data(ord_ref, reason, f_name, l_name, date):

    """ADD ALL THE ORDER DELETED INFORMATION IN THE ORDER SQL FILE"""

    conn = sqlite3.connect("data_order_deleted.db")

    c = conn.cursor()

    c.execute(("INSERT INTO data_order_deleted VALUES"
              "(:ord_ref,"
              ":reason,"
              ":f_name,"
              ":l_name,"
              ":data)"),
            {'ord_ref': ord_ref,
             'reason': reason,
             'f_name': f_name,
             'l_name': l_name,
             'data': date})

    conn.commit()


def create_mailing_data():

    """CREATE THE EMAILING SQL FILE"""

    conn = sqlite3.connect("data_e_mailing.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE data_e_mailing(
                date text,
                receiver text,
                country text,
                province text,
                subject text,
                qty integer)""")


def add_mailing_data(date, receiver, country, province, subject, qty):

    """ADD ALL THE EMAILING INFORMATION IN THE ORDER SQL FILE"""

    conn = sqlite3.connect("data_e_mailing.db")

    c = conn.cursor()

    c.execute(("INSERT INTO data_e_mailing VALUES("
               ":date, "
               ":receiver, "
               ":country, "
               ":province, "
               ":subject, "
               ":qty)"),
              {'date': date,
               'receiver': receiver,
               'country': country,
               'province': province,
               'subject': subject,
               'qty': qty})

    conn.commit()

def create_actions_data():

    """CREATE THE ACTION SQL FILE"""

    conn = sqlite3.connect("data_actions.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE data_actions(nb integer, action text, date text, f_name text, l_name text)""")

def add_actions_data(nb, action, date, f_name, l_name):

    """ADD ALL THE ACTION INFORMATION IN THE ORDER SQL FILE"""

    conn = sqlite3.connect("data_actions.db")

    c = conn.cursor()

    c.execute(("INSERT INTO data_actions VALUES("
              ":nb, "
              ":action, "
              ":date, "
              ":f_name, "
              ":l_name)"),
            {'nb': nb,
             'action': action,
             'date': date,
             'f_name': f_name,
             'l_name': l_name})

    conn.commit()


def nb_actions_data():

    """GIVES THE NUMBER OF ACTIONS DONE AND IMPLEMENT IN THE ACTION SQL FILE"""

    nb = 0

    conn = sqlite3.connect("data_actions.db")

    c = conn.cursor()

    with conn:
        for i in c.execute("SELECT * FROM data_actions"):
            nb += 1

        return nb










