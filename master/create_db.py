import sqlite3

Nome_Data_Base = "crm.db"

def crea_database():
    conn = sqlite3.connect(Nome_Data_Base)
    cursor = conn.cursor()

    # Creazione tabella account
    cursor.execute("""
    CREATE TABLE account (
        vat_code TEXT PRIMARY KEY,
        company_name TEXT NOT NULL,
        street_name TEXT,
        phone TEXT,
        email TEXT,
        fax TEXT
    )
    """)

    # Creazione tabella contatti
    cursor.execute("""
    CREATE TABLE contatti (
        tax_code TEXT PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        vat_code TEXT,
        FOREIGN KEY(vat_code) REFERENCES account(vat_code)
    )
    """)

    
    conn.commit()
    cursor.close()
    conn.close()


