import os
import mysql.connector
from mysql.connector import Error
from db_connection import create_db_connection


def execute_query(connection, query, data=None):
    """
    Execute a given SQL query on the provided database connection.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    query : str
        The SQL query to execute.
    data : tuple, optional
        The data tuple to pass to the query, for parameterized queries.

    Returns
    -------
    None
    """
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_category(connection, name, description):
    """
    Inserts a new category into the categories table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the category.
    description : str
        The description of the category.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s, %s)
    """
    data = (name, description)
    execute_query(connection, query, data)

def insert_reporter(connection, name, email):
    """
    Inserts a new reporter into the reporters table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the reporter.
    email : str
        The email of the reporter.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO reporters (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def insert_publisher(connection, name, email, phone_number, head_office_add, website, facebook, twitter, linkedin, instagram):
    """
    Inserts a new publisher into the publishers table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the publisher.
    email : str
        The email of the publisher.
    phone_number : str
        The phone number of the publisher.
    head_office_add : str
        The Head office address of publisher.
    website : str
        The website of publisher
    facebook : str
        The fb page link of publisher
    twitter : str
        The twitter link of publisher
    linkedin : str
        The linkedin profile of publisher
    instagram : str
        The insta link of publisher

    Returns
    -------
    None
    """
    query = """
    INSERT INTO publishers (name, email, phone_number, head_office_add, website, facebook, twitter, linkedin, instagram)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (name, email, phone_number, head_office_add, website, facebook, twitter, linkedin, instagram)
    execute_query(connection, query, data)

def insert_news(connection, category_id, reporter_id, publisher_id, datetime, title, body, link):
    """
    Inserts a new news article into the news table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    category_id : int
        The ID of the category.
    reporter_id : int
        The ID of the reporter.
    publisher_id : int
        The ID of the publisher.
    datetime : datetime
        The publication date and time of the news article.
    title : str
        The title of the news article.
    body : str
        The body text of the news article.
    link : str
        The URL link to the full news article.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO news (category_id, reporter_id, publisher_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, reporter_id, publisher_id, datetime, title, body, link)
    execute_query(connection, query, data)

def insert_image(connection, news_id, image_url):
    """
    Inserts a new image into the images table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the image.
    image_url : str
        The URL of the image.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO images (news_id, image_url)
    VALUES (%s, %s)
    """
    data = (news_id, image_url)
    execute_query(connection, query, data)

def insert_summary(connection, news_id, summary_text):
    """
    Inserts a new summary into the summaries table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the summary.
    summary_text : str
        The text of the summary.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO summaries (news_id, summary_text)
    VALUES (%s, %s)
    """
    data = (news_id, summary_text)
    execute_query(connection, query, data)

# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:

        insert_category(conn, "International", "All news related to Internation Current Affairs")
     
        insert_reporter(conn, "Tom H", "tommy@example.com")
  
        insert_publisher(conn, "Prothom Alo", "P_alo@prothomalo.com", "01545464513", "Chittagong", "www.Paloo.com", "www.fb.com/palooo", "www.twitter.com/palooo", "www.linkedin.com/palooo", "www.instagram.com/palooo")
       
        insert_news(conn, 1, 1, 1, "2024-05-03 00:00:00", "News", "Ronaldo wins World Cup", "https://trustmebro.com/sheinews")
    
        insert_image(conn, 1, "https://unsplash.com/photos/macbook-pro-on-brown-wooden-table-ygCCHPr_q2U")

        insert_summary(conn, 1, "This is the summary of Ronaldo's Career: Penalty & tap in; the end")
        
        conn.commit()
        conn.close()
        print("Demo Data Inserted")