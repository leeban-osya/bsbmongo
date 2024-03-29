import uuid
from src.common.mongo.database import Database
import src.models.bsb.orders.constants as BSBOrderConstants
from datetime import datetime

__author__ = 'nabee1'


class BSBOrder(object):
    def __init__(self, section, area, region, orderID, orderDetailID, orderDate, paymentDate,
                 membershipYear, program, division, userFirstName, userLastName, playerID, playerFirstName,
                 playerLastName, detail, regionPrice, nationalFees, visa_mc_payments, amex_payments, check_payments,
                 visa_mc_refunds, amex_refunds, check_refunds, cc_fee_by_region, cc_fee_by_national, cc_fee_total,
                 payment_to_region, payment_to_national, cancel_date, batchID, bank_acct, pymnt_classification,
                 sourceFile, _id=None):
        self.section = section
        self.area = area
        self.region = region
        self.orderID = orderID
        self.orderDetailID = orderDetailID
        self.orderDate = orderDate
        self.paymentDate = paymentDate
        self.membershipYear = membershipYear
        self.program = program
        self.division = division
        self.userFirstName = userFirstName
        self.userLastName = userLastName
        self.playerID = playerID
        self.playerFirstName = playerFirstName
        self.playerLastName = playerLastName
        self.detail = detail
        self.regionPrice = regionPrice
        self.nationalFees = nationalFees
        self.visa_mc_payments = visa_mc_payments
        self.amex_payments = amex_payments
        self.check_payments = check_payments
        self.visa_mc_refunds = visa_mc_refunds
        self.amex_refunds = amex_refunds
        self.check_refunds = check_refunds
        self.cc_fee_by_region = cc_fee_by_region
        self.cc_fee_by_national = cc_fee_by_national
        self.cc_fee_total = cc_fee_total
        self.payment_to_region = payment_to_region
        self.payment_to_national = payment_to_national
        self.cancel_date = cancel_date
        self.batchID = batchID
        self.bank_acct = bank_acct
        self.pymnt_classification = pymnt_classification
        self.sourceFile = sourceFile
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<BSB Order for Order Detail ID - {}".format(self.orderDetailID)

    def save_to_mongo(self):
        return Database.update(BSBOrderConstants.COLLECTION, {"_id": self._id}, self.json())

    def json(self):
        return {
            "_id": self._id,
            "section": self.section,
            "area": self.area,
            "region": self.region,
            "orderID": self.orderID,
            "orderDetailID": self.orderDetailID,
            "orderDate": self.orderDate,
            "paymentDate": self.paymentDate,
            "membershipYear": self.membershipYear,
            "program": self.program,
            "division": self.division,
            "userFirstName": self.userFirstName,
            "userLastName": self.userLastName,
            "playerID": self.playerID,
            "playerFirstName": self.playerFirstName,
            "playerLastName": self.playerLastName,
            "detail": self.detail,
            "regionPrice": self.regionPrice,
            "nationalFees": self.nationalFees,
            "visa_mc_payments": self.visa_mc_payments,
            "amex_payments": self.amex_payments,
            "check_payments": self.check_payments,
            "visa_mc_refunds": self.visa_mc_refunds,
            "amex_refunds": self.amex_refunds,
            "check_refunds": self.check_refunds,
            "cc_fee_by_region": self.cc_fee_by_region,
            "cc_fee_by_national": self.cc_fee_by_national,
            "cc_fee_total": self.cc_fee_total,
            "payment_to_region": self.payment_to_region,
            "payment_to_national": self.payment_to_national,
            "cancel_date": self.cancel_date,
            "batchID": self.batchID,
            "bank_acct": self.bank_acct,
            "pymnt_classification": self.pymnt_classification,
            "sourceFile": self.sourceFile
        }

    @classmethod
    def find_by_orderDetailID(cls, orderDetailID):
        return [cls(**elem) for elem in Database.find(BSBOrderConstants.COLLECTION, {'orderDetailID': {"$in": orderDetailID}})]


    @classmethod
    def find_by_playerID(cls, playerID):
        return [cls(**elem) for elem in Database.find(BSBOrderConstants.COLLECTION, {'playerID': {"$in": playerID}})]

    @classmethod
    def find_by_multiple_filters(cls, mongo_query):
        return [cls(**elem) for elem in Database.find(BSBOrderConstants.COLLECTION,
                                                      mongo_query)]

    @staticmethod
    def generate_regions_list():
        region_list = sorted(Database.distinct(BSBOrderConstants.COLLECTION, 'region'))
        region_list.insert(0, "All Regions")
        #print(region_list)
        return region_list

