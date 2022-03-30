import os 
import sqlite3 

def create_database(): 
    conn = sqlite3.connect("mydatabase.db") 
    cursor = conn.cursor() 
    # tworzenie tabeli 
    cursor.execute("""CREATE TABLE kluby 
                          (nazwa text, 
                          trener text, 
                          kraj text, 
                          liczba_pilkarzy int,
                          najlepszy_zawodnik text,
                          sponsor_glowny text) 

                       """) 

    # insert  
    temp = [('Manchester City','Maurycy Kowalski','Anglia',28,'Steward John','Jan'),('Bayern Monachium','Julian Nagelsmann','Niemcy',25,'Robert Lewandowski','Jan Neumann')]
    cursor.executemany("INSERT INTO kluby VALUES(?,?,?,?,?,?) ",temp) 

    # zapisanie danych do bazy  
    conn.commit() 

#Wybierz wszystkie rekordy
def select_all(): 
    conn = sqlite3.connect("mydatabase.db") 
    cursor = conn.cursor() 
    sql = "SELECT * FROM kluby"
    cursor.execute(sql) 
    result = cursor.fetchall() 
    cursor.close() 

    conn.close() 

    return result 

def select_club(nazwa):
    conn = sqlite3.connect("mydatabase.db") 
    cursor = conn.cursor() 
    sql = "SELECT * FROM kluby WHERE nazwa = ?"
    cursor.execute(sql, ([nazwa])) 
    result = cursor.fetchall() 
    cursor.close() 
    conn.close() 

    return result 


#Wybierz rekordy z konkretnym sponsorem
def select_all_sponsors(sponsor_glowny): 
    conn = sqlite3.connect("mydatabase.db") 
    cursor = conn.cursor() 
    sql = "SELECT * FROM kluby WHERE sponsor_glowny=?" 
    cursor.execute(sql, [(sponsor_glowny)]) 
    result = cursor.fetchall() 
    cursor.close() 

    conn.close() 

    return result 

#Usuń rekord
def delete_club(nazwa): 
    conn = sqlite3.connect("mydatabase.db") 
    cursor = conn.cursor() 
    sql = "DELETE FROM kluby WHERE nazwa=?"
    cursor.execute(sql, [(nazwa)])
    conn.commit()
    cursor.close() 
    conn.close() 

def update_sponsor_glowny(nazwa, sponsor_glowny): 

    conn = sqlite3.connect("mydatabase.db") 
    
    sql = "UPDATE kluby SET sponsor_glowny = ? WHERE nazwa = ?"
    cursor = conn.cursor() 
    cursor.execute(sql, [(sponsor_glowny),(nazwa)])
    conn.commit() 
    cursor.close() 
    conn.close() 

if __name__ == '__main__': 

    if not os.path.exists("mydatabase.db"): 
        create_database() 
    
    #Pokazywanie wszystkich rekordów
    #print(select_all())

    #Wybrać rekordy z konkretnym sponsorem
    #print(select_all_sponsors('Jan'))

    #Usuwanie klubu
    #print(select_all())
    #print(delete_club('Manchester City'))
    #print(select_all())

    #Zmienianie sponsora
    #print(select_all_sponsors('Jan'))
    #print(update_sponsor_glowny('Manchester City','Piotr Nowak'))
    #print(select_all_sponsors('Jan'))
    #print(select_all_sponsors('Piotr Nowak'))
    