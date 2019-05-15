#!/usr/bin/python3

import imaplib, getpass, re, email

def connect():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    email = input("Enter your gmail address: ")
    password = getpass.getpass("Enter pass: ")
    imap.login(email, password)
    return imap

if __name__ == '__main__':
    mail = connect()
    mail.select('inbox')
    
    type, data = mail.search(None, '(UNSEEN)')

    count = 0
    for num in data[0].split():
        mail.store(num, '+FLAGS', '\\Seen')
        print("Done " + str(count))
        count+=1



