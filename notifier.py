import requests
import sys

def notify(torrent_name: str):
    params = {
        'title': 'Torrent Completed',
        'body': torrent_name.upper()
    }
    requests.get(f'http://127.0.0.1:8081/api/v1/sendMessage', params=params)

if __name__ == '__main__':
    notify(str(sys.argv[1]), str(sys.argv[2]))