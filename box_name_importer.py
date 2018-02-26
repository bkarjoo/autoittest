# read the results as in mem sqlite database
import sqlite3

con = 0

def execute_inmem_query(query):

    cur = con.cursor()
    cur.execute(query)
    if query.lstrip().upper().startswith('SELECT'):
        return cur.fetchall()
    return None


def create_in_mem_db():
    global con
    con = sqlite3.connect(":memory:")


def create_box_loc_table():
    q = "CREATE TABLE IF NOT EXISTS box_loc (id INTEGER PRIMARY KEY,box_name TEXT NOT NULL,quant INTEGER NOT NULL,folder INTEGER NOT NULL,box INTEGER NOT NULL)"
    execute_inmem_query(q)


def insert_into_db(box_name, quant, folder, box):
    q = "INSERT INTO box_loc (box_name, quant, folder, box) VALUES ('{}',{},{},{})".format(box_name, quant, folder, box)
    execute_inmem_query(q)


def load_box_loc_csv():
    f = open('box_loc.csv','r')
    while True:
        l = f.readline()
        print l
        if l != '':
            t = l[:-1].split(',')
            insert_into_db(t[3],t[0],t[1],t[2])
        else:
            break


def get_row_count():
    res = execute_inmem_query('SELECT COUNT(*) FROM box_loc')
    return int(res[0][0])


def get_box_address(box_name, quant):
    q = "SELECT folder, box FROM box_loc WHERE box_name = '{}' and quant = {}".format(box_name, quant)
    res = execute_inmem_query(q)
    # print res
    try:
        return res[0]
    except:
        return None

# create_in_mem_db()
# create_box_loc_table()
# load_box_loc_csv()
#print get_row_count()
#print get_box_address('OPG MR_Ratings MR_S_200_Sankalp Krishnan',2)
#
