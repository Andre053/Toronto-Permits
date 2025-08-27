# sql-lite for managing permits
import sqlite3

db_file = ""
con = sqlite.connect(db_file)

cur = con.cursor()

"""
Each permit can have multiple revisions
Each revision has its own details


TABLES

permit (after last revision)
- Primary key: permit #
- Fields
    - Revision count

revisions 
- 

"""

cur.execute("CREATE TABLE revisions(permit_id, revision_id, permit_type, structure_type, " \
    "work, description, postal, application_date, issued_date, completed_date, status, " \
    "current_use, proposed_use, dwelling_units_created, dwelling_units_lost)")

cur.execute("CREATE TABLE permits(permit_id, revision_count, " \
    "permit_type, structure_type, work, " \
    "description, postal, application_date, issued_date, " \
    "completed_date, status, current_use, proposed_use, " \
    "dwelling_units_created, dwelling_units_lost)")


permit_id = 0
revision_id = 0
permit_type = 0
struct_type = 0
work = ""
description = ""
postal = ""
app_date = ""
issued_date = ""
completed_date = ""
status = ""
current_use = ""
proposed_use = ""
dwelling_units_created = 0
dwelling_units_lost = 0

cur.execute(f"""
    INSERT INTO revisions VALUES
            ({permit_id}, {xyz}, {xyz}, {xyz}, {xyz}, {xyz}, {xyz}, {xyz}, {xyz}, {xyz}, {xyz},  {xyz}, {xyz}, {xyz}, {xyz}, {xyz})

""")

con.commit()