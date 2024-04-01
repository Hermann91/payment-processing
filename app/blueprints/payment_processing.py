import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.blueprints.ticket_generator import TicketGenerator
from app.blueprints.sender_email import EmailSender
import pandas as pd


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
    for email in email_list:
        boleto = ticket_generator(data_frame)
        send_email(email, boleto)
