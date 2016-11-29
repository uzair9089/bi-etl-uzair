--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.3
-- Dumped by pg_dump version 9.5.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = nwsl, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: conversation_senders; Type: TABLE; Schema: public; Owner: segment
--


DROP TABLE IF EXISTS msg.conversation_senders,msg.conversations,msg.group_senders,msg.merchant_senders,msg.messages,msg.participants;

CREATE TABLE msg.conversation_senders (
    id integer NOT NULL,
    conversation_id uuid NOT NULL,
    sender_id uuid NOT NULL,
    read_at timestamp without time zone NOT NULL,
    sender_type text
);


ALTER TABLE msg.conversation_senders OWNER TO segment;


--
-- Name: conversations; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE msg.conversations (
    id uuid,
    merchant_id uuid NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    last_message_id uuid
);


ALTER TABLE msg.conversations OWNER TO segment;

--
-- Name: group_senders; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE msg.group_senders (
    id integer NOT NULL,
    merchant_id uuid NOT NULL,
    group_id uuid NOT NULL,
    sender_id uuid NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    group_type text,
    sender_type text
);


ALTER TABLE msg.group_senders OWNER TO segment;


--
-- Name: merchant_senders; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE msg.merchant_senders (
    id integer NOT NULL,
    merchant_id uuid NOT NULL,
    sender_id uuid NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    sender_type text
);


ALTER TABLE msg.merchant_senders OWNER TO segment;




--
-- Name: messages; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE msg.messages (
    id uuid,
    conversation_id uuid NOT NULL,
    content text NOT NULL,
    sender_id uuid NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    sender_type text
);


ALTER TABLE msg.messages OWNER TO segment;

--
-- Name: participants; Type: TABLE; Schema: public; Owner: segment
--

CREATE TABLE msg.participants (
    id uuid,
    conversation_id uuid NOT NULL,
    group_id uuid NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    group_type text
);


ALTER TABLE msg.participants OWNER TO segment;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: segment
--

--
-- Name: conversation_senders_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY msg.conversation_senders
    ADD CONSTRAINT conversation_senders_pkey PRIMARY KEY (id);


--
-- Name: conversations_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY msg.conversations
    ADD CONSTRAINT conversations_pkey PRIMARY KEY (id,updated_at);


--
-- Name: group_senders_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY msg.group_senders
    ADD CONSTRAINT group_senders_pkey PRIMARY KEY (id,updated_at);


--
-- Name: merchant_senders_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY msg.merchant_senders
    ADD CONSTRAINT merchant_senders_pkey PRIMARY KEY (id,updated_at);


--
-- Name: messages_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY msg.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id,updated_at);


--
-- Name: participants_pkey; Type: CONSTRAINT; Schema: public; Owner: segment
--

ALTER TABLE ONLY msg.participants
    ADD CONSTRAINT participants_pkey PRIMARY KEY (id,updated_at);



