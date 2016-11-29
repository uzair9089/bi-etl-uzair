
CREATE OR REPLACE FUNCTION table_partition_creator(bdt varchar(30) , edt varchar(30))
RETURNS TABLE (
txt   text )  -- visible as OUT parameter inside and outside function
AS
$func$
BEGIN
   RETURN QUERY
	select 'drop table if exists partition.s_'||tablename||'_'||substring(replace(replace(bdt,'-',''),'''',''),1,6)||'; create table partition.s_'||tablename||'_'||substring(replace(replace(bdt,'-',''),'''',''),1,6)||
	'( CHECK (created_at::date >= '|| bdt
|| ' and created_at::date < '|| edt||'))INHERITS ('|| 'stage.s_'||tablename||');
alter table partition.s_'||tablename||'_'||substring(replace(replace(bdt,'-',''),'''',''),1,6)||' add constraint pk_s_'||tablename||'_'||substring(replace(replace(bdt,'-',''),'''',''),1,6)||
' primary key (id); create index if not exists idx_s_'||tablename||'_'||substring(replace(replace(bdt,'-',''),'''',''),1,6)|| 
' on partition.s_'||tablename||'_'||substring(replace(replace(bdt,'-',''),'''',''),1,6)||'(created_at);'
from pg_tables where schemaname in ('core','msg','pymt','comm','nwsl')
and tablename not in (
'newsletter_customers', 'employees', 'conversation_senders', 'merchants', 'disputes', 
                    'bank_accounts', 'request_logs', 'stripe_events', 'charges','merchants_pymt','admins_intercom','tags_intercom','merchant_permissions'
);

 -- note the potential ambiguity 
END
$func$  LANGUAGE plpgsql;


select 'create or replace function stage_'||tablename||'_insert_trigger() 
returns trigger as $$   
        
        BEGIN

        IF(NEW.created_at >= DATE ' || '''2016-11-01''' ||' AND
        NEW.created_at < DATE '||'''2016-12-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201611'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2016-12-01''' ||' AND
        NEW.created_at < DATE '||'''2017-01-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201612'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2017-01-01''' ||' AND
        NEW.created_at < DATE '||'''2017-02-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201701'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2016-10-01''' ||' AND
        NEW.created_at < DATE '||'''2016-11-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201610'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2016-09-01''' ||' AND
        NEW.created_at < DATE '||'''2016-10-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201609'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2016-08-01''' ||' AND
        NEW.created_at < DATE '||'''2016-09-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201608'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2016-07-01''' ||' AND
        NEW.created_at < DATE '||'''2016-08-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201607'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2016-06-01''' ||' AND
        NEW.created_at < DATE '||'''2016-07-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201606'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2016-05-01''' ||' AND
        NEW.created_at < DATE '||'''2016-06-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201605'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2016-04-01''' ||' AND
        NEW.created_at < DATE '||'''2016-05-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201604'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2016-03-01''' ||' AND
        NEW.created_at < DATE '||'''2016-04-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201603'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2016-02-01''' ||' AND
        NEW.created_at < DATE '||'''2016-03-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201602'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2016-01-01''' ||' AND
        NEW.created_at < DATE '||'''2016-02-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201601'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-12-01''' ||' AND
        NEW.created_at < DATE '||'''2016-01-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201512'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-11-01''' ||' AND
        NEW.created_at < DATE '||'''2015-12-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201511'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-10-01''' ||' AND
        NEW.created_at < DATE '||'''2015-11-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201510'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-09-01''' ||' AND
        NEW.created_at < DATE '||'''2015-10-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201509'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-08-01''' ||' AND
        NEW.created_at < DATE '||'''2015-09-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201508'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-07-01''' ||' AND
        NEW.created_at < DATE '||'''2015-08-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201507'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2015-06-01''' ||' AND
        NEW.created_at < DATE '||'''2015-07-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201506'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-05-01''' ||' AND
        NEW.created_at < DATE '||'''2015-06-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201505'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-04-01''' ||' AND
        NEW.created_at < DATE '||'''2015-05-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201504'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2015-03-01''' ||' AND
        NEW.created_at < DATE '||'''2015-04-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201503'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-02-01''' ||' AND
        NEW.created_at < DATE '||'''2015-03-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201502'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2015-01-01''' ||' AND
        NEW.created_at < DATE '||'''2015-02-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201501'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-12-01''' ||' AND
        NEW.created_at < DATE '||'''2015-01-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201412'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-11-01''' ||' AND
        NEW.created_at < DATE '||'''2014-12-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201411'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-10-01''' ||' AND
        NEW.created_at < DATE '||'''2014-11-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201410'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-09-01''' ||' AND
        NEW.created_at < DATE '||'''2014-10-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201409'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-08-01''' ||' AND
        NEW.created_at < DATE '||'''2014-09-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201408'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-07-01''' ||' AND
        NEW.created_at < DATE '||'''2014-08-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201407'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2014-06-01''' ||' AND
        NEW.created_at < DATE '||'''2014-07-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201406'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-05-01''' ||' AND
        NEW.created_at < DATE '||'''2014-06-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201405'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-04-01''' ||' AND
        NEW.created_at < DATE '||'''2014-05-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201404'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2014-03-01''' ||' AND
        NEW.created_at < DATE '||'''2014-04-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201403'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-02-01''' ||' AND
        NEW.created_at < DATE '||'''2014-03-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201402'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2014-01-01''' ||' AND
        NEW.created_at < DATE '||'''2014-02-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201401'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-12-01''' ||' AND
        NEW.created_at < DATE '||'''2014-01-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201312'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2013-11-01''' ||' AND
        NEW.created_at < DATE '||'''2013-12-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201311'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-10-01''' ||' AND
        NEW.created_at < DATE '||'''2013-11-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201310'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-09-01''' ||' AND
        NEW.created_at < DATE '||'''2013-10-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201309'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-08-01''' ||' AND
        NEW.created_at < DATE '||'''2013-09-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201308'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-07-01''' ||' AND
        NEW.created_at < DATE '||'''2013-08-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201307'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2013-06-01''' ||' AND
        NEW.created_at < DATE '||'''2013-07-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201306'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-05-01''' ||' AND
        NEW.created_at < DATE '||'''2013-06-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201305'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-04-01''' ||' AND
        NEW.created_at < DATE '||'''2013-05-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201304'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2013-03-01''' ||' AND
        NEW.created_at < DATE '||'''2013-04-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201303'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-02-01''' ||' AND
        NEW.created_at < DATE '||'''2013-03-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201302'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2013-01-01''' ||' AND
        NEW.created_at < DATE '||'''2013-02-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201301'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2012-12-01''' ||' AND
        NEW.created_at < DATE '||'''2013-01-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201212'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-11-01''' ||' AND
        NEW.created_at < DATE '||'''2012-12-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201211'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-10-01''' ||' AND
        NEW.created_at < DATE '||'''2012-11-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201210'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-09-01''' ||' AND
        NEW.created_at < DATE '||'''2012-10-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201209'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-08-01''' ||' AND
        NEW.created_at < DATE '||'''2012-09-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201208'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-07-01''' ||' AND
        NEW.created_at < DATE '||'''2012-08-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201207'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2012-06-01''' ||' AND
        NEW.created_at < DATE '||'''2012-07-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201206'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-05-01''' ||' AND
        NEW.created_at < DATE '||'''2012-06-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201205'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-04-01''' ||' AND
        NEW.created_at < DATE '||'''2012-05-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201204'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2012-03-01''' ||' AND
        NEW.created_at < DATE '||'''2012-04-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201203'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-02-01''' ||' AND
        NEW.created_at < DATE '||'''2012-03-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201202'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2012-01-01''' ||' AND
        NEW.created_at < DATE '||'''2012-02-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201201'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-12-01''' ||' AND
        NEW.created_at < DATE '||'''2012-01-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201112'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-11-01''' ||' AND
        NEW.created_at < DATE '||'''2011-12-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201111'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-10-01''' ||' AND
        NEW.created_at < DATE '||'''2011-11-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201110'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-09-01''' ||' AND
        NEW.created_at < DATE '||'''2011-10-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201109'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-08-01''' ||' AND
        NEW.created_at < DATE '||'''2011-09-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201108'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-07-01''' ||' AND
        NEW.created_at < DATE '||'''2011-08-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201107'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2011-06-01''' ||' AND
        NEW.created_at < DATE '||'''2011-07-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201106'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-05-01''' ||' AND
        NEW.created_at < DATE '||'''2011-06-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201105'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-04-01''' ||' AND
        NEW.created_at < DATE '||'''2011-05-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201104'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2011-03-01''' ||' AND
        NEW.created_at < DATE '||'''2011-04-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201103'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-02-01''' ||' AND
        NEW.created_at < DATE '||'''2011-03-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201102'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2011-01-01''' ||' AND
        NEW.created_at < DATE '||'''2011-02-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201101'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-12-01''' ||' AND
        NEW.created_at < DATE '||'''2011-01-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201012'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2010-11-01''' ||' AND
        NEW.created_at < DATE '||'''2010-12-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201011'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-10-01''' ||' AND
        NEW.created_at < DATE '||'''2010-11-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201010'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-09-01''' ||' AND
        NEW.created_at < DATE '||'''2010-10-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201009'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-08-01''' ||' AND
        NEW.created_at < DATE '||'''2010-09-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201008'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-07-01''' ||' AND
        NEW.created_at < DATE '||'''2010-08-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201007'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2010-06-01''' ||' AND
        NEW.created_at < DATE '||'''2010-07-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201006'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-05-01''' ||' AND
        NEW.created_at < DATE '||'''2010-06-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201005'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-04-01''' ||' AND
        NEW.created_at < DATE '||'''2010-05-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201004'||' values (NEW.*);


        ELSIF(NEW.created_at >= DATE ' || '''2010-03-01''' ||' AND
        NEW.created_at < DATE '||'''2010-04-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201003'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-02-01''' ||' AND
        NEW.created_at < DATE '||'''2010-03-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201002'||' values (NEW.*);

        ELSIF(NEW.created_at >= DATE ' || '''2010-01-01''' ||' AND
        NEW.created_at < DATE '||'''2010-02-01'''||' ) THEN
        INSERT INTO partition.s_'||tablename||'_201001'||' values (NEW.*);

                
        ELSE
        RAISE EXCEPTION '||'''Date out of range for '||tablename||'.  Fix the function!'''||';
    	END IF;
    	RETURN NULL;
END;
$$
LANGUAGE plpgsql;' ||
' drop trigger if exists stage_insert_'||tablename||' on stage.s_'||tablename||';CREATE TRIGGER stage_insert_'||tablename||' 
BEFORE INSERT ON stage.s_'||tablename||' 
FOR EACH ROW EXECUTE PROCEDURE stage_'||tablename||'_insert_trigger();'
from pg_tables where schemaname in ( 'nwsl' ,'core' ,'msg' ,'pymt' ,'comm')
and tablename not in (
'newsletter_customers', 'employees', 'conversation_senders', 'merchants', 'disputes', 
                    'bank_accounts', 'request_logs', 'stripe_events', 'charges','merchants_pymt','admins_intercom','tags_intercom','merchant_permissions'
)







