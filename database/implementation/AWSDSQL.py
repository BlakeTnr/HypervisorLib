from ..CourseRepository import SysSecRepository
import sqlalchemy
from aurora_dsql_sqlalchemy import create_dsql_engine
from sqlalchemy import event
import aurora_dsql_psycopg2 as dsql

from Person import Person
from database.CourseRepository import Semester

class AWSDSQL(SysSecRepository):

    def __init__(self, host, database):
        config = {
            'host': "ijtpmgi6p3mzml46xjhsv7xhx4.dsql.us-east-1.on.aws",
            'region': "us-east-1",
            'user': "admin",
        }

        conn = dsql.connect(**config)
        
        # engine = sqlalchemy.create_engine(f"postgresql://scott:tiger@{host}/{database}")
        # self.databaseConnection = engine.connect()

        # conn = self.databaseConnection
        with conn.cursor() as cur:
            cur.execute("SELECT * from test")
            result = cur.fetchone()
            print(result)

        # engine = create_dsql_engine(
        #     host="ijtpmgi6p3mzml46xjhsv7xhx4.dsql.us-east-1.on.aws",
        #     user="admin",
        #     driver="psycopg2",
        # )

        # print("hi")

    def getSysSecStudents(self, semester: Semester, year: int) -> list[Person]:
        return super().getSysSecStudents(semester, year)
        