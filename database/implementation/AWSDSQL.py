from ..CourseRepository import SysSecRepository
import sqlalchemy
from aurora_dsql_sqlalchemy import create_dsql_engine
from sqlalchemy import event, text
import aurora_dsql_psycopg2 as dsql

from Person import Person
from database.CourseRepository import Semester

class AWSDSQL(SysSecRepository):

    def __init__(self, host, database):

        engine = create_dsql_engine(
            host="ijtpmgi6p3mzml46xjhsv7xhx4.dsql.us-east-1.on.aws",
            user="admin",
            driver="psycopg2",
            sslmode="require"
        )

        with engine.connect() as connection:
            result = connection.execute(text('SELECT * FROM test'))
            print(result.all())

        print("hi")

    def getSysSecStudents(self, semester: Semester, year: int) -> list[Person]:
        return super().getSysSecStudents(semester, year)
        