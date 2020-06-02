from data.utils import build_db_info

db_info = {
    "task": {
        "type": "classification",
        "n_classes": 2,
        "n_train": 307511,
        "n_test": 48744,
        "train_class_counts": [282686, 24825],
    },
    "node_type_to_int": {
        "Application": 0,
        "Bureau": 1,
        "BureauBalance": 2,
        "PreviousApplication": 3,
        "CashBalance": 4,
        "CreditBalance": 5,
        "InstallmentPayment": 6,
    },
    "edge_type_to_int": {
        "SELF": 0,
        "BUREAU_TO_APPLICATION": 1,
        "BUREAUBALANCE_TO_BUREAU": 2,
        "PREVIOUSAPPLICATION_TO_APPLICATION": 3,
        "CASHBALANCE_TO_APPLICATION": 4,
        "CASHBALANCE_TO_PREVIOUSAPPLICATION": 5,
        "CREDITBALANCE_TO_APPLICATION": 6,
        "CREDITBALANCE_TO_PREVIOUSAPPLICATION": 7,
        "INSTALLMENTPAYMENT_TO_APPLICATION": 8,
        "INSTALLMENTPAYMENT_TO_PREVIOUSAPPLICATION": 9,
    },
    "node_types_and_features": {
        "Application": {
            "TARGET": {"type": "CATEGORICAL"},
            "NAME_CONTRACT_TYPE": {"type": "CATEGORICAL"},
            "CODE_GENDER": {"type": "CATEGORICAL"},
            "FLAG_OWN_CAR": {"type": "CATEGORICAL"},
            "FLAG_OWN_REALTY": {"type": "CATEGORICAL"},
            "CNT_CHILDREN": {"type": "SCALAR"},
            "AMT_INCOME_TOTAL": {"type": "SCALAR"},
            "AMT_CREDIT": {"type": "SCALAR"},
            "AMT_ANNUITY": {"type": "SCALAR"},
            "AMT_GOODS_PRICE": {"type": "SCALAR"},
            "NAME_TYPE_SUITE": {"type": "CATEGORICAL"},
            "NAME_INCOME_TYPE": {"type": "CATEGORICAL"},
            "NAME_EDUCATION_TYPE": {"type": "CATEGORICAL"},
            "NAME_FAMILY_STATUS": {"type": "CATEGORICAL"},
            "NAME_HOUSING_TYPE": {"type": "CATEGORICAL"},
            "REGION_POPULATION_RELATIVE": {"type": "SCALAR"},
            "DAYS_BIRTH": {"type": "SCALAR"},
            "DAYS_EMPLOYED": {"type": "SCALAR"},
            "DAYS_REGISTRATION": {"type": "SCALAR"},
            "DAYS_ID_PUBLISH": {"type": "SCALAR"},
            "OWN_CAR_AGE": {"type": "SCALAR"},
            "FLAG_MOBIL": {"type": "CATEGORICAL"},
            "FLAG_EMP_PHONE": {"type": "CATEGORICAL"},
            "FLAG_WORK_PHONE": {"type": "CATEGORICAL"},
            "FLAG_CONT_MOBILE": {"type": "CATEGORICAL"},
            "FLAG_PHONE": {"type": "CATEGORICAL"},
            "FLAG_EMAIL": {"type": "CATEGORICAL"},
            "OCCUPATION_TYPE": {"type": "CATEGORICAL"},
            "CNT_FAM_MEMBERS": {"type": "SCALAR"},
            "REGION_RATING_CLIENT": {"type": "CATEGORICAL"},
            "REGION_RATING_CLIENT_W_CITY": {"type": "CATEGORICAL"},
            "WEEKDAY_APPR_PROCESS_START": {"type": "CATEGORICAL"},
            "HOUR_APPR_PROCESS_START": {"type": "CATEGORICAL"},
            "REG_REGION_NOT_LIVE_REGION": {"type": "CATEGORICAL"},
            "REG_REGION_NOT_WORK_REGION": {"type": "CATEGORICAL"},
            "LIVE_REGION_NOT_WORK_REGION": {"type": "CATEGORICAL"},
            "REG_CITY_NOT_LIVE_CITY": {"type": "CATEGORICAL"},
            "REG_CITY_NOT_WORK_CITY": {"type": "CATEGORICAL"},
            "LIVE_CITY_NOT_WORK_CITY": {"type": "CATEGORICAL"},
            "ORGANIZATION_TYPE": {"type": "CATEGORICAL"},
            "EXT_SOURCE_1": {"type": "SCALAR"},
            "EXT_SOURCE_2": {"type": "SCALAR"},
            "EXT_SOURCE_3": {"type": "SCALAR"},
            "APARTMENTS_AVG": {"type": "SCALAR"},
            "BASEMENTAREA_AVG": {"type": "SCALAR"},
            "YEARS_BEGINEXPLUATATION_AVG": {"type": "SCALAR"},
            "YEARS_BUILD_AVG": {"type": "SCALAR"},
            "COMMONAREA_AVG": {"type": "SCALAR"},
            "ELEVATORS_AVG": {"type": "SCALAR"},
            "ENTRANCES_AVG": {"type": "SCALAR"},
            "FLOORSMAX_AVG": {"type": "SCALAR"},
            "FLOORSMIN_AVG": {"type": "SCALAR"},
            "LANDAREA_AVG": {"type": "SCALAR"},
            "LIVINGAPARTMENTS_AVG": {"type": "SCALAR"},
            "LIVINGAREA_AVG": {"type": "SCALAR"},
            "NONLIVINGAPARTMENTS_AVG": {"type": "SCALAR"},
            "NONLIVINGAREA_AVG": {"type": "SCALAR"},
            "APARTMENTS_MODE": {"type": "SCALAR"},
            "BASEMENTAREA_MODE": {"type": "SCALAR"},
            "YEARS_BEGINEXPLUATATION_MODE": {"type": "SCALAR"},
            "YEARS_BUILD_MODE": {"type": "SCALAR"},
            "COMMONAREA_MODE": {"type": "SCALAR"},
            "ELEVATORS_MODE": {"type": "SCALAR"},
            "ENTRANCES_MODE": {"type": "SCALAR"},
            "FLOORSMAX_MODE": {"type": "SCALAR"},
            "FLOORSMIN_MODE": {"type": "SCALAR"},
            "LANDAREA_MODE": {"type": "SCALAR"},
            "LIVINGAPARTMENTS_MODE": {"type": "SCALAR"},
            "LIVINGAREA_MODE": {"type": "SCALAR"},
            "NONLIVINGAPARTMENTS_MODE": {"type": "SCALAR"},
            "NONLIVINGAREA_MODE": {"type": "SCALAR"},
            "APARTMENTS_MEDI": {"type": "SCALAR"},
            "BASEMENTAREA_MEDI": {"type": "SCALAR"},
            "YEARS_BEGINEXPLUATATION_MEDI": {"type": "SCALAR"},
            "YEARS_BUILD_MEDI": {"type": "SCALAR"},
            "COMMONAREA_MEDI": {"type": "SCALAR"},
            "ELEVATORS_MEDI": {"type": "SCALAR"},
            "ENTRANCES_MEDI": {"type": "SCALAR"},
            "FLOORSMAX_MEDI": {"type": "SCALAR"},
            "FLOORSMIN_MEDI": {"type": "SCALAR"},
            "LANDAREA_MEDI": {"type": "SCALAR"},
            "LIVINGAPARTMENTS_MEDI": {"type": "SCALAR"},
            "LIVINGAREA_MEDI": {"type": "SCALAR"},
            "NONLIVINGAPARTMENTS_MEDI": {"type": "SCALAR"},
            "NONLIVINGAREA_MEDI": {"type": "SCALAR"},
            "FONDKAPREMONT_MODE": {"type": "CATEGORICAL"},
            "HOUSETYPE_MODE": {"type": "CATEGORICAL"},
            "TOTALAREA_MODE": {"type": "SCALAR"},
            "WALLSMATERIAL_MODE": {"type": "CATEGORICAL"},
            "EMERGENCYSTATE_MODE": {"type": "CATEGORICAL"},
            "OBS_30_CNT_SOCIAL_CIRCLE": {"type": "SCALAR"},
            "DEF_30_CNT_SOCIAL_CIRCLE": {"type": "SCALAR"},
            "OBS_60_CNT_SOCIAL_CIRCLE": {"type": "SCALAR"},
            "DEF_60_CNT_SOCIAL_CIRCLE": {"type": "SCALAR"},
            "DAYS_LAST_PHONE_CHANGE": {"type": "SCALAR"},
            "FLAG_DOCUMENT_2": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_3": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_4": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_5": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_6": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_7": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_8": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_9": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_10": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_11": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_12": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_13": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_14": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_15": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_16": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_17": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_18": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_19": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_20": {"type": "CATEGORICAL"},
            "FLAG_DOCUMENT_21": {"type": "CATEGORICAL"},
            "AMT_REQ_CREDIT_BUREAU_HOUR": {"type": "SCALAR"},
            "AMT_REQ_CREDIT_BUREAU_DAY": {"type": "SCALAR"},
            "AMT_REQ_CREDIT_BUREAU_WEEK": {"type": "SCALAR"},
            "AMT_REQ_CREDIT_BUREAU_MON": {"type": "SCALAR"},
            "AMT_REQ_CREDIT_BUREAU_QRT": {"type": "SCALAR"},
            "AMT_REQ_CREDIT_BUREAU_YEAR": {"type": "SCALAR"},
        },
        "Bureau": {
            "CREDIT_ACTIVE": {"type": "CATEGORICAL"},
            "CREDIT_CURRENCY": {"type": "CATEGORICAL"},
            "DAYS_CREDIT": {"type": "SCALAR"},
            "CREDIT_DAY_OVERDUE": {"type": "SCALAR"},
            "DAYS_CREDIT_ENDDATE": {"type": "SCALAR"},
            "DAYS_ENDDATE_FACT": {"type": "SCALAR"},
            "AMT_CREDIT_MAX_OVERDUE": {"type": "SCALAR"},
            "CNT_CREDIT_PROLONG": {"type": "SCALAR"},
            "AMT_CREDIT_SUM": {"type": "SCALAR"},
            "AMT_CREDIT_SUM_DEBT": {"type": "SCALAR"},
            "AMT_CREDIT_SUM_LIMIT": {"type": "SCALAR"},
            "AMT_CREDIT_SUM_OVERDUE": {"type": "SCALAR"},
            "CREDIT_TYPE": {"type": "CATEGORICAL"},
            "DAYS_CREDIT_UPDATE": {"type": "SCALAR"},
            "AMT_ANNUITY": {"type": "SCALAR"},
        },
        "BureauBalance": {
            "MONTHS_BALANCE": {"type": "SCALAR"},
            "STATUS": {"type": "CATEGORICAL"},
        },
        "PreviousApplication": {
            "NAME_CONTRACT_TYPE": {"type": "CATEGORICAL"},
            "AMT_ANNUITY": {"type": "SCALAR"},
            "AMT_APPLICATION": {"type": "SCALAR"},
            "AMT_CREDIT": {"type": "SCALAR"},
            "AMT_DOWN_PAYMENT": {"type": "SCALAR"},
            "AMT_GOODS_PRICE": {"type": "SCALAR"},
            "WEEKDAY_APPR_PROCESS_START": {"type": "CATEGORICAL"},
            "HOUR_APPR_PROCESS_START": {"type": "CATEGORICAL"},
            "FLAG_LAST_APPL_PER_CONTRACT": {"type": "CATEGORICAL"},
            "NFLAG_LAST_APPL_IN_DAY": {"type": "CATEGORICAL"},
            "RATE_DOWN_PAYMENT": {"type": "SCALAR"},
            "RATE_INTEREST_PRIMARY": {"type": "SCALAR"},
            "RATE_INTEREST_PRIVILEGED": {"type": "SCALAR"},
            "NAME_CASH_LOAN_PURPOSE": {"type": "CATEGORICAL"},
            "NAME_CONTRACT_STATUS": {"type": "CATEGORICAL"},
            "DAYS_DECISION": {"type": "SCALAR"},
            "NAME_PAYMENT_TYPE": {"type": "CATEGORICAL"},
            "CODE_REJECT_REASON": {"type": "CATEGORICAL"},
            "NAME_TYPE_SUITE": {"type": "CATEGORICAL"},
            "NAME_CLIENT_TYPE": {"type": "CATEGORICAL"},
            "NAME_GOODS_CATEGORY": {"type": "CATEGORICAL"},
            "NAME_PORTFOLIO": {"type": "CATEGORICAL"},
            "NAME_PRODUCT_TYPE": {"type": "CATEGORICAL"},
            "CHANNEL_TYPE": {"type": "CATEGORICAL"},
            "SELLERPLACE_AREA": {"type": "SCALAR"},
            "NAME_SELLER_INDUSTRY": {"type": "CATEGORICAL"},
            "CNT_PAYMENT": {"type": "SCALAR"},
            "NAME_YIELD_GROUP": {"type": "CATEGORICAL"},
            "PRODUCT_COMBINATION": {"type": "CATEGORICAL"},
            "DAYS_FIRST_DRAWING": {"type": "SCALAR"},
            "DAYS_FIRST_DUE": {"type": "SCALAR"},
            "DAYS_LAST_DUE_1ST_VERSION": {"type": "SCALAR"},
            "DAYS_LAST_DUE": {"type": "SCALAR"},
            "DAYS_TERMINATION": {"type": "SCALAR"},
            "NFLAG_INSURED_ON_APPROVAL": {"type": "CATEGORICAL"},
        },
        "CashBalance": {
            "MONTHS_BALANCE": {"type": "SCALAR"},
            "CNT_INSTALMENT": {"type": "SCALAR"},
            "CNT_INSTALMENT_FUTURE": {"type": "SCALAR"},
            "NAME_CONTRACT_STATUS": {"type": "CATEGORICAL"},
            "SK_DPD": {"type": "SCALAR"},
            "SK_DPD_DEF": {"type": "SCALAR"},
        },
        "CreditBalance": {
            "MONTHS_BALANCE": {"type": "SCALAR"},
            "AMT_BALANCE": {"type": "SCALAR"},
            "AMT_CREDIT_LIMIT_ACTUAL": {"type": "SCALAR"},
            "AMT_DRAWINGS_ATM_CURRENT": {"type": "SCALAR"},
            "AMT_DRAWINGS_CURRENT": {"type": "SCALAR"},
            "AMT_DRAWINGS_OTHER_CURRENT": {"type": "SCALAR"},
            "AMT_DRAWINGS_POS_CURRENT": {"type": "SCALAR"},
            "AMT_INST_MIN_REGULARITY": {"type": "SCALAR"},
            "AMT_PAYMENT_CURRENT": {"type": "SCALAR"},
            "AMT_PAYMENT_TOTAL_CURRENT": {"type": "SCALAR"},
            "AMT_RECEIVABLE_PRINCIPAL": {"type": "SCALAR"},
            "AMT_RECIVABLE": {"type": "SCALAR"},
            "AMT_TOTAL_RECEIVABLE": {"type": "SCALAR"},
            "CNT_DRAWINGS_ATM_CURRENT": {"type": "SCALAR"},
            "CNT_DRAWINGS_CURRENT": {"type": "SCALAR"},
            "CNT_DRAWINGS_OTHER_CURRENT": {"type": "SCALAR"},
            "CNT_DRAWINGS_POS_CURRENT": {"type": "SCALAR"},
            "CNT_INSTALMENT_MATURE_CUM": {"type": "SCALAR"},
            "NAME_CONTRACT_STATUS": {"type": "CATEGORICAL"},
            "SK_DPD": {"type": "SCALAR"},
            "SK_DPD_DEF": {"type": "SCALAR"},
        },
        "InstallmentPayment": {
            "NUM_INSTALMENT_VERSION": {"type": "CATEGORICAL"},
            "NUM_INSTALMENT_NUMBER": {"type": "SCALAR"},
            "DAYS_INSTALMENT": {"type": "SCALAR"},
            "DAYS_ENTRY_PAYMENT": {"type": "SCALAR"},
            "AMT_INSTALMENT": {"type": "SCALAR"},
            "AMT_PAYMENT": {"type": "SCALAR"},
        },
    },
    "label_feature": "Application.TARGET",
}

if __name__ == "__main__":
    db_name = "homecreditdefaultrisk"
    test_dp_query = "MATCH (app:Application) WHERE app.TARGET is null RETURN app.SK_ID_CURR ORDER BY app.SK_ID_CURR "
    train_dp_query = "MATCH (app:Application) WHERE app.TARGET is not null RETURN app.SK_ID_CURR ORDER BY app.SK_ID_CURR "
    build_db_info(db_name, db_info, test_dp_query, train_dp_query)
