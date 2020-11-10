import mysql.connector


config = {
    'database': 'mycommunity_config_test',
    'user': 'yunshequ',
    'password': 'vsAlgXM6OuRQBeTh2TsE',
    'host': 'yl-test-vpc-public.mysql.rds.aliyuncs.com',
    'port': 3306,
    'charset': 'utf8',
    'connection_timeout': 10
}

if __name__ == "__main__":
    con = mysql.connector.connect(**config)
    cur = con.cursor(dictionary=True)
    cur.execute('select 1')
    res = cur.fetchall()
    print res
