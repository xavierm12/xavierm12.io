

# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector


def connectionBD():
    print("ENTRO A LA CONEXION")
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host="roundhouse.proxy.rlwy.net",
                #host="viaduct.proxy.rlwy.net",
            port=52172,
            user="root",
            passwd="acBHch-AFEeg3EHb36FG6fEB5G26aFDf",
                #passwd="-D2eD6aDb5Bg6dEbhAAeBB6gd3EheaBg",
            database="railway",
                #database="crud_python",
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True

        )
        if connection.is_connected():
            print("Conexión exitosa a la BD")
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")
