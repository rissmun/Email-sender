import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail():
    login = input( 'Email: ' )
    password = input( 'Password: ' )
    url = input( 'URL: ' )
    number = int( input( 'Number of messages: ' ) )
    toaddr = input( 'To whom: ' )
    topic = input( 'Subject: ' )
    message = input( 'Text: ' )

    for value in range( number ):
        msg = MIMEMultipart()

        msg[ 'Subject' ] = topic
        msg[ 'From' ] = login
        body = message

        msg.attach( MIMEText( body, 'plain'))

        server = root.SMTP_SSL( url, 465 )
        server.login( login, password )
        server.sendmail( login, toaddr, msg.as_string() )

def main():
    send_mail()

if __name__ == '__main__':
    main()