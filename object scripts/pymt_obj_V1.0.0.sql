

CREATE TABLE IF NOT EXISTS pymt.bank_accounts
(
  id text NOT NULL,
  merchant_id uuid NOT NULL,
  object text,
  account_holder_name text,
  account_holder_type text,
  last4 text NOT NULL,
  bank_name text,
  country text NOT NULL,
  currency text NOT NULL,
  default_for_currency boolean NOT NULL,
  status text,
  routing_number text,
  meta jsonb NOT NULL DEFAULT '{}'::jsonb,
  created integer NOT NULL
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pymt.bank_accounts
  OWNER TO segment;



CREATE TABLE IF NOT EXISTS pymt.charges
(
  stripe_charge_id text,
  merchant_id uuid NOT NULL,
  meta jsonb NOT NULL DEFAULT '{}'::jsonb,
  amount integer NOT NULL,
  currency text NOT NULL,
  created timestamp(0) without time zone NOT NULL,
  status text NOT NULL,
  failure_code text,
  failure_message text,
  refund_ids text[] NOT NULL DEFAULT ARRAY[]::text[],
  amount_refunded integer NOT NULL DEFAULT 0,
  customer_name text,
  customer_email text,
  customer_address jsonb DEFAULT '{}'::jsonb,
  description text,
  services jsonb NOT NULL DEFAULT '[]'::jsonb,
  captured boolean DEFAULT true,
  origin text,
  id uuid NOT NULL ,
  payments jsonb NOT NULL DEFAULT '[]'::jsonb,
  gastrofix_charge_id uuid
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pymt.charges
  OWNER TO segment;


CREATE TABLE IF NOT EXISTS pymt.disputes
(
  id text NOT NULL,
  status text NOT NULL,
  reason text,
  amount integer NOT NULL,
  currency text NOT NULL,
  created timestamp(0) without time zone NOT NULL,
  due_by timestamp(0) without time zone,
  has_evidence boolean DEFAULT false,
  past_due boolean DEFAULT false,
  submission_count integer NOT NULL,
  charge_id uuid
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pymt.disputes
  OWNER TO segment;



CREATE TABLE IF NOT EXISTS pymt.request_logs
(
  id integer NOT NULL ,
  path text NOT NULL,
  verb text NOT NULL,
  "user" text,
  ip_address text,
  "timestamp" timestamp without time zone NOT NULL,
  params jsonb
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pymt.request_logs
  OWNER TO segment;


CREATE TABLE IF NOT EXISTS pymt.stripe_events
(
  id text NOT NULL,
  object text NOT NULL,
  api_version text,
  created integer NOT NULL,
  data jsonb NOT NULL,
  livemode boolean NOT NULL,
  pending_webhooks integer NOT NULL,
  request text,
  type text NOT NULL
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pymt.stripe_events
  OWNER TO segment;


ALTER TABLE ONLY pymt.stripe_events
    ADD CONSTRAINT stripe_events_pkey PRIMARY KEY (id);


ALTER TABLE ONLY pymt.request_logs
    ADD CONSTRAINT request_logs_pkey PRIMARY KEY (id);


ALTER TABLE ONLY pymt.charges
    ADD CONSTRAINT charges_pkey PRIMARY KEY (id);



ALTER TABLE ONLY pymt.bank_accounts
    ADD CONSTRAINT bank_accounts_pkey PRIMARY KEY (id);


ALTER TABLE ONLY pymt.disputes
    ADD CONSTRAINT disputes_pkey PRIMARY KEY (id);



