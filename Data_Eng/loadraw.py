import pandas as pd
from connectRDS import connect_to_rds
import numpy as np

def load_data_into_sp500(csv_file_path):
    # Connect to the database
    connection = connect_to_rds()
    
    if connection:
        cursor = connection.cursor()

        # Load CSV data and replace NaN with None
        data = pd.read_csv(csv_file_path)
        data = data.replace({np.nan: None})

        # Prepare insert query template
        insert_query = """
            INSERT INTO SP500 (
                Exchange, Symbol, Shortname, Longname, Sector, Industry, 
                Currentprice, Marketcap, Ebitda, Revenuegrowth, 
                City, State, Country, Fulltimeemployees, 
                Longbusinesssummary, Weight
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        # Insert each row in the table
        for _, row in data.iterrows():
            values = (
                row['Exchange'], row['Symbol'], row['Shortname'], row['Longname'],
                row['Sector'], row['Industry'], row['Currentprice'], row['Marketcap'],
                row['Ebitda'], row['Revenuegrowth'], row['City'], row['State'],
                row['Country'], row['Fulltimeemployees'], row['Longbusinesssummary'], row['Weight']
            )
            cursor.execute(insert_query, values)

        # Commit the transaction
        connection.commit()
        print("Data loaded into SP500 table successfully")

        # Close cursor and connection
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to database for data loading")

# Run the function with the path to your CSV
if __name__ == "__main__":
    csv_file_path = r"C:\\Flexon\\flexonenv\\sp500_companies.csv"  # Replace with your actual CSV file path
    load_data_into_sp500(csv_file_path)
