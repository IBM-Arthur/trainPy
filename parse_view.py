import sqlparse


# sql = u'select t2.pwsw_row_id, t2.pwsw_id, t1.cust_name_full, t1.adr_1, t1.adr_intrnl, t1.city, state, t1.postal_code, t1.cntry_code_2, t1.bus_prtnr_estblshmt_id, t1.bus_prtnr_id, t1.mod_date, t2.cust_num FROM bprs1.pwsw_customer t1 RIGHT OUTER JOIN bprs1.bus_prtnr_addtnl_sites t2  ON t1.pwsw_row_id = LOWER(t2.pwsw_row_id)  AND t1.pwsw_id = t2.pwsw_id'



sql = ('SELECT t2.pwsw_row_id, t2.pwsw_id, t1.cust_name_full, t1.adr_1, t1.adr_intrnl, t1.city, state, t1.postal_code, t1.cntry_code_2, t1.bus_prtnr_estblshmt_id, t1.bus_prtnr_id, t1.mod_date, t2.cust_num '
       'FROM bprs1.pwsw_customer t1 '
       'RIGHT OUTER JOIN bprs1.bus_prtnr_addtnl_sites t2 ON t1.pwsw_row_id = LOWER(t2.pwsw_row_id) '
       'AND t1.pwsw_id = t2.pwsw_id'
       '-- comment on ')

print(sqlparse.format(sql,reindent=True,keyword_case = 'upper', wrap_after=True))
