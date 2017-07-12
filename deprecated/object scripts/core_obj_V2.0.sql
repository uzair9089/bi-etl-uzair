--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.2
-- Dumped by pg_dump version 9.5.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

--COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = core, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: appointment_resources; Type: TABLE; Schema: public; Owner: segment
--

DROP TABLE IF EXISTS core.employees,core.appointment_resources,core.appointment_services,core.customers,core.merchant_accounts,core.events,core.feedbacks,core.merchant_customers,core.shift_plan_templates,core.newsletters,core.resources,core.services,core.merchant_key_accounts,core.merchant_profiles,core.event_participants,core.appointment_series,core.shifts;

CREATE TABLE core.employees
(
  id text,
  organization_id numeric NOT NULL,
  first_name text,
  last_name text NOT NULL,
  email_business text,
  phone text,
  birthday date,
  address_street text,
  address_postal_code text,
  address_city text,
  address_country text,
  ordinality numeric NOT NULL,
  color character varying(255) DEFAULT NULL::character varying
);



ALTER TABLE core.employees OWNER TO segment;

--
-- Name: appointment_resources_id_seq; Type: SEQUENCE; Schema: public; Owner: segment
--



CREATE TABLE core.appointment_resources (
    id numeric NOT NULL,
    appointment_id numeric NOT NULL,
    name character varying(255) NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    resource_id uuid,
    color character varying(255)
);


ALTER TABLE core.appointment_resources OWNER TO segment;



--
-- Name: appointment_series; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.appointment_series (
    id numeric NOT NULL,
    merchant_profile_id numeric NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    datetime timestamp without time zone,
    additional_information_archive text,
    state character varying(255) NOT NULL,
    previous_datetime timestamp without time zone,
    reminder_hours numeric DEFAULT 24.0 NOT NULL,
    color character varying(255),
    deleted_at timestamp without time zone,
    created_by_merchant boolean DEFAULT false NOT NULL,
    state_changed_by_merchant boolean NOT NULL,
    type character varying(255) NOT NULL,
    appointment_group_id numeric,
    uuid uuid NOT NULL,
    customer_json json,
    participating_account_ids text NOT NULL,
    origin character varying(255),
    caldav_properties text,
    location_uuid uuid NOT NULL,
    caldav_uid character varying(255) NOT NULL,
    verification_code character varying(255),
    attachments text,
    steps json DEFAULT '[]'::json NOT NULL,
    explicit_steps boolean DEFAULT false NOT NULL,
    complete_datetime_end timestamp without time zone,
    merchant_customer_id uuid,
    original_customer_id uuid,
    customer_attachments text,
    rules jsonb DEFAULT '[]'::jsonb NOT NULL,
    address_street character varying(255),
    address_postal_code character varying(255),
    address_city character varying(255),
    address_country_code character varying(255),
    address_of numeric,
    booking_definitions jsonb,
    booking_data jsonb,
    charge_id uuid
);


ALTER TABLE core.appointment_series OWNER TO segment;


--
-- Name: appointment_services; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.appointment_services (
    id numeric NOT NULL,
    appointment_id numeric NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    max_capacity numeric,
    price_cents numeric,
    price_currency character varying(255),
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    requirements text,
    service_id uuid,
    steps json DEFAULT '[]'::json NOT NULL,
    uuid uuid
);


ALTER TABLE core.appointment_services OWNER TO segment;



--
-- Name: customers; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.customers (
    id numeric NOT NULL,
    mobile character varying(255),
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    gender character varying(255),
    first_name character varying(255),
    last_name character varying(255),
    fake boolean,
    suspension_comment text,
    suspended boolean DEFAULT false,
    urban_airship_alias character varying(255),
    locale character varying(255),
    encrypted_password character varying(255) DEFAULT ''::character(1) NOT NULL,
    reset_password_token character varying(255),
    reset_password_sent_at timestamp without time zone,
    remember_created_at timestamp without time zone,
    sign_in_count numeric DEFAULT 0.0,
    current_sign_in_at timestamp without time zone,
    last_sign_in_at timestamp without time zone,
    authentication_token character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    uuid uuid NOT NULL
);


ALTER TABLE core.customers OWNER TO segment;


