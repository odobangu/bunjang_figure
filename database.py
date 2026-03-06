import sqlite3

conn=sqlite3.connect("seen.db")
c=conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS items(
id TEXT PRIMARY KEY
)
""")

conn.commit()

def is_new(item_id):

    c.execute("SELECT id FROM items WHERE id=?",(item_id,))
    result=c.fetchone()

    if result:
        return False

    c.execute("INSERT INTO items VALUES(?)",(item_id,))
    conn.commit()

    return True