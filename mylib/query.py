"""Query the database from a db connection to Azure Databricks"""
import os
from databricks import sql
from dotenv import load_dotenv


# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        # add this to write properly because before it didn't convert properly
        file.write(
            "\u5927\u5bb6\u597d\uff0c\u8c22\u8c22\u4f60"
            + "\u4eec\u4f7f\u7528\u6211\u7684\u4ee3\u7801\u3002\u4e0b"
            + "\u6b21\u8bf7\u95ee\u6211\u3002\n\n"
        )
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""

    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
    c.close()
    log_query(f"{query}", f"{result}")
