import pymysql

def connect_to_rds():
        host="database-1.crsaioae0kin.us-west-1.rds.amazonaws.com"  # Your AWS RDS endpoint
        port=3306  # Default MySQL port
        user="flexonshantanu"  # Your RDS username
        password="SHANTANu23"  # Your RDS password
        database="flexon_practice"  # Your RDS database name
    
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            print("Connection to AWS RDS MySQL successful")
            return connection

        except Exception as e:
            print(f"Error connecting to AWS RDS: {e}")
            return None

#connect_to_rds()

