import sqlite3

def setup_db():
    conn = sqlite3.connect("vulns.db", check_same_thread=False)
    cursor = conn.cursor()

    vulns = [
        ("xss", 1),
        ("lfi", 2),
        ("rfi", 3),
        ("hhi", 4),
        ("sqli", 5),
        ("ssti", 6),
    ]

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS USERS (
        USERNAME VARCHAR(255),
        PASSWORD VARCHAR(255)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vulns (
        NAME VARCHAR(255),
        ID INTEGER
    )
    """)

    cursor.executemany("INSERT INTO vulns VALUES (?, ?)", vulns)
    cursor.execute("INSERT INTO USERS VALUES (?, ?)", ("mike", "kaines"))
    cursor.execute("INSERT INTO USERS VALUES (?, ?)", ("admin", "admin"))
    conn.commit()
    conn.close()
