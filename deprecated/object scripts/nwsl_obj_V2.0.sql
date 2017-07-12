

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.8
-- Dumped by pg_dump version 9.5.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;



CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA nwsl;


CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA nwsl;


SET search_path = nwsl, pg_catalog;

--
-- Name: newsletter_kind; Type: TYPE; Schema: public; Owner: segment
--


DROP TABLE IF EXISTS nwsl.newsletter_customers,nwsl.newsletters_nwsl;


ALTER TYPE nwsl.newsletter_state OWNER TO segment;

SET default_tablespace = '';

SET default_with_oids = false;



CREATE TABLE nwsl.newsletter_customers (
    newsletter_id uuid NOT NULL,
    customer_uuid uuid NOT NULL,
    state character varying DEFAULT 'new'::character varying NOT NULL
);


ALTER TABLE nwsl.newsletter_customers OWNER TO segment;

--
-- Name: newsletters; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE nwsl.newsletters_nwsl (
    id uuid  NOT NULL,
    merchant_uuid text NOT NULL,
    state VARCHAR(200) NOT NULL,
    send_at timestamp without time zone,
    sent_at timestamp without time zone,
    finished_at timestamp without time zone,
    variables jsonb DEFAULT '{}'::jsonb,
    subject text,
    title text,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    customer_uuids uuid[] DEFAULT '{}'::uuid[] NOT NULL,
    template_uuid uuid NOT NULL,
    locale text DEFAULT 'en'::text NOT NULL,
    customer_groups text,
    kind VARCHAR(200) NOT NULL
);


ALTER TABLE nwsl.newsletters_nwsl OWNER TO segment;


--
-- Name: newsletters_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY nwsl.newsletters_nwsl
    ADD CONSTRAINT newsletters_nwsl_pkey PRIMARY KEY (id,updated_at);


--
-- Name: public; Type: ACL; Schema: -; Owner: segment
--

REVOKE ALL ON SCHEMA nwsl FROM PUBLIC;
REVOKE ALL ON SCHEMA nwsl FROM segment;
GRANT ALL ON SCHEMA nwsl TO segment;
GRANT ALL ON SCHEMA nwsl TO PUBLIC;


--
-- PostgreSQL database dump complete
--

