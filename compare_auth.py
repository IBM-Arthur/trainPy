#! /usr/bin/python

import os
import getpass

odstablist = ['SODS0.L_MNGED_ENTMT_ORD','SODS0.L_MNGED_ENTMT','SODS0.L_MNGED_ENTMT_EXCPTN','SODS0.L_ENTMT_ACTV_EVLTN','SODS0.L_DCNTRLZ_ENTMT_MST','SENT0.L_DCNTRLZ_ENTMT','FFXT1.RENWL_QUOTE_SCW_INTMDT','SODS0.L_CNTRY_PRICE','SODS0.L_CNTRY_PRICE_TIERD','SODS0.L_MTM_SERIAL_DTL_RECON','SODS0.L_BILLING_RECON','SODS0.L_BILLG_LINE_ITEM_RECON','SODS0.L_BILLG_PRICE_COND_RECON','FFXT1.PRICING_TIERD_ECOM_SCW_INTMDT','SODS0.L_REBATE_VAP_BRAND','FFXT1.SW_PROD_SCW_INTMDT','FFXT1.VAD_TIMELNSS']
odsdblist = ('odsrock','odsrum')

dsstablist = ['ENTL1.ENTMT_SUM_FACT_STAGING','ENTL1.EVOLTN_DTL_FACT_STAGING','ENTL1.EVOLTN_DTL_FACT_PK_TEMP','ENTL1.EVOLTN_DTL_FACT_TEMP_COMPLEX','CDM0.L_CONTACT','CDM1.CONTACT_ERR','DWDM2.GEOGPHY_DIMNSN','ENTL1.EVOLTN_DTL_FACT_TEMP','CDM1.OCV_ATF_DATA','DWDM1.GEOGPHY_DIMNSN','DWDM1.QUOTE_RPT_FACT','DWDM2.QUOTE_RPT_FACT','DWDM1.QUOTE_BILLD_SALES_ORD_ADJMT','FNCC0.L_DFRRD_CLLCTN']
dssdblist = ('dssrug','dssreef')

csdwtablist = ['ENTL0.L_ENTMT_CTRCT','ENTL0.L_SODS2_CUST','ENTL0.L_ENTMT_CNT','ENTL0.L_SERV_DEFINTN_XREF','ENTL0.L_ENTMT_CUST','ENTL0.L_PRODUCT','ENTL0.L_ENTITLEMENT_ESOS','ENTL0.L_BCKLOG_ENTITLEMENT_MIW','ENTL0.L_BCKLOG_PROD_FEATURE_MIW','ENTL0.L_ENTITLEMENT','ENTL0.L_INSTLD_PROD_FEATURE','ENTL0.L_INSTLD_PROD_HW','ENTL0.L_TEMP_ENTMT_INCR_FINAL','ENTL0.L_TEMP_ENTMT_INCR_FINAL','ENTL0.L_CUST_LNV','ENTL0.L_PROD_LNV','ENTL0.L_ENTMT_LNV fixed.','ENTL0.L_INSTLD_PROD_HW_LNV','ENTL0.L_SERVICE_ID_LNV']
csdwdblist = ('csdwrice','csdwrule')

comdict = {}

comdict[odsdblist] = odstablist
comdict[dssdblist] = dsstablist
comdict[csdwdblist] = csdwtablist

username = raw_input('DB username:')
pwd = getpass.getpass('Password:')

os.system('> compare_result.txt')

for dblist,tablist in comdict.iteritems():

    for tab in tablist:
        tabschema = tab.split('.')[0]
        tabname =  tab.split('.')[1]

        for dbname in dblist:
            deli = dbname + ' ' + tab
            deli = deli.center(80,'=')
            os.system('echo ' + deli + '>> compare_result.txt')
            dbconn = 'db2 connect to ' + dbname + ' user ' + username + '  using ' + pwd
            authstr = r"SELECT char(GRANTOR,10) GRANTOR,char(GRANTEE,10) GRANTEE,char(tabschema,8) tabschema,char(tabname,30) tabname,CONTROLAUTH,ALTERAUTH,DELETEAUTH,INDEXAUTH,INSERTAUTH,REFAUTH,SELECTAUTH,UPDATEAUTH  FROM SYSCAT.TABAUTH where tabschema = " + "'" + tabschema + "' and " + " tabname like '" + tabname + "%'"
            authstr = 'db2 ' + '"' + authstr + '"'
            termstr = 'db2 terminate'

            with open('scripts.sh','w') as f:
                f.write(dbconn + '\n')
                f.write(authstr+ '\n')
                f.write(termstr+ '\n')
            f.close()
            os.system('sh scripts.sh >> compare_result.txt')
            os.system('> scripts.sh')
