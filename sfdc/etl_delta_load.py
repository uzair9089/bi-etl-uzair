
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function 1: remove the records existing in the stage database so that it is in sync with the application prod database.
Function 2: load data into staging in incremental way i.e, load data every 3 hours from the ETL
"""

from sf_param import param

# delta_query = { 

# 'contract': "drop table if exists contract_id; create temp table contract_id as select distinct id from sfdc.contract where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_contract where id in (select id from contract_id); insert into stage.s_contract select * from sfdc.contract where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__invoice__c': "drop table if exists onb2__invoice__c_id; create temp table onb2__invoice__c_id as select distinct id from sfdc.onb2__invoice__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__invoice__c where id in (select id from onb2__invoice__c_id); insert into stage.s_onb2__invoice__c select * from sfdc.onb2__invoice__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__item__c': "drop table if exists onb2__item__c_id; create temp table onb2__item__c_id as select distinct id from sfdc.onb2__item__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__item__c where id in (select id from onb2__item__c_id); insert into stage.s_onb2__item__c select * from sfdc.onb2__item__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__subscription__c': "drop table if exists onb2__subscription__c_id; create temp table onb2__subscription__c_id as select distinct id from sfdc.onb2__subscription__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__subscription__c where id in (select id from onb2__subscription__c_id); insert into stage.s_onb2__subscription__c select * from sfdc.onb2__subscription__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__dunningdetail__c': "drop table if exists onb2__dunningdetail__c_id; create temp table onb2__dunningdetail__c_id as select distinct id from sfdc.onb2__dunningdetail__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__dunningdetail__c where id in (select id from onb2__dunningdetail__c_id); insert into stage.s_onb2__dunningdetail__c select * from sfdc.onb2__dunningdetail__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'lead': "drop table if exists lead_id; create temp table lead_id as select distinct id from sfdc.lead where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_lead where id in (select id from lead_id); insert into stage.s_lead select * from sfdc.lead where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'users': "drop table if exists users_id; create temp table users_id as select distinct id from sfdc.users where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_users where id in (select id from users_id); insert into stage.s_users select * from sfdc.users where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'opportunity': "drop table if exists opportunity_id; create temp table opportunity_id as select distinct id from sfdc.opportunity where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_opportunity where id in (select id from opportunity_id); insert into stage.s_opportunity select * from sfdc.opportunity where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'recordtype': "drop table if exists recordtype_id; create temp table recordtype_id as select distinct id from sfdc.recordtype where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_recordtype where id in (select id from recordtype_id); insert into stage.s_recordtype select * from sfdc.recordtype where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__balance__c': "drop table if exists onb2__balance__c_id; create temp table onb2__balance__c_id as select distinct id from sfdc.onb2__balance__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__balance__c where id in (select id from onb2__balance__c_id); insert into stage.s_onb2__balance__c select * from sfdc.onb2__balance__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'account': "drop table if exists account_id; create temp table account_id as select distinct id from sfdc.account where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_account where id in (select id from account_id); insert into stage.s_account select * from sfdc.account where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'contact': "drop table if exists contact_id; create temp table contact_id as select distinct id from sfdc.contact where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_contact where id in (select id from contact_id); insert into stage.s_contact select * from sfdc.contact where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__dunning__c': "drop table if exists onb2__dunning__c_id; create temp table onb2__dunning__c_id as select distinct id from sfdc.onb2__dunning__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__dunning__c where id in (select id from onb2__dunning__c_id); insert into stage.s_onb2__dunning__c select * from sfdc.onb2__dunning__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__dunningrun__c' : "drop table if exists onb2__dunningrun__c_id; create temp table onb2__dunningrun__c_id as select distinct id from sfdc.onb2__dunningrun__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__dunningrun__c where id in (select id from onb2__dunningrun__c_id); insert into stage.s_onb2__dunningrun__c select * from sfdc.onb2__dunningrun__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'asset': "drop table if exists asset_id; create temp table asset_id as select distinct id from sfdc.asset where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_asset where id in (select id from asset_id); insert into stage.s_asset select * from sfdc.asset where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'order': "drop table if exists order_id; create temp table order_id as select distinct id from sfdc.order where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_order where id in (select id from order_id); insert into stage.s_order select * from sfdc.order where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__invoicelineitem__c': "drop table if exists onb2__invoicelineitem__c_id; create temp table onb2__invoicelineitem__c_id as select distinct id from sfdc.onb2__invoicelineitem__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__invoicelineitem__c where id in (select id from onb2__invoicelineitem__c_id); insert into stage.s_onb2__invoicelineitem__c select * from sfdc.onb2__invoicelineitem__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'onb2__invoicerun__c': "drop table if exists onb2__invoicerun__c_id; create temp table onb2__invoicerun__c_id as select distinct id from sfdc.onb2__invoicerun__c where SystemModstamp >='" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"' ; delete from stage.s_onb2__invoicerun__c where id in (select id from onb2__invoicerun__c_id); insert into stage.s_onb2__invoicerun__c select * from sfdc.onb2__invoicerun__c where SystemModstamp >= '" +str(param.start_date) +"' and SystemModstamp < '" +str(param.end_date)+"'; "
# ,'leadhistory': "drop table if exists leadhistory_id; create temp table leadhistory_id as select distinct id from sfdc.leadhistory where createddate >='" +str(param.start_date) +"' and createddate < '" +str(param.end_date)+"' ; delete from stage.s_leadhistory where id in (select id from leadhistory_id); insert into stage.s_leadhistory select * from sfdc.leadhistory where createddate >= '" +str(param.start_date) +"' and createddate < '" +str(param.end_date)+"'; "
# }



delta_query = { 

'order': "drop table if exists order_id; create temp table order_id as select distinct id from sfdc.order where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_order where id in (select id from order_id); insert into stage.s_order select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.order where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'contract': "drop table if exists contract_id; create temp table contract_id as select distinct id from sfdc.contract where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_contract where id in (select id from contract_id); insert into stage.s_contract select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.contract where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'lead': "drop table if exists lead_id; create temp table lead_id as select distinct id from sfdc.lead where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_lead where id in (select id from lead_id); insert into stage.s_lead select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.lead where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__balance__c': "drop table if exists onb2__balance__c_id; create temp table onb2__balance__c_id as select distinct id from sfdc.onb2__balance__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__balance__c where id in (select id from onb2__balance__c_id); insert into stage.s_onb2__balance__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__balance__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__dunning__c': "drop table if exists onb2__dunning__c_id; create temp table onb2__dunning__c_id as select distinct id from sfdc.onb2__dunning__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__dunning__c where id in (select id from onb2__dunning__c_id); insert into stage.s_onb2__dunning__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__dunning__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__dunningdetail__c': "drop table if exists onb2__dunningdetail__c_id; create temp table onb2__dunningdetail__c_id as select distinct id from sfdc.onb2__dunningdetail__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__dunningdetail__c where id in (select id from onb2__dunningdetail__c_id); insert into stage.s_onb2__dunningdetail__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__dunningdetail__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__invoice__c': "drop table if exists onb2__invoice__c_id; create temp table onb2__invoice__c_id as select distinct id from sfdc.onb2__invoice__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__invoice__c where id in (select id from onb2__invoice__c_id); insert into stage.s_onb2__invoice__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__invoice__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__item__c': "drop table if exists onb2__item__c_id; create temp table onb2__item__c_id as select distinct id from sfdc.onb2__item__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__item__c where id in (select id from onb2__item__c_id); insert into stage.s_onb2__item__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__item__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__subscription__c': "drop table if exists onb2__subscription__c_id; create temp table onb2__subscription__c_id as select distinct id from sfdc.onb2__subscription__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__subscription__c where id in (select id from onb2__subscription__c_id); insert into stage.s_onb2__subscription__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__subscription__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'opportunity': "drop table if exists opportunity_id; create temp table opportunity_id as select distinct id from sfdc.opportunity where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_opportunity where id in (select id from opportunity_id); insert into stage.s_opportunity select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.opportunity where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'recordtype': "drop table if exists recordtype_id; create temp table recordtype_id as select distinct id from sfdc.recordtype where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_recordtype where id in (select id from recordtype_id); insert into stage.s_recordtype select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.recordtype where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'users': "drop table if exists users_id; create temp table users_id as select distinct id from sfdc.users where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_users where id in (select id from users_id); insert into stage.s_users select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.users where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'account': "drop table if exists account_id; create temp table account_id as select distinct id from sfdc.account where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_account where id in (select id from account_id); insert into stage.s_account select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.account where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'contact': "drop table if exists contact_id; create temp table contact_id as select distinct id from sfdc.contact where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_contact where id in (select id from contact_id); insert into stage.s_contact select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.contact where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__dunningrun__c': "drop table if exists onb2__dunningrun__c_id; create temp table onb2__dunningrun__c_id as select distinct id from sfdc.onb2__dunningrun__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__dunningrun__c where id in (select id from onb2__dunningrun__c_id); insert into stage.s_onb2__dunningrun__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__dunningrun__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__invoicelineitem__c': "drop table if exists onb2__invoicelineitem__c_id; create temp table onb2__invoicelineitem__c_id as select distinct id from sfdc.onb2__invoicelineitem__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__invoicelineitem__c where id in (select id from onb2__invoicelineitem__c_id); insert into stage.s_onb2__invoicelineitem__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__invoicelineitem__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'onb2__invoicerun__c': "drop table if exists onb2__invoicerun__c_id; create temp table onb2__invoicerun__c_id as select distinct id from sfdc.onb2__invoicerun__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_onb2__invoicerun__c where id in (select id from onb2__invoicerun__c_id); insert into stage.s_onb2__invoicerun__c select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.onb2__invoicerun__c where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'asset': "drop table if exists asset_id; create temp table asset_id as select distinct id from sfdc.asset where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_asset where id in (select id from asset_id); insert into stage.s_asset select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.asset where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"
,'leadhistory': "drop table if exists leadhistory_id; create temp table leadhistory_id as select distinct id from sfdc.leadhistory where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"';delete from stage.s_leadhistory where id in (select id from leadhistory_id); insert into stage.s_leadhistory select * from (select *,row_number() over (partition by id order by systemmodstamp desc) as rnk from sfdc.leadhistory where systemmodstamp>='" +str(param.start_date) +"' and  systemmodstamp<'" +str(param.end_date) +"') as t where rnk=1;"

}
