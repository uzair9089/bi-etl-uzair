CREATE TABLE IF NOT EXISTS comm.merchants
(
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  organization_id uuid
  
)
WITH (
  OIDS=FALSE
);
ALTER TABLE comm.merchants
  OWNER TO segment;


CREATE TABLE IF NOT EXISTS comm.emails
(
  old_id integer NOT NULL ,
  address character varying,
  message_id character varying,
  sent_at character varying,
  created_at timestamp without time zone NOT NULL,
  updated_at timestamp without time zone NOT NULL,
  publication_id uuid,
  category character varying,
  merchant_id uuid,
  receiver_id uuid,
  receiver_type character varying,
  id uuid NOT NULL DEFAULT uuid_generate_v4()
  
)
WITH (
  OIDS=FALSE
);
ALTER TABLE comm.emails
  OWNER TO segment;


  -- Table: sms

-- DROP TABLE sms;

CREATE TABLE IF NOT EXISTS comm.sms
(
  id serial NOT NULL,
  phone_number character varying,
  message_id character varying,
  sent_at timestamp without time zone,
  receiver_id uuid,
  publication_id uuid,
  created_at timestamp without time zone NOT NULL,
  updated_at timestamp without time zone NOT NULL,
  merchant_id uuid,
  category character varying,
  segments integer NOT NULL DEFAULT 1,
  receiver_type character varying
)
WITH (
  OIDS=FALSE
);
ALTER TABLE comm.sms
  OWNER TO segment;


CREATE TABLE IF NOT EXISTS comm.publications
(
  id uuid NOT NULL ,
  source_uuid uuid NOT NULL,
  source_type character varying NOT NULL,
  entries_count integer DEFAULT 0,
  is_completed boolean NOT NULL DEFAULT false,
  created_at timestamp without time zone NOT NULL,
  updated_at timestamp without time zone NOT NULL,
  merchant_id uuid
)
WITH (
  OIDS=FALSE
);
ALTER TABLE comm.publications
  OWNER TO segment;



  ALTER TABLE ONLY comm.publications
    ADD CONSTRAINT publications_pkey PRIMARY KEY (id,updated_at);


  ALTER TABLE ONLY comm.merchants
    ADD CONSTRAINT merchants_pkey PRIMARY KEY (id);



  ALTER TABLE ONLY comm.sms
    ADD CONSTRAINT sms_pkey PRIMARY KEY (id,updated_at);


  ALTER TABLE ONLY comm.emails
    ADD CONSTRAINT emails_pkey PRIMARY KEY (id,updated_at);

