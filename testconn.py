import cx_Oracle
from config import EmConfig
import imaplib


def testDBconn():
    if str.find(EmConfig.CXORACLE_URI, 'URL-de-la-base') == -1:
        try:
            con = cx_Oracle.connect(EmConfig.CXORACLE_URI)
            print('Versión de la Base de Datos: ', con.version)
            print('SQLAlchemy: ', EmConfig.SQLALCHEMY_DATABASE_URI)
            print('Cx_Oracle: ', EmConfig.CXORACLE_URI)
            con.close()
        except cx_Oracle.DatabaseError:
            print(cx_Oracle.DatabaseError)
            print('Credenciales: ', EmConfig.CXORACLE_URI)
    else:
        print('ERROR: Las credenciales de DB no se encontraron')
        print('Credenciales: ', EmConfig.CXORACLE_URI)


def testEMAILconn():
    if EmConfig.IMAP['user'] != 'Usuario-de-IMAP':
        try:
            conn = imaplib.IMAP4_SSL(EmConfig.IMAP['server'], EmConfig.IMAP['port'])
            conn.login(EmConfig.IMAP['user'], EmConfig.IMAP['password'])
            print('Correos totales en INBOX de {}: {}'.format(EmConfig.IMAP['user'], int(conn.select('INBOX')[1][0])))
            conn.close()
            conn.logout()
        except imaplib.IMAP4.error:
            print('ERROR: No se pudo conectar')
            print('Credenciales: ', EmConfig.IMAP)
    else:
        print('ERROR: Las credenciales de Email no se encontraron')
        print('Credenciales: ', EmConfig.IMAP)


if __name__ == '__main__':
    testDBconn()
    testEMAILconn()
