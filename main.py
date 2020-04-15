from client import Client
from worker.sqlite import Db_Connection

def main():
    # database connection
    db_conn = Db_Connection()
    singleton_db = db_conn.get_instance()
    print(singleton_db)

    # Client
    client = Client('https://sc01.alicdn.com/kf/HTB1FM3eLXXXXXadXXXXq6xXFXXXC/teddy-bear-stuff-toys.jpg_350x350.jpg')
    result = client.to_worker()
    print(result)

if __name__ == '__main__':
    main()