#!/usr/bin/env python3
"""Sends an email with 'Gutentag, World!' using smtplib.

Demo only — configure SMTP_HOST, SMTP_PORT, FROM_ADDR, TO_ADDR, and
credentials via environment variables before running.

Run: python3 send.py
"""
import os
import smtplib
from email.message import EmailMessage

SMTP_HOST = os.environ.get('SMTP_HOST', 'localhost')
SMTP_PORT = int(os.environ.get('SMTP_PORT', '587'))
SMTP_USER = os.environ.get('SMTP_USER', '')
SMTP_PASS = os.environ.get('SMTP_PASS', '')
FROM_ADDR = os.environ.get('FROM_ADDR', 'gutentag@example.com')
TO_ADDR = os.environ.get('TO_ADDR', 'world@example.com')

msg = EmailMessage()
msg['Subject'] = 'Gutentag, World!'
msg['From'] = FROM_ADDR
msg['To'] = TO_ADDR
msg.set_content('Gutentag, World!')

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
    if SMTP_USER:
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)
    print(f'Email sent to {TO_ADDR}')
