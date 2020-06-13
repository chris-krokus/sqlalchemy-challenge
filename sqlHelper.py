import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

class SQLHelper():

    def __init__(self):
        self.connection_string = "sqlite:///Resources/hawaii.sqlite"
        self.engine = create_engine(self.connection_string)

    def getRainOnDates(self):
        query = f"""
                    Select
                        date, 
                        sum(prcp) as rainfall
                    From 
                        measurement
                    group by
                        date
                    order by 
                        date;
                """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        return df

    def getAllStationData(self):
        query = f"""
                    Select
                        station as station_id,
                        name as station_name,
                        latitude as lat,
                        longitude as long,
                        elevation
                    From 
                        station
                    order by 
                        station_id asc;
                """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        return df

    def getActiveStationData(self):
        query = f"""
                    Select
                        station,
                        date,
                        tobs
                    From 
                        measurement
                    where
                        station = "USC00519397" and
                        date > "2016-08-23"
                    order by 
                        tobs desc;
                """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        #date YYYY-MM-DD must be a string
    def getTempForDate(self, date):
        query = f"""
                    Select
                        date,
                        min(tobs) as min_temp,
                        max(tobs) as max_temp,
                        avg(tobs) as avg_temp
                    From 
                        measurement
                    where
                        date = '{date}'
                """

        conn = self.engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()

        return df    



