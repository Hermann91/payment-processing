import threading

import pandas as pd

from app.blueprints.sender_email import EmailSender
from app.blueprints.ticket_generator import TicketGenerator


def extract_email_list(data_frame_email_list):
    emai_colum_list = data_frame_email_list['email'].tolist()
    return emai_colum_list


def ticket_generator(data_client):
    return TicketGenerator(data_client).generator_tickets()


def send_email(recipient_email, boleto):
    EmailSender().send_email(recipient_email, boleto)


def main_csv_processing(csv_file):
    data_frame = pd.read_csv(csv_file)
    email_list = extract_email_list(data_frame)
    threads = []

    for email in email_list:
        # Cria uma nova thread para processar cada email
        thread = threading.Thread(target=process_email, args=(email, data_frame))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def process_email(email, data_frame):
    boleto = ticket_generator(data_frame)
    send_email(email, boleto)

