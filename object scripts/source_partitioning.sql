
select 'drop table if exists partition.'||tablename||'_y2016m10; create table partition.'||tablename || '_y2016m10 
( CHECK (updated_at::date >= '|| '''2016-10-01'''  || ' and updated_at::date < '|| '''2016-11-01''' || '))INHERITS (' ||schemaname|| '.'||tablename||');
alter table partition.'||tablename||'_y2016m10'||' add constraint pk_'||tablename||'_y2016m10' ||
' primary key (id,updated_at); create index if not exists idx_'||tablename||'_y2016m10' || 
' on partition.'||tablename||'_y2016m10'||'(created_at);' 
from pg_tables where schemaname in ('core','msg','nwsl','comm','pymt')
and tablename not in (
'newsletter_customers', 'employees', 'conversation_senders', 'merchants', 'disputes', 
                    'bank_accounts', 'request_logs', 'stripe_events', 'charges','merchants_pymt','admins_intercom','tags_intercom'
);





select 'create or replace function '||tablename||'_insert_trigger() 
returns trigger as $$
BEGIN 
		IF(NEW.updated_at >= DATE ' || '''2016-09-01''' ||' AND
         NEW.updated_at < DATE '||'''2016-10-01'''||' ) THEN
        INSERT INTO partition.'||tablename||'_y2016m09'||' values (NEW.*);

		ELSIF(NEW.updated_at >= DATE ' || '''2016-10-01''' ||' AND
        NEW.updated_at < DATE '||'''2016-11-01'''||' ) THEN
        INSERT INTO partition.'||tablename||'_y2016m10'||' values (NEW.*);


         ELSE
        RAISE EXCEPTION '||'''Date out of range.  Fix the function!'''||';
    	END IF;
    	RETURN NULL;
END;
$$
LANGUAGE plpgsql;' ||
	'drop trigger if exists insert_'||tablename||' on  '||schemaname||'.'||tablename||
	'; CREATE TRIGGER insert_'||tablename||' 
    BEFORE INSERT ON ' ||schemaname||'.'||tablename||' 
    FOR EACH ROW EXECUTE PROCEDURE '||tablename||'_insert_trigger();'
from pg_tables where schemaname in ('core','msg','nwsl','comm','pymt')
and tablename not in (
'newsletter_customers', 'employees', 'conversation_senders', 'merchants', 'disputes', 
                    'bank_accounts', 'request_logs', 'stripe_events', 'charges','merchants_pymt','admins_intercom','tags_intercom'
)


-- index creator script for the uuid containing tables
SELECT ' drop index if exists '||table_schema||'.idx_'||table_name||'_'||column_name ||';create index idx_'||table_name||'_'||column_name || ' on '||table_schema|| '.'||table_name||' using btree ('||column_name||');'
FROM information_schema.columns
where table_schema = 'partition' and table_name like 's_%'
and data_type = 'uuid'
