import cx_Oracle
import vars


def buildconnstring():
    DBCRED = {'dburl': vars.DB_URL or 'URL-de-la-base',
              'dbport': vars.DB_PORT or 'PUERTO-de-la-base',
              'dbservice': vars.DB_SERVICE or 'SERVICENAME-de-la-base',
              'dbuser': vars.DB_USER or 'USER-de-la-base',
              'dbpass': vars.DB_PASS or 'PASS-de-la-base'}
    dnsStr = cx_Oracle.makedsn(DBCRED['dburl'], DBCRED['dbport'], DBCRED['dbservice'])
    dnsStr = dnsStr.replace('SID', 'SERVICE_NAME')
    connect_str = 'oracle://' + DBCRED['dbuser'] + ':' + DBCRED['dbpass'] + '@' + dnsStr
    connect_str_alt = DBCRED['dbuser'] + '/' + DBCRED['dbpass'] + '@' + DBCRED['dburl'] + ':' +  \
                      DBCRED['dbport'] + '/' + DBCRED['dbservice']
    return connect_str, connect_str_alt


class EmConfig(object):
    SQLALCHEMY_DATABASE_URI, CXORACLE_URI = buildconnstring()
    IMAP = {'user': vars.IMAP_USER or 'Usuario-de-IMAP',
            'password': vars.IMAP_PASS or 'Password-de-IMAP',
            'server': vars.IMAP_SRV or 'Servidor-de-IMAP',
            'port': vars.IMAP_PORT or 'Puerto-de-IMAP'}