--
-- Name: event_participants; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.event_participants (
    id numeric NOT NULL,
    event_id numeric NOT NULL,
    sender boolean NOT NULL,
    model_id numeric,
    model_type character varying(255),
    read boolean DEFAULT false NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE core.event_participants OWNER TO segment;


--
-- Name: events; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.events (
    id numeric NOT NULL,
    type character varying(255) NOT NULL,
    content text,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    deliveries text NOT NULL,
    appointment_id uuid,
    messaging_message_id uuid
);


ALTER TABLE core.events OWNER TO segment;



--
-- Name: feedbacks; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.feedbacks (
    id numeric NOT NULL,
    positive boolean,
    comment text,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    uuid uuid NOT NULL,
    permitted_at timestamp without time zone NOT NULL,
    state character varying(255) NOT NULL,
    was_requested boolean DEFAULT false NOT NULL,
    appointment_id uuid NOT NULL,
    merchant_customer_id uuid NOT NULL,
    public boolean DEFAULT true NOT NULL,
    CONSTRAINT check_constraint_feedbacks_positive_not_null CHECK (((((state)::text = 'given'::text) AND (positive IS NOT NULL)) OR (((state)::text <> 'given'::text) AND (positive IS NULL))))
);


ALTER TABLE core.feedbacks OWNER TO segment;


--
-- Name: merchant_accounts; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.merchant_accounts (
    id numeric NOT NULL,
    encrypted_password character varying(255) DEFAULT ''::character varying NOT NULL,
    reset_password_token character varying(255),
    reset_password_sent_at timestamp without time zone,
    remember_created_at timestamp without time zone,
    sign_in_count numeric DEFAULT 0.0,
    current_sign_in_at timestamp without time zone,
    last_sign_in_at timestamp without time zone,
    authentication_token character varying(255),
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    email character varying(255) NOT NULL,
    confirmation_token character varying(255),
    confirmed_at timestamp without time zone,
    confirmation_sent_at timestamp without time zone,
    full_name character varying(255),
    invitation_token character varying(255),
    invitation_sent_at timestamp without time zone,
    config_json json,
    uuid uuid NOT NULL,
    organization_admin boolean DEFAULT false NOT NULL,
    merchant_key_account_id numeric NOT NULL
);


ALTER TABLE core.merchant_accounts OWNER TO segment;


--
-- Name: merchant_customers; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.merchant_customers (
    id numeric NOT NULL,
    merchant_profile_id numeric NOT NULL,
    gender character varying(255),
    first_name character varying(255),
    last_name character varying(255),
    email character varying(255),
    mobile character varying(255),
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    deleted_at timestamp without time zone,
    locale character varying(255),
    tag_ids text,
    address_json json,
    birthday character varying(255),
    uuid uuid NOT NULL,
    unread_event_messages_count numeric DEFAULT 0.0 NOT NULL,
    original_customer_id uuid
);


ALTER TABLE core.merchant_customers OWNER TO segment;


--
-- Name: merchant_key_accounts; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.merchant_key_accounts (
    id numeric NOT NULL,
    name character varying(255) NOT NULL,
    slug character varying(255) NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    max_number_of_profiles numeric DEFAULT 1.0 NOT NULL,
    max_number_of_merchant_accounts numeric DEFAULT 5.0 NOT NULL,
    campaign_id character varying(255),
    test boolean DEFAULT false NOT NULL,
    self_sign_up boolean DEFAULT false NOT NULL,
    uuid uuid NOT NULL,
    trial_ends_on date,
    language character varying(255) DEFAULT 'de'::character varying NOT NULL,
    suspended boolean DEFAULT false NOT NULL,
    feature_toggles json,
    locale character varying(255) DEFAULT 'de'::character varying NOT NULL,
    uberall_package_id numeric,
    sms_newsletter_yearly_contingent numeric DEFAULT 3600 NOT NULL,
    sms_newsletter_contingent_starts_on date DEFAULT now() NOT NULL,
    visible_in_customer_app boolean DEFAULT true NOT NULL,
    key_account_contract boolean DEFAULT false NOT NULL,
    terms_and_conditions_url character varying(255),
    privacy_policy_url character varying(255),
    legal_name character varying(255)
    CONSTRAINT positive_sms_newsletter_limit CHECK ((sms_newsletter_yearly_contingent >= 0))
);


ALTER TABLE core.merchant_key_accounts OWNER TO segment;


--
-- Name: merchant_profiles; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.merchant_profiles (
    id numeric NOT NULL,
    name character varying(255),
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    street character varying(255),
    postal_code character varying(255),
    latitude double precision,
    longitude double precision,
    phone_number character varying(255),
    contact_person character varying(255),
    website character varying(255),
    description text,
    opening_hours text,
    suspended boolean DEFAULT false,
    suspension_comment text,
    slug character varying(255),
    salesforce_id character varying(255),
    widget_hint_text text,
    open_bitstring text,
    lead_time_minutes numeric DEFAULT 1440 NOT NULL,
    direct_bookable boolean DEFAULT false NOT NULL,
    email_hint_text text,
    bitstring text,
    bookable_id numeric NOT NULL,
    interval_duration numeric DEFAULT 30 NOT NULL,
    currency character varying(255),
    config_json json,
    merchant_key_account_id numeric NOT NULL,
    state character varying(255) DEFAULT 'ready'::character varying NOT NULL,
    uuid uuid NOT NULL,
    address_country character varying(255) DEFAULT 'DE'::character varying NOT NULL,
    time_zone character varying(255) DEFAULT 'Etc/UTC'::character varying NOT NULL,
    main_category_slug character varying(255) DEFAULT 'other'::character varying NOT NULL,
    city_name character varying(255),
    city_slug character varying(255),
    max_lead_time_minutes numeric,
    enabled_payments text,
    social_media_links jsonb DEFAULT '{}'::jsonb NOT NULL
);


ALTER TABLE core.merchant_profiles OWNER TO segment;


--
-- Name: newsletters; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.newsletters (
    id numeric NOT NULL,
    merchant_profile_id numeric,
    subject text,
    body text,
    receivers json,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    sent_at timestamp without time zone,
    scheduled_at timestamp without time zone,
    attachment_uid character varying(255),
    attachment_name character varying(255),
    recipient_count numeric DEFAULT 0.0 NOT NULL,
    deliver_via character varying(255) DEFAULT 'email'::character varying NOT NULL,
    sms_count numeric,
    uuid uuid
);


ALTER TABLE core.newsletters OWNER TO segment;


--
-- Name: resources; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.resources (
    id numeric NOT NULL,
    merchant_profile_id numeric NOT NULL,
    name character varying(255) NOT NULL,
    "position" numeric NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    visible boolean DEFAULT false,
    all_services boolean DEFAULT true NOT NULL,
    color character varying(255),
    bitstring text,
    bookable_id numeric NOT NULL,
    constraints_configuration json,
    constraints json,
    constraints_type character varying(255),
    uuid uuid NOT NULL,
    employee_id uuid
);


ALTER TABLE core.resources OWNER TO segment;

--
-- Name: services; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.services (
    id numeric NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    merchant_profile_id numeric NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    "position" numeric,
    requirements text,
    type character varying(255),
    color character varying(255),
    max_capacity numeric,
    bookable_id numeric NOT NULL,
    service_category_id numeric,
    price_cents numeric,
    deleted_at timestamp without time zone,
    uuid uuid NOT NULL,
    steps json DEFAULT '[]'::json NOT NULL,
    bookable_by_customer boolean DEFAULT true,
    tax_category_id uuid
);


ALTER TABLE core.services OWNER TO segment;


--
-- Name: shift_plan_templates; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.shift_plan_templates (
    merchant_profile_id numeric,
    name character varying(255) NOT NULL,
    shift_params json NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    id uuid NOT NULL
);


ALTER TABLE core.shift_plan_templates OWNER TO segment;

--
-- Name: shifts; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE core.shifts (
    id uuid NOT NULL,
    resource_id numeric NOT NULL,
    starts_at timestamp(0) without time zone NOT NULL,
    ends_at timestamp(0) without time zone NOT NULL,
    kind text NOT NULL,
    created_at timestamp without time zone  ,
    updated_at timestamp without time zone  ,
    CONSTRAINT shifts_starts_at_check CHECK ((date_part('year'::text, starts_at) >= (1950)::double precision))
);


ALTER TABLE core.shifts OWNER TO segment;

--
-- Name: public; Type: ACL; Schema: -; Owner: segment
--

REVOKE ALL ON SCHEMA core FROM segment;
REVOKE ALL ON SCHEMA core FROM segment;
GRANT ALL ON SCHEMA core TO segment;
GRANT ALL ON SCHEMA core TO segment;


--
-- PostgreSQL database dump complete
--

ALTER TABLE ONLY core.merchant_accounts
    ADD CONSTRAINT accounts_pkey PRIMARY KEY (id,updated_at);


--
-- Name: appointment_resources_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.appointment_resources
    ADD CONSTRAINT appointment_resources_pkey PRIMARY KEY (id,updated_at);


--
-- Name: appointment_services_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.appointment_services
    ADD CONSTRAINT appointment_services_pkey PRIMARY KEY (id,updated_at);


--
-- Name: appointments_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.appointment_series
    ADD CONSTRAINT appointments_pkey PRIMARY KEY (id,updated_at);


--
-- Name: customers_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id,updated_at);


