# Before running this script, please install the following packages:
# pip install faker mysql-connector-python
# python3 -m pip install pymysql

from faker import Faker
import pymysql
import random
import datetime

fake = Faker()

# Connect to the Aiven database
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=10,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-group6-5200-cs5200-groupproject.h.aivencloud.com",
  password="AVNS_qMXTGKx05ZMAVczfNKG",
  read_timeout=10,
  port=12029,
  user="avnadmin",
  write_timeout=10,
)

cursor = connection.cursor()


def generate_users():
    users = []
    for _ in range(200):
        user_name = fake.first_name_female()
        email = fake.email()
        password = fake.password()
        phone = fake.phone_number()
        gender = "Female"
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=80)
        account_status = random.choice(["Activated", "Deactivated"])
        users.append((
            user_name, email, password, phone,
            gender, birthday, account_status))
    for _ in range(200):
        user_name = fake.first_name_male()
        email = fake.email()
        password = fake.password()
        phone = fake.phone_number()
        gender = "Male"
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=80)
        account_status = random.choice(["Activated", "Deactivated"])
        users.append((
            user_name, email, password, phone,
            gender, birthday, account_status))
    for _ in range(100):
        user_name = fake.first_name()
        email = fake.email()
        password = fake.password()
        phone = fake.phone_number()
        gender = "Other"
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=80)
        account_status = random.choice(["Activated", "Deactivated"])
        users.append((
            user_name, email, password, phone,
            gender, birthday, account_status))
    return users


