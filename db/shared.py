from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np

db = SQLAlchemy()

class Database():
    
    def clear_db(LumberTransaction):
        #Wipe DB incase of old transactions and print out successful delete message
        db.session.query(LumberTransaction).delete()
        print("DB has been successfully wiped")

    def populate_db(file_name,LumberTransaction):

        df = pd.read_excel(file_name)

        columns = ['Open', 'High', 'Low','Close*','Adj Close**', 'Volume']
        
        #Convert date values to a recognizable format and replace all '-' values with NaN

        df[columns] = df[columns].replace("^-$", np.NaN, regex=True)
        df['Date']= pd.to_datetime(df['Date'])

        #Iterrows actually causes an error, which I'd love to mention to you guys
        for i in range(len(df)):
            lumber_transaction = LumberTransaction(date=df.iloc[i]["Date"], open=df.iloc[i]["Open"],high=df.iloc[i]["High"],low=df.iloc[i]["Low"],close=df.iloc[i]["Close*"],adjusted_close=df.iloc[i]["Adj Close**"],volume=df.iloc[i]["Volume"])
            db.session.add(lumber_transaction)
       
        #Commit changes to DB and print out completion message
        db.session.commit()
        print("Finished adding transactions to the DB")
        