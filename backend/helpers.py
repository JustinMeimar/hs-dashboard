from model import Log
from datetime import datetime, timedelta
import random

def generate_random_datetime_in_december(year=2023):
    """ Generate a random datetime in December of the given year. """
    start_date = datetime(year, 12, 1)
    end_date = datetime(year, 12, 31)
    seconds = random.randint(0, int((end_date - start_date).total_seconds()))

    return start_date + timedelta(seconds=seconds)

def generate_random_log():
    """ Generate a random log entry. """
    
    ip = f'192.168.0.{random.randint(1, 255)}'
    datetime = generate_random_datetime_in_december()
    request_method = random.choice(['GET', 'POST', 'PUT', 'DELETE', 'HEAD'])
    paths = ['/home', '/about', '/contact', '/submit', '/login', '/register']
    path = random.choice(paths)
    status = random.choice([200, 301, 400, 404, 500])
    size = random.randint(100, 10000)
    referrers = ['https://example.com', 'https://anotherdomain.com', None]
    referrer = random.choice(referrers)
    user_agents = ['Mozilla/5.0', 'curl/7.64.1', 'PostmanRuntime/7.28.4', None]
    user_agent = random.choice(user_agents)

    return Log(ip=ip, datetime=datetime, request_method=request_method, 
               path=path, status=status, size=size, referrer=referrer, 
               user_agent=user_agent)

def insert_mock_data(session, num_logs=10):

    for _ in range(num_logs):
        log = generate_random_log()
        session.add(log)
    session.commit()