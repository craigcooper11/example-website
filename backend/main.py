from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os
from pydantic import BaseModel

mydb = mysql.connector.connect(
  host=os.environ.get("DATABASE_HOST"),
  user=os.environ.get("DATABASE_USER"),
  password=os.environ.get("DATABASE_PASSWORD"),
  database=os.environ.get("DATABASE_DB")
)
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 2132141234")
mycursor.execute(sql, val)

mydb.commit()
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello_world():
    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()  
    return myresult

class Customer(BaseModel):
    name: str
    description: str | None = None

@app.post("/customer")
def post_customer(customer: Customer):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (customer.name, customer.description)
    mycursor.execute(sql, val)
