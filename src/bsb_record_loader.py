import csv
from src.models.bsb.orders.order import BSBOrder
from src.common.mongo.database import Database
import os

#print()
Database.initialize()

with open("common/jan_sample_orders.csv") as csvFile:
    csvreader = csv.reader(csvFile, delimiter=",")
    next(csvreader)
    for line in csvreader:
        bsb_order = BSBOrder(
                            section=line[0],
                            area=line[1],
                            region=line[2],
                            orderID=line[3],
                            orderDetailID=line[4],
                            orderDate=line[5],
                            paymentDate=line[6],
                            membershipYear=line[7],
                            program=line[8],
                            division=line[9],
                            userFirstName=line[10],
                            userLastName=line[11],
                            playerID=line[12],
                            playerFirstName=line[13],
                            playerLastName=line[14],
                            detail=line[15],
                            regionPrice=line[16],
                            nationalFees=line[17],
                            visa_mc_payments=line[18],
                            amex_payments=line[19],
                            check_payments=line[20],
                            visa_mc_refunds=line[21],
                            amex_refunds=line[22],
                            check_refunds=line[23],
                            cc_fee_by_region=line[24],
                            cc_fee_by_national=line[25],
                            cc_fee_total=line[26],
                            payment_to_region=line[27],
                            payment_to_national=line[28],
                            cancel_date=line[29],
                            batchID=line[30],
                            bank_acct=line[31],
                            pymnt_classification=line[32],
                            sourceFile=line[33]
                            )
        bsb_order.save_to_mongo()

print("Done")