--
-- Name: event_participants_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.event_participants
    ADD CONSTRAINT event_participants_pkey PRIMARY KEY (id,updated_at);


--
-- Name: events_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id,updated_at);


--
-- Name: feedbacks_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.feedbacks
    ADD CONSTRAINT feedbacks_pkey PRIMARY KEY (id,updated_at);


--
-- Name: merchant_customers_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.merchant_customers
    ADD CONSTRAINT merchant_customers_pkey PRIMARY KEY (id,updated_at);


--
-- Name: merchant_key_accounts_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.merchant_key_accounts
    ADD CONSTRAINT merchant_key_accounts_pkey PRIMARY KEY (id,updated_at);


--
-- Name: merchant_profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.merchant_profiles
    ADD CONSTRAINT merchant_profiles_pkey PRIMARY KEY (id,updated_at);


--
-- Name: newsletters_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.newsletters
    ADD CONSTRAINT newsletters_pkey PRIMARY KEY (id,updated_at);


--
-- Name: resources_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.resources
    ADD CONSTRAINT resources_pkey PRIMARY KEY (id,updated_at);


--
-- Name: services_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.services
    ADD CONSTRAINT services_pkey PRIMARY KEY (id,updated_at);


--
-- Name: shift_plan_templates_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.shift_plan_templates
    ADD CONSTRAINT shift_plan_templates_pkey PRIMARY KEY (id,updated_at);


--
-- Name: shifts_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY core.shifts
    ADD CONSTRAINT shifts_pkey PRIMARY KEY (id, updated_at);



