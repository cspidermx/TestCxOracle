import cx_Oracle
from config import EmConfig, conURI
import imaplib
import sys


def cleanDB(conn):
    cur = conn.cursor()
    cur.execute('delete from email')
    cur.execute('delete from email_to')
    cur.execute('delete from email_from')
    cur.execute('delete from alerta')
    conn.commit()
    cur.close


def testDBconn(clean):
    if str.find(EmConfig.CXORACLE_URI, 'URL-de-la-base') == -1:
        try:
            con = cx_Oracle.connect(EmConfig.CXORACLE_URI)
            print('Versión de la Base de Datos: ', con.version)
            print('SQLAlchemy: ', EmConfig.SQLALCHEMY_DATABASE_URI)
            print('Cx_Oracle: ', EmConfig.CXORACLE_URI)
            # if clean:
                # cleanDB(con)
                # print('Se limpiaron los datos existentes.')
            con.close()
        except cx_Oracle.DatabaseError as abc:
            print(abc)
            print('Credenciales: ', EmConfig.CXORACLE_URI)
        try:
            con = cx_Oracle.connect(conURI)
            print('Versión de la Base de Datos: ', con.version)
            print('Cx_Oracle: ', conURI)
            con.close()
        except cx_Oracle.DatabaseError as abc:
            print(abc)
            print('Credenciales: ', conURI)
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
    arg = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'clean':
            arg = True
    testDBconn(arg)
    testEMAILconn()
