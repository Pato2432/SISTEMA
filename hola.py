import sqlite3
con = sqlite3.connect("Notas.db")
cursor = con.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute("DROP TABLE IF EXISTS Pagos;")
cursor.execute("""
CREATE TABLE Pagos (
    CodigoEstu VARCHAR(10),
    Tarjeta INT,
    CCV INT,
    FechaExp VARCHAR(5),
    PRIMARY KEY (CodigoEstu),
    FOREIGN KEY (CodigoEstu) REFERENCES Estudiantes(Codigo)
);
""")
con.commit()
con.close()