def insert_users(users):
    query = """
        INSERT INTO User (
        user_name, email, password, phone, gender, birthday, account_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    cursor.executemany(query, users)
    connection.commit()


def generate_events():
    events = []
    for _ in range(50):
        event_category = random.choice(
            ['Concert', 'Festival', 'Sports event', 'Theatre'])
        location = fake.address()
        date = fake.date_between(start_date='-2y', end_date='today')
        description = "Good event"
        event_name = fake.company()
        artist_team = fake.name()
        event_status = "Past"
        events.append((
            event_category, location, date, description,
            event_name, artist_team, event_status))
    for _ in range(40):
        event_category = random.choice(
            ['Concert', 'Festival', 'Sports event', 'Theatre'])
        location = fake.address()
        date = fake.date_between(start_date='today', end_date='+1y')
        description = "Good event"
        event_name = fake.company()
        artist_team = fake.name()
        event_status = "Active"
        events.append((
            event_category, location, date, description,
            event_name, artist_team, event_status))
    for _ in range(10):
        event_category = random.choice(
            ['Concert', 'Festival', 'Sports event', 'Theatre'])
        location = fake.address()
        date = fake.date_between(start_date='-2y', end_date='+1y')
        description = "Good event"
        event_name = fake.company()
        artist_team = fake.name()
        event_status = "Canceled"
        events.append((
            event_category, location, date, description,
            event_name, artist_team, event_status))
    return events


def insert_events(events):
    query = """
        INSERT INTO Event (
        event_category, location, date, description,
        event_name, artist_team, event_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    cursor.executemany(query, events)
    connection.commit()


def generate_orders():
    orders = []

    cursor.execute("SELECT user_id FROM User")
    user_ids = [row['user_id'] for row in cursor.fetchall()]

    for _ in range(1000):
        user_id = random.choice(user_ids)
        purchase_date = fake.date_between(start_date='-2y', end_date='today')
        order_status = random.choice(["Completed", "Failed"])
        payment_method = random.choice(["Credit/debit", "Paypal"])
        orders.append((
            user_id, purchase_date, order_status, payment_method))
    return orders


def insert_orders(orders):
    query = """
    INSERT INTO `Order`
    (user_id, purchase_date, order_status, payment_method)
    VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(query, orders)
    connection.commit()


def generate_tickets():
    tickets = []

    cursor.execute('''
        SELECT event_id FROM Event
        WHERE event_status = 'Active' OR event_status = 'Past'
    ''')
    event_ids = [row['event_id'] for row in cursor.fetchall()]

    for event_id in event_ids:
        general_price = round(random.uniform(50, 300), 2)
        vip_price = round(
            random.uniform(general_price + 50, general_price + 200), 2)
        general_quantity = random.randint(100, 500)
        vip_quantity = random.randint(50, 200)
        tickets.append((
            event_id, 'General Admission', general_price, general_quantity))
        tickets.append((event_id, 'VIP', vip_price, vip_quantity))
    return tickets


def insert_tickets(tickets):
    query = '''
        INSERT INTO Ticket (event_id, ticket_type, price, quantity_available)
        VALUES (%s, %s, %s, %s)
    '''
    cursor.executemany(query, tickets)
    connection.commit()


def generate_order_tickets():
    order_tickets = []

    # use 50 sample events to reduce runtime
    cursor.execute('''
        SELECT event_id, date FROM Event
        WHERE event_status IN ('Past', 'Active')
        ORDER BY RAND()
        LIMIT 50
    ''')
    events = cursor.fetchall()

    # generate 10 pieces of orderticket data for 1 event to reduce runtime
    for event in events:
        event_date = event['date']
        event_id = event['event_id']

        if isinstance(event_date, str):
            event_date = datetime.datetime.strptime(
                event_date, "%Y-%m-%d").date()

        cursor.execute('''
        SELECT order_id, purchase_date FROM `Order`
        WHERE order_status = 'Completed' AND purchase_date < %s
        ORDER BY RAND() LIMIT 10
        ''', (event_date,))
        orders = cursor.fetchall()

        for order in orders:
            order_id = order['order_id']

            cursor.execute('''
                SELECT ticket_id FROM Ticket
                WHERE event_id = %s
            ''', (event_id,))
            ticket_ids = [row['ticket_id'] for row in cursor.fetchall()]

            if ticket_ids:
                ticket_id = random.choice(ticket_ids)
                quantity_purchase = random.randint(1, 5)
                order_tickets.append((order_id, ticket_id, quantity_purchase))

    return order_tickets


def insert_order_tickets(order_tickets):
    query = '''
        INSERT INTO OrderTicket (order_id, ticket_id, quantity_purchase)
        VALUES (%s, %s, %s)
    '''
    cursor.executemany(query, order_tickets)
    connection.commit()


def generate_refunds():
    refunds = []

    cursor.execute('''
        SELECT OT.order_ticket_id, OT.quantity_purchase,
        O.purchase_date, E.date FROM OrderTicket OT
        JOIN `Order` O ON OT.order_id = O.order_id
        JOIN Ticket T ON OT.ticket_id = T.ticket_id
        JOIN Event E ON T.event_id = E.event_id
        ORDER BY RAND() LIMIT 50
    ''')
    result = cursor.fetchall()

    for data in result:
        order_ticket_id = data['order_ticket_id']
        quantity_purchase = data['quantity_purchase']
        purchase_date = data['purchase_date']
        event_date = data['date']

        if isinstance(purchase_date, str):
            purchase_date = datetime.datetime.strptime(
                purchase_date, "%Y-%m-%d").date()
        if isinstance(event_date, str):
            event_date = datetime.datetime.strptime(
                event_date, "%Y-%m-%d").date()
        refund_date = fake.date_between(
            start_date=purchase_date, end_date=event_date)

        quantity_refund = random.randint(1, quantity_purchase)
        refund_status = random.choice(['Approved', 'Declined'])
        refunds.append(
            (order_ticket_id, quantity_refund, refund_date, refund_status))
    return refunds


def insert_refunds(refunds):
    query = '''
        INSERT INTO Refund
        (order_ticket_id, quantity_refund, refund_date, refund_status)
        VALUES (%s, %s, %s, %s)
    '''
    cursor.executemany(query, refunds)
    connection.commit()


def generate_reviews():
    reviews = []

    cursor.execute('''
        SELECT DISTINCT O.user_id, E.event_id FROM `Order` O
        JOIN OrderTicket OT ON O.order_id = OT.order_id
        JOIN Ticket T ON OT.ticket_id = T.ticket_id
        JOIN Event E ON T.event_id = E.event_id
        WHERE E.event_status = 'Past' AND O.purchase_date < E.date
        AND O.order_status = 'Completed' ORDER BY RAND() LIMIT 200
    ''')
    user_events = cursor.fetchall()

    for user_event in user_events:
        user_id = user_event['user_id']
        event_id = user_event['event_id']
        rating = round(random.uniform(1, 10), 1)
        comment = fake.sentence()
        review_status = random.choice(['Approved', 'Rejected', 'Pending'])
        reviews.append((event_id, user_id, rating, comment, review_status))

    return reviews


def insert_reviews(reviews):
    query = '''
        INSERT INTO Review
        (event_id, user_id, rating, comment, review_status)
        VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.executemany(query, reviews)
    connection.commit()


users = generate_users()
insert_users(users)

events = generate_events()
insert_events(events)

orders = generate_orders()
insert_orders(orders)

tickets = generate_tickets()
insert_tickets(tickets)

order_tickets = generate_order_tickets()
insert_order_tickets(order_tickets)

refunds = generate_refunds()
insert_refunds(refunds)

reviews = generate_reviews()
insert_reviews(reviews)
