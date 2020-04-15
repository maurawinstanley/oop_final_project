from client import Client
from worker.sqlite import Db_Connection
import io
import sys

def main():
    # database connection
    db_conn = Db_Connection()
    singleton_db = db_conn.get_instance()
    print(singleton_db)

    # user input for image url
    # testing with 'https://sc01.alicdn.com/kf/HTB1FM3eLXXXXXadXXXXq6xXFXXXC/teddy-bear-stuff-toys.jpg_350x350.jpg'
    img_url = sys.argv[1]

    # Client
    client = Client(img_url)
    result = client.to_worker()
    print(result)

if __name__ == '__main__':
    main()