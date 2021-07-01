import sqlite3
from os import error

from tabulate import tabulate
from clint.textui import puts, colored, indent


conn = sqlite3.connect('database.db')
db = conn.cursor()
def create_user_table():
    create_users_table = """ 
    CREATE TABLE users (
        rowid INTEGER PRIMARY KEY ,
        first_name blob NOT NULL, 
        last_name blob NOT NULL,
        email blob UNIQUE NOT NULL,
        password blob NOT NULL, 
        created_at blob NOT NULL); 

   """
    try:
        db.execute(create_users_table)
        response = "Database created"
        return response
    except:
        response = 'Users Table already created'

        return response



def create_message_table():
    create_messages_table = """
    CREATE TABLE messages (
        rowid INTEGER PRIMARY KEY , 
        user_id INTERGER NOT NULL, 
        message text NOT NULL,
        status text NOT NULL, 
        receiver_number text NOT NULL,
        time_scheduled text NOT NULL, 
        created_at text NOT NULL, 
        updated_at text NOT NULL);

    """


    try:
        db.execute(create_messages_table)
        response = "Message table created"
        return response
    except:
        response = 'Message table already created'
        return response



#add message
def add_scheduled_message(user_id,message,receiver_number,time_scheduled,current_date):
    try:
        db.execute("INSERT INTO messages (user_id,message,status, receiver_number,time_scheduled, created_at, updated_at) VALUES (?,?,'Scheduled',?,?,?,?)",(str(user_id),str(message),str(receiver_number),str(time_scheduled),str(current_date),str(current_date)))
        conn.commit() 
        response = "Message added Successfully"
        return response
    except:
        response = "Error adding new message"


#display all messages
def display_all_messages(user_id):
    try:
        db.execute("SELECT * FROM messages WHERE user_id = ?;",(str(user_id)))
        record = db.fetchall()
        headers = ["ROWID", "User ID", "Message", "Status" , "Receiver Number", "Time Scheduled","Created At", "Updates At"]
        print(colored.green(tabulate(record, headers,tablefmt="grid"))) 
        response = "Displaying all message"
        return response
    except:
        response = "User not Found"
        return response

def display_all_scheduled_in_the_database():
    try:
        db.execute("SELECT * FROM messages where status = 'Scheduled';")
        record = db.fetchall()
        headers = ["ROWID", "User ID", "Message", "Status" , "Receiver Number", "Time Scheduled","Created At", "Updates At"]
        print(colored.green(tabulate(record, headers,tablefmt="grid"))) 
        response = "Displaying all message"
        return response
    except:
        response = "User not Found"
        return response




# display scheduled messages
def display_scheduled_messages(user_id):
    try:
        db.execute("SELECT * FROM messages WHERE user_id = ? and status = 'Scheduled';",(str(user_id)))
        record = db.fetchall()  
        headers = ["ROWID", "User ID", "Message", "Status" , "Receiver Number", "Time Scheduled","Created At", "Updates At"]
        print(colored.green(tabulate(record, headers,tablefmt="grid"))) 
        response = "Displaying all message"   
        return response
    except:
        response = "User not Found"
        return response



# display cancelled messages
def display_cancelled_messages(user_id):
    try:
        db.execute("SELECT * FROM messages WHERE user_id = ? and status = 'Cancelled';",(str(user_id)))
        record = db.fetchall()
        headers = ["ROWID", "User ID", "Message", "Status" , "Receiver Number", "Time Scheduled","Created At", "Updates At"]
        print(colored.green(tabulate(record, headers,tablefmt="grid")))
        response = "Displaying all message"
        return response
    except:
        response = "User not Found"
        return response



# select single message
def display_selected_messages(rowid,user_id):
        db.execute("SELECT * FROM messages WHERE rowid = ? and user_id = ?;",(str(rowid),str(user_id)))
        record = db.fetchall()
        #print(record)
        headers = ["ROWID", "User ID", "Message", "Status" , "Receiver Number", "Time Scheduled","Created At", "Updates At"]
        print(colored.green(tabulate(record, headers,tablefmt="grid")))
        if( len(record) == 1 ):
            response = "Message Found"
            return record
        else:
            response = "Message not Found"
            return response



#edit message from single message
def edit_message_message(rowid,current_time,message):
    try:
        db.execute('''UPDATE messages SET message = ? and updated_at = ? WHERE rowid = ?;''',(str(message),str(current_time),str(rowid)))
        conn.commit() 
        response = "Message Successfully Updated"
        return response
    except:
        response = "Message not updated"



#edit status from single message
def edit_message_status(rowid,current_time,status):
    db.execute(''' UPDATE messages SET status = ? and updated_at = ? WHERE rowid = ?;''',(str(status),str(current_time),str(rowid)))
    conn.commit() 
    response = "Status Successfully Updated"
    return error



#edit schedule from single message
def edit_message_schedule(rowid,schedule,current_time):
    db.execute(''' UPDATE messages SET time_scheduled = ? and updated_at = ? WHERE rowid = ?;''',(str(schedule),str(current_time),str(rowid)))
    conn.commit() 
    response = "Schedule Successfully Updated"
    return response   
    