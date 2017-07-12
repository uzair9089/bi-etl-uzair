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

SET search_path = stage, pg_catalog;

SET default_with_oids = false;

--
-- Name: s_account; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_account (
    billingcity character varying(8000),
    billingcountry character varying(8000),
    billingpostalcode character varying(8000),
    billingstate character varying(8000),
    billingstreet character varying(8000),
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(8000),
    id character(400) NOT NULL,
    industry character varying(8000),
    isdeleted boolean,
    lastactivitydate date,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    merchant_happiness__c character varying(8000),
    name character varying(8000),
    numberofemployees numeric,
    ownerid character(400),
    parentid character(400),
    phone character varying(8000),
    rating character varying(8000),
    recordtypeid character(400),
    type character varying(8000),
    website character varying(8000),
    baccountrisk__c boolean,
    bactive__c boolean,
    bispartner__c boolean,
    dcrmscore__c numeric,
    dcustomerscore__c numeric,
    dinventoryscore__c numeric,
    dkeyaccountid__c numeric,
    dshopid__c numeric,
    dtotalactivityscore__c numeric,
    dtractionscore__c numeric,
    datedatecustomerimport__c date,
    datedebtcollectioninitiated__c date,
    dateinternaluse__c date,
    datescall__c date,
    datetrialend__c date,
    datetrialstart__c date,
    datewidgetin__c date,
    dtactivationdate__c date,
    dtcrnumberofcustomersimported__c numeric,
    dtonboardingdate__c date,
    fmlSubscriptionStatus__c VARCHAR(4000),
    plcreditworthiness__c character varying(8000),
    plcustomerdatainfo__c character varying(8000),
    plsubcategory__c character varying(8000),
    refactivesubscription__c character(400),
    strcreditscore__c character varying(8000),
    strmerchantuuid__c character varying(8000),
    object_type character varying(8000),
    urllinktosuccessstory__c character varying(8000)

);


--
-- Name: s_appointment_resources; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_appointment_resources (
    id numeric NOT NULL,
    appointment_id numeric,
    name character varying(255),
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    resource_id uuid,
    color character varying(255)
);


--
-- Name: s_appointment_series; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_appointment_series (
    id numeric NOT NULL,
    merchant_profile_id numeric,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    datetime timestamp without time zone,
    additional_information_archive text,
    state character varying(255),
    previous_datetime timestamp without time zone,
    reminder_hours numeric,
    color character varying(255),
    deleted_at timestamp without time zone,
    created_by_merchant boolean,
    state_changed_by_merchant boolean,
    type character varying(255),
    appointment_group_id numeric,
    uuid uuid,
    customer_json json,
    participating_account_ids text,
    origin character varying(255),
    caldav_properties text,
    location_uuid uuid,
    caldav_uid character varying(255),
    verification_code character varying(255),
    attachments text,
    steps json,
    explicit_steps boolean,
    complete_datetime_end timestamp without time zone,
    merchant_customer_id uuid,
    original_customer_id uuid,
    customer_attachments text,
    rules jsonb,
    address_street character varying(255),
    address_postal_code character varying(255),
    address_city character varying(255),
    address_country_code character varying(255),
    address_of numeric,
    booking_definitions jsonb,
    booking_data jsonb,
    charge_id uuid
);


--
-- Name: s_appointment_services; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_appointment_services (
    id numeric NOT NULL,
    appointment_id numeric,
    name character varying(255),
    description text,
    max_capacity numeric,
    price_cents numeric,
    price_currency character varying(255),
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    requirements text,
    service_id uuid,
    steps json,
    uuid uuid
);


--
-- Name: s_contact; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_contact (
    accountid character(400),
    birthdate date,
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(200),
    department character varying(200),
    email character varying(200),
    firstname character varying(200),
    homephone character varying(200),
    id character varying(400) NOT NULL,
    isdeleted boolean,
    lastactivitydate date,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    lastname character varying(200),
    leadsource character varying(200),
    mailingcity character varying(200),
    mailingcountry character varying(200),
    mailingpostalcode character varying(200),
    mailingstate character varying(200),
    mailingstreet character varying(2000),
    mobilephone character varying(200),
    name character varying(200),
    ownerid character(400),
    phone character varying(200),
    recordtypeid character(400),
    reportstoid character(400),
    salutation character varying(200),
    systemmodstamp timestamp without time zone,
    title character varying(200),
    object_type character varying(200)
);


--
-- Name: s_contract; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_contract (
    accountid character(400),
    activatedbyid character(400),
    activateddate timestamp without time zone,
    billingcity character varying(8000),
    billingcountry character varying(8000),
    billingpostalcode character varying(8000),
    billingstate character varying(8000),
    billingstreet text,
    companysigneddate date,
    companysignedid character(400),
    contractnumber character varying(8000),
    contractterm numeric,
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(1000),
    customersigneddate date,
    customersignedid character(400),
    customersignedtitle character varying(8000),
    enddate date,
    id character(400) NOT NULL,
    isdeleted boolean,
    lastactivitydate date,
    lastapproveddate timestamp without time zone,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    name character varying(8000),
    ownerid character(400),
    pricebook2id character(400),
    recordtypeid character(400),
    shippingcity character varying(8000),
    shippingcountry character varying(8000),
    shippingpostalcode character varying(8000),
    shippingstate character varying(8000),
    shippingstreet text,
    specialterms text,
    startdate date,
    status character varying(1000),
    statuscode character varying(1000),
    systemmodstamp timestamp without time zone,
    bbonusonhold__c boolean,
    bedgecase__c boolean,
    daveragesalesmrr__c numeric,
    dguaranteedbookings__c numeric,
    dyearlydiscount__c numeric,
    datecancellationperiod__c date,
    pledgecasecategory__c character varying(1000),
    plmoneyback__c character varying(1000),
    plpaymentcycle__c character varying(1000),
    plspecialrightofcancellation__c character varying(1000),
    pltrial__c character varying(1000),
    refaccountmanagercash__c character(400),
    refaccountmanager__c character(400),
    refbusinessowner__c character(400),
    refcontactperson__c character(400),
    refopportunity__c character(400),
    refsubscription__c character(400),
    strfinancialreporting_saleschannel__c character varying(8000),
    strpaymentmethod__c character varying(1000),
    object_type character varying(200)
);


--
-- Name: s_conversation_senders; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_conversation_senders (
    id integer,
    conversation_id uuid,
    sender_id uuid,
    read_at timestamp without time zone,
    sender_type text
);


--
-- Name: s_conversations; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_conversations (
    id uuid NOT NULL,
    merchant_id uuid,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    last_message_id uuid
);


--
-- Name: s_customers; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_customers (
    id numeric NOT NULL,
    mobile character varying(255),
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    gender character varying(255),
    first_name character varying(255),
    last_name character varying(255),
    fake boolean,
    suspension_comment text,
    suspended boolean,
    urban_airship_alias character varying(255),
    locale character varying(255),
    encrypted_password character varying(255),
    reset_password_token character varying(255),
    reset_password_sent_at timestamp without time zone,
    remember_created_at timestamp without time zone,
    sign_in_count numeric,
    current_sign_in_at timestamp without time zone,
    last_sign_in_at timestamp without time zone,
    authentication_token character varying(255),
    email character varying(255),
    uuid uuid
);


--
-- Name: s_employees; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_employees (
    id text,
    organization_id numeric,
    first_name text,
    last_name text,
    email_business text,
    phone text,
    birthday date,
    address_street text,
    address_postal_code text,
    address_city text,
    address_country text,
    ordinality numeric,
    color character varying(255)
);


--
-- Name: s_event_participants; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_event_participants (
    id numeric NOT NULL,
    event_id numeric,
    sender boolean,
    model_id numeric,
    model_type character varying(255),
    read boolean,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


--
-- Name: s_events; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_events (
    id numeric NOT NULL,
    type character varying(255),
    content text,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    deliveries text,
    appointment_id uuid,
    messaging_message_id uuid
);


--
-- Name: s_feedbacks; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_feedbacks (
    id numeric NOT NULL,
    positive boolean,
    comment text,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    uuid uuid,
    permitted_at timestamp without time zone,
    state character varying(255),
    was_requested boolean,
    appointment_id uuid,
    merchant_customer_id uuid,
    public boolean
);


--
-- Name: s_group_senders; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_group_senders (
    id integer NOT NULL,
    merchant_id uuid,
    group_id uuid,
    sender_id uuid,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    group_type text,
    sender_type text
);


--
-- Name: s_lead; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_lead (
    annualrevenue numeric,
    bsendinfomaterial__c boolean,
    city character varying(8000),
    company character varying(8000),
    convertedaccountid character(400),
    convertedcontactid character(400),
    converteddate date,
    convertedopportunityid character(400),
    country character varying(8000),
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(1000),
    email character(400),
    firstname character varying(8000),
    id character varying(400) NOT NULL,
    industry character varying(1000),
    isconverted boolean,
    isdeleted boolean,
    isunreadbyowner boolean,
    lastactivitydate date,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    lastname character varying(8000),
    lasttransferdate date,
    leadsource character varying(1000),
    mobilephone character varying(200),
    name character varying(8000),
    numberofemployees numeric,
    ownerid character(400),
    phone character varying(200),
    postalcode character varying(8000),
    rating character varying(1000),
    recordtypeid character(400),
    salutation character varying(1000),
    state character varying(8000),
    status character varying(1000),
    street text,
    systemmodstamp timestamp without time zone,
    title character varying(8000),
    website character varying(2000),
    bbelongstochain__c boolean,
    bdemosetbyowner__c boolean,
    bgotreferred__c boolean,
    bonlinebookingavailable__c boolean,
    brejectlead__c boolean,
    bsendemailconfirmation__c boolean,
    bstarlead__c boolean,
    dnumberofoutlets__c numeric,
    pltemplatelanguage__c character varying(1000),
    pltype__c character varying(1000),
    refassignedto__c character(400),
    strcompetitorsystem__c character varying(8000),
    object_type character varying(200),
    urlfacebookprofile__c character varying(2000)
);


--
-- Name: s_merchant_accounts; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_merchant_accounts (
    id numeric NOT NULL,
    encrypted_password character varying(255),
    reset_password_token character varying(255),
    reset_password_sent_at timestamp without time zone,
    remember_created_at timestamp without time zone,
    sign_in_count numeric,
    current_sign_in_at timestamp without time zone,
    last_sign_in_at timestamp without time zone,
    authentication_token character varying(255),
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    email character varying(255),
    confirmation_token character varying(255),
    confirmed_at timestamp without time zone,
    confirmation_sent_at timestamp without time zone,
    full_name character varying(255),
    invitation_token character varying(255),
    invitation_sent_at timestamp without time zone,
    config_json json,
    uuid uuid,
    organization_admin boolean,
    merchant_key_account_id numeric
);


--
-- Name: s_merchant_customers; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_merchant_customers (
    id numeric NOT NULL,
    merchant_profile_id numeric,
    gender character varying(255),
    first_name character varying(255),
    last_name character varying(255),
    email character varying(255),
    mobile character varying(255),
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    locale character varying(255),
    tag_ids text,
    address_json json,
    birthday character varying(255),
    uuid uuid,
    unread_event_messages_count numeric,
    original_customer_id uuid
);


--
-- Name: s_merchant_key_accounts; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_merchant_key_accounts (
    id numeric NOT NULL,
    name character varying(255),
    slug character varying(255),
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    max_number_of_profiles numeric,
    max_number_of_merchant_accounts numeric,
    campaign_id character varying(255),
    test boolean,
    self_sign_up boolean,
    uuid uuid,
    trial_ends_on date,
    language character varying(255),
    suspended boolean,
    feature_toggles json,
    locale character varying(255),
    uberall_package_id numeric,
    sms_newsletter_yearly_contingent numeric,
    sms_newsletter_contingent_starts_on date,
    visible_in_customer_app boolean,
    key_account_contract boolean,
    terms_and_conditions_url character varying(255),
    privacy_policy_url character varying(255),
    legal_name character varying(255)
);


--
-- Name: s_merchant_profiles; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_merchant_profiles (
    id numeric NOT NULL,
    name character varying(255),
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    street character varying(255),
    postal_code character varying(255),
    latitude double precision,
    longitude double precision,
    phone_number character varying(255),
    contact_person character varying(255),
    website character varying(255),
    description text,
    opening_hours text,
    suspended boolean,
    suspension_comment text,
    slug character varying(255),
    salesforce_id character varying(255),
    widget_hint_text text,
    open_bitstring text,
    lead_time_minutes numeric,
    direct_bookable boolean,
    email_hint_text text,
    bitstring text,
    bookable_id numeric,
    interval_duration numeric,
    currency character varying(255),
    config_json json,
    merchant_key_account_id numeric,
    state character varying(255),
    uuid uuid,
    address_country character varying(255),
    time_zone character varying(255),
    main_category_slug character varying(255),
    city_name character varying(255),
    city_slug character varying(255),
    max_lead_time_minutes numeric,
    enabled_payments text,
    social_media_links jsonb
);


--
-- Name: s_merchant_senders; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_merchant_senders (
    id integer NOT NULL,
    merchant_id uuid,
    sender_id uuid,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    sender_type text
);


--
-- Name: s_messages; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_messages (
    id uuid NOT NULL,
    conversation_id uuid,
    content text,
    sender_id uuid,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    sender_type text
);


--
-- Name: s_newsletter_customers; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_newsletter_customers (
    newsletter_id uuid,
    customer_uuid uuid,
    state character varying
);


--
-- Name: s_newsletters_nwsl; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_newsletters_nwsl (
    id uuid NOT NULL,
    merchant_uuid text,
    state character varying(200),
    send_at timestamp without time zone,
    sent_at timestamp without time zone,
    finished_at timestamp without time zone,
    variables jsonb,
    subject text,
    title text,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    customer_uuids uuid[],
    template_uuid uuid,
    locale text,
    customer_groups text,
    kind character varying(200)
);


--
-- Name: s_newsletters; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_newsletters (
    id numeric NOT NULL,
    merchant_profile_id numeric,
    subject text,
    body text,
    receivers json,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    sent_at timestamp without time zone,
    scheduled_at timestamp without time zone,
    attachment_uid character varying(255),
    attachment_name character varying(255),
    recipient_count numeric,
    deliver_via character varying(255),
    sms_count numeric,
    uuid uuid
);


--
-- Name: s_onb2__balance__c; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_onb2__balance__c (
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(1000),
    id character(400) NOT NULL,
    isdeleted boolean,
    lastactivitydate date,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    name character varying(8000),
    onb2__account__c character(400),
    onb2__amount__c numeric,
    onb2__date__c date,
    onb2__dunning__c character(400),
    onb2__invoice__c character(400),
    onb2__noautoassignment__c boolean,
    onb2__paymentmethod__c character varying(1000),
    onb2__paymentprovider__c character varying(1000),
    onb2__reference__c character varying(8000),
    onb2__relatedinvoice__c character(400),
    onb2__subscription__c character(400),
    onb2__transactionno__c character varying(8000),
    onb2__type__c character varying(1000),
    systemmodstamp timestamp without time zone,
    object_type character varying(200)
);


--
-- Name: s_onb2__dunning__c; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_onb2__dunning__c (
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(400),
    esrexportdate__c date,
    id character varying(400) NOT NULL,
    isdeleted boolean,
    lastactivitydate date,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    name character varying(1000),
    onb2__accountname__c character varying(1000),
    onb2__account__c character(400),
    onb2__billingaddress__c character varying(2000),
    onb2__billingcity__c character varying(1000),
    onb2__billingcountry__c character varying(1000),
    onb2__billingpostalcode__c character varying(1000),
    onb2__billingstate__c character varying(1000),
    onb2__billingstreet__c character varying(1000),
    onb2__contact__c character(400),
    onb2__date__c date,
    onb2__displaytype__c character varying(1000),
    onb2__dunningrun__c character(400),
    onb2__emailbcc__c character varying(2000),
    onb2__emailcc__c character varying(2000),
    onb2__emailcontact__c character(400),
    onb2__emaildunning__c boolean,
    onb2__emailerror__c character varying(1000),
    onb2__emailfirstname__c character varying(1000),
    onb2__emaillastname__c character varying(1000),
    onb2__emailsalutation__c character varying(1000),
    onb2__emailstatus__c character varying(400),
    onb2__email__c character varying(200),
    onb2__flatfee__c numeric,
    onb2__footer__c character varying(2000),
    onb2__grandtotal__c numeric,
    onb2__header__c character varying(2000),
    onb2__infoleft__c character varying(2000),
    onb2__inforight__c character varying(2000),
    onb2__latefee__c numeric,
    onb2__level__c numeric,
    onb2__mailingcity__c character varying(1000),
    onb2__mailingcontact__c character(400),
    onb2__mailingcountry__c character varying(1000),
    onb2__mailingfirstname__c character varying(1000),
    onb2__mailinglastname__c character varying(1000),
    onb2__mailingpostalcode__c character varying(1000),
    onb2__mailingsalutation__c character varying(1000),
    onb2__mailingstate__c character varying(1000),
    onb2__mailingstreet__c character varying(1000),
    onb2__maxsequence__c numeric,
    onb2__pdf__c character varying(1000),
    onb2__pageheader__c character varying(2000),
    onb2__paymentduedate__c date,
    onb2__paymentdue__c numeric,
    onb2__printdunning__c boolean,
    onb2__recipientaddress__c character varying(2000),
    onb2__senderaddress__c character varying(1000),
    onb2__status__c character varying(400),
    onb2__template__c character(400),
    onb2__tenant__c character varying(1000),
    onb2__text1__c character varying(2000),
    onb2__text2__c character varying(2000),
    onb2__text3__c character varying(2000),
    onb2__type__c character varying(1000),
    onb2__uuid__c character varying(1000),
    ownerid character(400),
    systemmodstamp timestamp without time zone,
    stresrparticipantnumber__c character varying(1000),
    stresrreferencenumber__c character varying(1000),
    object_type character varying(200)
);


--
-- Name: s_onb2__dunningdetail__c; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_onb2__dunningdetail__c (
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(1000),
    id character(400) NOT NULL,
    isdeleted boolean,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    name character varying(8000),
    onb2__amount__c numeric,
    onb2__balancedifference__c numeric,
    onb2__daysoverdue__c numeric,
    onb2__description__c text,
    onb2__dunningamount__c numeric,
    onb2__dunning__c character(400),
    onb2__grandtotal__c numeric,
    onb2__invoice__c character(400),
    onb2__latefee__c numeric,
    onb2__paymentduedate__c date,
    onb2__paymentdue__c numeric,
    onb2__previousfees__c numeric,
    onb2__rate__c numeric,
    onb2__sequence__c numeric,
    onb2__title__c character varying(8000),
    onb2__type__c character varying(1000),
    systemmodstamp timestamp without time zone,
    object_type character varying(200)
);


--
-- Name: s_onb2__invoice__c; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_onb2__invoice__c (
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(1000),
    esrexportdate__c date,
    id character(400) NOT NULL,
    isdeleted boolean,
    lastactivitydate date,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    name character varying(8000),
    onb2__accountname__c character varying(8000),
    onb2__account__c character(400),
    onb2__balancedifference__c numeric,
    onb2__balance__c numeric,
    onb2__bankaccountowner__c character varying(8000),
    onb2__bankaccount__c character varying(8000),
    onb2__bankcode__c character varying(8000),
    onb2__billingaddress__c text,
    onb2__billingcity__c character varying(8000),
    onb2__billingcountry__c character varying(8000),
    onb2__billingpostalcode__c character varying(8000),
    onb2__billingstate__c character varying(8000),
    onb2__billingstreet__c character varying(8000),
    onb2__cancelationreason__c character varying(1000),
    onb2__canceledwith__c character(400),
    onb2__class__c character varying(8000),
    onb2__contact__c character(400),
    onb2__conversionrate__c numeric,
    onb2__date__c date,
    onb2__daysoverdue__c numeric,
    onb2__directdebitmandategranted__c date,
    onb2__directdebitmandatereference__c character varying(8000),
    onb2__directdebitsequencetype__c character varying(1000),
    onb2__discountamount__c numeric,
    onb2__discountmessage__c text,
    onb2__discountpaymentduedate__c date,
    onb2__discountpaymentdue__c numeric,
    onb2__discountrate__c numeric,
    onb2__discountednextpaymentdue__c numeric,
    onb2__discountedtotalgross__c numeric,
    onb2__displaytransactiontables__c boolean,
    onb2__displaytype__c character varying(8000),
    onb2__dunninglevel__c numeric,
    onb2__emailbcc__c text,
    onb2__emailcontact__c character(400),
    onb2__emailerror__c text,
    onb2__emailfirstname__c character varying(8000),
    onb2__emailinvoicecc__c text,
    onb2__emailinvoice__c boolean,
    onb2__emaillastname__c character varying(8000),
    onb2__emailsalutation__c character varying(8000),
    onb2__emailstatus__c character varying(1000),
    onb2__email__c character varying(400),
    onb2__exported__c character varying(8000),
    onb2__footer__c text,
    onb2__grandtotal__c numeric,
    onb2__grossinvoice__c boolean,
    onb2__header__c text,
    onb2__infoleft__c text,
    onb2__inforight__c text,
    onb2__installment__c numeric,
    onb2__invoicerun__c character(400),
    onb2__lastdunningdate__c date,
    onb2__mailingcity__c character varying(8000),
    onb2__mailingcountry__c character varying(8000),
    onb2__mailingfirstname__c character varying(8000),
    onb2__mailinglastname__c character varying(8000),
    onb2__mailingpostalcode__c character varying(8000),
    onb2__mailingsalutation__c character varying(8000),
    onb2__mailingstate__c character varying(8000),
    onb2__mailingstreet__c character varying(8000),
    onb2__nextpaymentduedate__c date,
    onb2__nextpaymentdue__c numeric,
    onb2__outstandinginvoicestext__c text,
    onb2__pdf__c character varying(2000),
    onb2__pageheader__c text,
    onb2__paymentcycleperiod__c character varying(1000),
    onb2__paymentcycles__c numeric,
    onb2__paymentdate__c date,
    onb2__paymentduedate__c date,
    onb2__paymentdue__c numeric,
    onb2__paymentinfo__c text,
    onb2__paymentmethod__c character varying(1000),
    onb2__printcontact__c character(400),
    onb2__printinvoice__c boolean,
    onb2__recipientaddress__c text,
    onb2__relatedinvoice__c character(400),
    onb2__review__c character varying(1000),
    onb2__senderaddress__c character varying(8000),
    onb2__sepapaymenterror__c character varying(8000),
    onb2__serviceperiodend__c date,
    onb2__serviceperiodstart__c date,
    onb2__shippingcity__c character varying(8000),
    onb2__shippingcountry__c character varying(8000),
    onb2__shippingpostalcode__c character varying(8000),
    onb2__shippingstate__c character varying(8000),
    onb2__shippingstreet__c character varying(8000),
    onb2__status__c character varying(1000),
    onb2__subscription__c character(400),
    onb2__template__c character(400),
    onb2__tenant__c character varying(8000),
    onb2__text1__c text,
    onb2__text2__c text,
    onb2__text3__c text,
    onb2__totalnet__c numeric,
    onb2__totaltax__c numeric,
    onb2__type__c character varying(1000),
    onb2__uuid__c character varying(8000),
    ownerid character(400),
    systemmodstamp timestamp without time zone,
    besrexportdone__c boolean,
    object_type character varying(200)
);


--
-- Name: s_onb2__item__c; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_onb2__item__c (
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(1000),
    id character(400) NOT NULL,
    isdeleted boolean,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    name character varying(8000),
    onb2__active__c boolean,
    onb2__additionaldescription__c text,
    onb2__additionaltitle__c text,
    onb2__aggregateindividualpriced__c boolean,
    onb2__billingperiod__c numeric,
    onb2__billingtype__c character varying(1000),
    onb2__billingunit__c character varying(1000),
    onb2__chargemodel__c character varying(1000),
    onb2__commission__c numeric,
    onb2__contractvaluecorrection__c numeric,
    onb2__contractvalueinvoiced__c numeric,
    onb2__contractvalueremaining__c numeric,
    onb2__contractvalue__c numeric,
    onb2__decimalplacesforquantity__c numeric,
    onb2__decimalplacesforunitprice__c numeric,
    onb2__description__c text,
    onb2__discount__c numeric,
    onb2__displaysubtotalafter__c boolean,
    onb2__enddate__c date,
    onb2__globalmonthlyminimum__c boolean,
    onb2__ignorecriterion__c boolean,
    onb2__invoicelineitemtype__c character varying(1000),
    onb2__nextinvoice__c date,
    onb2__pricetype__c character varying(1000),
    onb2__price__c numeric,
    onb2__productgroup__c character varying(8000),
    onb2__quantity__c numeric,
    onb2__sequence__c numeric,
    onb2__startdate__c date,
    onb2__subscription__c character(400),
    onb2__syncwith__c character varying(1000),
    onb2__title__c text,
    onb2__transactionpricefield__c character varying(8000),
    onb2__transactionpricetierquantityfield__c character varying(8000),
    onb2__transactionquantityfield__c character varying(8000),
    onb2__transactiontype__c character varying(1000),
    onb2__unit__c character varying(1000),
    ownerid character(400),
    salesmrr__c numeric,
    systemmodstamp timestamp without time zone,
    bisbundle__c boolean,
    bishardware__c boolean,
    bismodule__c boolean,
    bisrecurring__c boolean,
    bistrialitem__c boolean,
    brenewitem__c boolean,
    fmlactivemrr__c numeric,
    fmlchannel__c character varying(8000),
    fmldiscountedmrr__c numeric,
    fmlitempricediscounted__c numeric,
    fmlnextinvoicevalue__c numeric,
    fmlnextrevenue__c numeric,
    fmlterm__c numeric,
    plchannelcountrycode__c character varying(1000),
    plchannelsalestype__c character varying(1000),
    plchanneluserrole__c character varying(1000),
    plfinancialreporting_productclass__c character varying(1000),
    refcontract__c character(400),
    refopportunity__c character(400),
    refparentitem__c character(400),
    refproduct2__c character(400),
    ruitemprice__c numeric,
    strfinancialreporting_saleschannel__c character varying(8000),
    stropportunityproductid__c character varying(8000),
    strparentopportunityproductid__c character varying(8000),
    object_type character varying(200)
);


--
-- Name: s_onb2__subscription__c; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_onb2__subscription__c (
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(1000),
    id character(400) NOT NULL,
    isdeleted boolean,
    lastactivitydate date,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    name character varying(8000),
    onb2__account__c character(400),
    onb2__aggregationperiod__c character varying(1000),
    onb2__autorenewal__c character varying(1000),
    onb2__bankaccountowner__c character varying(8000),
    onb2__bankaccount__c character varying(8000),
    onb2__bankcode__c character varying(8000),
    onb2__billingperiod__c numeric,
    onb2__cancelationdate__c date,
    onb2__cancelationterm__c character varying(1000),
    onb2__contact__c character(400),
    onb2__directdebitmandategranted__c date,
    onb2__directdebitmandatereference__c character varying(8000),
    onb2__directdebitsequencetype__c character varying(1000),
    onb2__discountpaymentdue__c numeric,
    onb2__discountrate__c numeric,
    onb2__displaytransactiontables__c boolean,
    onb2__emailbcc__c text,
    onb2__emailinvoiceactive__c boolean,
    onb2__emailinvoicecc__c text,
    onb2__emailinvoice__c character(400),
    onb2__enddate__c date,
    onb2__invoicepaymentmethod__c character varying(1000),
    onb2__lasterror__c text,
    onb2__lastinvoicerun__c character(400),
    onb2__legalaccountname__c character varying(8000),
    onb2__legalcity__c character varying(8000),
    onb2__legalcountry__c character varying(8000),
    onb2__legalpostalcode__c character varying(8000),
    onb2__legalstate__c character varying(8000),
    onb2__legalstreet__c character varying(8000),
    onb2__nextinvoice__c date,
    onb2__paymentcycleperiod__c character varying(1000),
    onb2__paymentcycles__c numeric,
    onb2__paymentdue__c numeric,
    onb2__preferredinvoicedate__c date,
    onb2__priceincreasedate__c character varying(1000),
    onb2__priceincrease__c numeric,
    onb2__printinvoicecontact__c character(400),
    onb2__printinvoice__c boolean,
    onb2__renewaldate__c date,
    onb2__reviewinvoice__c character varying(1000),
    onb2__startdate__c date,
    onb2__status__c character varying(1000),
    onb2__template__c character(400),
    onb2__tenant__c character varying(8000),
    on_type__c character varying(1000),
    ownerid character(400),
    systemmodstamp timestamp without time zone,
    bopenpaymentcase__c boolean,
    fmlchannel__c character varying(8000),
    plchannelcountrycode__c character varying(1000),
    plchannelsalestype__c character varying(1000),
    plchanneluserrole__c character varying(1000),
    refcontract__c character(400),
    object_type character varying(200)
);


--
-- Name: s_opportunity; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_opportunity (
    accountid character(400),
    amount numeric,
    closedate date,
    createdbyid character varying(400),
    createddate timestamp without time zone,
    currencyisocode character varying(400),
    hasopportunitylineitem boolean,
    id character(400) NOT NULL,
    isclosed boolean,
    isdeleted boolean,
    iswon boolean,
    lastactivitydate date,
    lastmodifiedbyid character varying(400),
    lastmodifieddate timestamp without time zone,
    leadsource character varying(400),
    name character varying(8000),
    nextstep character varying(8000),
    ownerid character varying(400),
    pricebook2id character varying(400),
    probability numeric,
    recordtypeid character varying(400),
    stagename character varying(400),
    systemmodstamp timestamp without time zone,
    totalopportunityquantity numeric,
    type character varying(400),
    bdemosetbyowner__c boolean,
    bonlinebookingavailable__c boolean,
    btrialclosed__c boolean,
    curincrementalmrr__c numeric,
    datetrialclosedate__c date,
    datetrialenddate__c date,
    datetrialstartdate__c date,
    fmlchannelcountrycode__c character varying(8000),
    fmlchannelsalestype__c character varying(8000),
    fmlchanneluserrole__c character varying(8000),
    fmlchannel__c character varying(8000),
    strcompetitorsystem__c character varying(8000),
    object_type character varying(400)
);


--
-- Name: s_participants; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_participants (
    id uuid NOT NULL,
    conversation_id uuid,
    group_id uuid,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    group_type text
);


--
-- Name: s_recordtype; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_recordtype (
    businessprocessid character(400),
    createdbyid character(400),
    createddate timestamp without time zone,
    description character varying(8000),
    developername character varying(8000),
    id character(400) NOT NULL,
    isactive boolean,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    name character varying(8000),
    namespaceprefix character varying(8000),
    sobjecttype character varying(8000),
    systemmodstamp timestamp without time zone,
    object_type character varying(200)
);


--
-- Name: s_resources; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_resources (
    id numeric NOT NULL,
    merchant_profile_id numeric,
    name character varying(255),
    "position" numeric,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    visible boolean,
    all_services boolean,
    color character varying(255),
    bitstring text,
    bookable_id numeric,
    constraints_configuration json,
    constraints json,
    constraints_type character varying(255),
    uuid uuid,
    employee_id uuid
);


--
-- Name: s_services; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_services (
    id numeric NOT NULL,
    name character varying(255),
    description text,
    merchant_profile_id numeric,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    "position" numeric,
    requirements text,
    type character varying(255),
    color character varying(255),
    max_capacity numeric,
    bookable_id numeric,
    service_category_id numeric,
    price_cents numeric,
    deleted_at timestamp without time zone,
    uuid uuid,
    steps json,
    bookable_by_customer boolean,
    tax_category_id uuid
);


--
-- Name: s_shift_plan_templates; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_shift_plan_templates (
    merchant_profile_id numeric,
    name character varying(255),
    shift_params json,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    id uuid NOT NULL
);


--
-- Name: s_shifts; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_shifts (
    id uuid NOT NULL,
    resource_id numeric,
    starts_at timestamp(0) without time zone,
    ends_at timestamp(0) without time zone,
    kind text,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


--
-- Name: s_users; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_users (
    aboutme text,
    accountid character(400),
    alias character varying(8000),
    callcenterid character(400),
    city character varying(8000),
    communitynickname character varying(8000),
    companyname character varying(8000),
    contactid character(400),
    country character varying(8000),
    createdbyid character(400),
    createddate timestamp without time zone,
    currencyisocode character varying(1000),
    defaultcurrencyisocode character varying(1000),
    delegatedapproverid character(400),
    department character varying(8000),
    digestfrequency character varying(1000),
    division character varying(8000),
    email character varying(400),
    emailencodingkey character varying(1000),
    employeenumber character varying(8000),
    extension character varying(200),
    fax character varying(200),
    federationidentifier character varying(8000),
    firstname character varying(8000),
    forecastenabled boolean,
    fullphotourl character varying(2000),
    id character(400) NOT NULL,
    isactive boolean,
    isportalenabled boolean,
    languagelocalekey character varying(1000),
    lastlogindate timestamp without time zone,
    lastmodifiedbyid character(400),
    lastmodifieddate timestamp without time zone,
    lastname character varying(8000),
    lastpasswordchangedate timestamp without time zone,
    localesidkey character varying(1000),
    managerid character(400),
    mobilephone character varying(200),
    name character varying(8000),
    offlinepdatrialexpirationdate timestamp without time zone,
    offlinetrialexpirationdate timestamp without time zone,
    phone character varying(200),
    portalrole character varying(1000),
    postalcode character varying(8000),
    profileid character(400),
    receivesadmininfoemails boolean,
    receivesinfoemails boolean,
    smallphotourl character varying(2000),
    state character varying(8000),
    street text,
    systemmodstamp timestamp without time zone,
    team__c character varying(1000),
    timezonesidkey character varying(1000),
    title character varying(8000),
    userroleid character(400),
    usertype character varying(1000),
    username character varying(8000),
    bdisplayprofilepicturecompusersignature__c boolean,
    dgmtoffset__c numeric,
    plfinancialreporting_saleschannel__c character varying(1000),
    plgender__c character varying(1000),
    strmanagermail__c character varying(400),
    strorganisationnumber__c text,
    object_type character varying(200),
    urlzoomlink__c character varying(2000)
);


--
-- Name: s_bank_accounts; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_bank_accounts (
    id text NOT NULL,
    merchant_id uuid,
    object text,
    account_holder_name text,
    account_holder_type text,
    last4 text,
    bank_name text,
    country text,
    currency text,
    default_for_currency boolean,
    status text,
    routing_number text,
    meta jsonb,
    created integer
);


--
-- Name: s_charges; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_charges (
    stripe_charge_id text,
    merchant_id uuid,
    meta jsonb,
    amount integer,
    currency text,
    created timestamp(0) without time zone,
    status text,
    failure_code text,
    failure_message text,
    refund_ids text[],
    amount_refunded integer,
    customer_name text,
    customer_email text,
    customer_address jsonb,
    description text,
    services jsonb,
    captured boolean,
    origin text,
    id uuid NOT NULL,
    payments jsonb,
    gastrofix_charge_id uuid
);


--
-- Name: s_daily_events; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_daily_events (
    created_at date,
    event_type character varying(255),
    event_counts bigint
);


--
-- Name: s_daily_events_1; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_daily_events_1 (
    created_at date,
    event_type character varying(255),
    event_counts bigint
);


--
-- Name: s_disputes; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_disputes (
    id text NOT NULL,
    status text,
    reason text,
    amount integer,
    currency text,
    created timestamp(0) without time zone,
    due_by timestamp(0) without time zone,
    has_evidence boolean,
    past_due boolean,
    submission_count integer,
    charge_id uuid
);


--
-- Name: s_emails; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_emails (
    old_id integer,
    address character varying,
    message_id character varying,
    sent_at character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    publication_id uuid,
    category character varying,
    merchant_id uuid,
    receiver_id uuid,
    receiver_type character varying,
    id uuid NOT NULL
);


--
-- Name: s_merchants; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_merchants (
    id uuid NOT NULL,
    organization_id uuid
);


--
-- Name: s_publications; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_publications (
    id uuid NOT NULL,
    source_uuid uuid,
    source_type character varying,
    entries_count integer,
    is_completed boolean,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    merchant_id uuid
);


--
-- Name: s_request_logs; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_request_logs (
    id integer NOT NULL,
    path text,
    verb text,
    "user" text,
    ip_address text,
    "timestamp" timestamp without time zone,
    params jsonb
);


--
-- Name: s_sms; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_sms (
    id integer NOT NULL,
    phone_number character varying,
    message_id character varying,
    sent_at timestamp without time zone,
    receiver_id uuid,
    publication_id uuid,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    merchant_id uuid,
    category character varying,
    segments integer,
    receiver_type character varying
);


--
-- Name: s_stripe_events; Type: TABLE; Schema: stage; Owner: -
--

CREATE TABLE s_stripe_events (
    id text NOT NULL,
    object text,
    api_version text,
    created integer,
    data jsonb,
    livemode boolean,
    pending_webhooks integer,
    request text,
    type text
);


--
-- PostgreSQL database dump complete
--


merchantsALTER TABLE stage.s_sms OWNER TO segment; ALTER TABLE ONLY stage.s_sms ADD CONSTRAINT s_sms_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_emails OWNER TO segment; ALTER TABLE ONLY stage.s_emails ADD CONSTRAINT s_emails_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_publications OWNER TO segment; ALTER TABLE ONLY stage.s_publications ADD CONSTRAINT s_publications_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_merchants OWNER TO segment; ALTER TABLE ONLY stage.s_merchants ADD CONSTRAINT s_merchants_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_merchant_accounts OWNER TO segment; ALTER TABLE ONLY stage.s_merchant_accounts ADD CONSTRAINT s_merchant_accounts_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_daily_events OWNER TO segment; ALTER TABLE ONLY stage.s_daily_events ADD CONSTRAINT s_daily_events_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_daily_events_1 OWNER TO segment; ALTER TABLE ONLY stage.s_daily_events_1 ADD CONSTRAINT s_daily_events_1_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_contract OWNER TO segment; ALTER TABLE ONLY stage.s_contract ADD CONSTRAINT s_contract_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_onb2__invoice__c OWNER TO segment; ALTER TABLE ONLY stage.s_onb2__invoice__c ADD CONSTRAINT s_onb2__invoice__c_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_onb2__item__c OWNER TO segment; ALTER TABLE ONLY stage.s_onb2__item__c ADD CONSTRAINT s_onb2__item__c_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_conversation_senders OWNER TO segment; ALTER TABLE ONLY stage.s_conversation_senders ADD CONSTRAINT s_conversation_senders_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_merchant_customers OWNER TO segment; ALTER TABLE ONLY stage.s_merchant_customers ADD CONSTRAINT s_merchant_customers_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_employees OWNER TO segment; ALTER TABLE ONLY stage.s_employees ADD CONSTRAINT s_employees_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_merchant_key_accounts OWNER TO segment; ALTER TABLE ONLY stage.s_merchant_key_accounts ADD CONSTRAINT s_merchant_key_accounts_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.sf_cntrl_table OWNER TO segment; ALTER TABLE ONLY stage.sf_cntrl_table ADD CONSTRAINT sf_cntrl_table_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_appointment_series OWNER TO segment; ALTER TABLE ONLY stage.s_appointment_series ADD CONSTRAINT s_appointment_series_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_onb2__subscription__c OWNER TO segment; ALTER TABLE ONLY stage.s_onb2__subscription__c ADD CONSTRAINT s_onb2__subscription__c_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_onb2__dunningdetail__c OWNER TO segment; ALTER TABLE ONLY stage.s_onb2__dunningdetail__c ADD CONSTRAINT s_onb2__dunningdetail__c_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_lead OWNER TO segment; ALTER TABLE ONLY stage.s_lead ADD CONSTRAINT s_lead_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_disputes OWNER TO segment; ALTER TABLE ONLY stage.s_disputes ADD CONSTRAINT s_disputes_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_bank_accounts OWNER TO segment; ALTER TABLE ONLY stage.s_bank_accounts ADD CONSTRAINT s_bank_accounts_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_stripe_events OWNER TO segment; ALTER TABLE ONLY stage.s_stripe_events ADD CONSTRAINT s_stripe_events_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_request_logs OWNER TO segment; ALTER TABLE ONLY stage.s_request_logs ADD CONSTRAINT s_request_logs_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_newsletter_customers OWNER TO segment; ALTER TABLE ONLY stage.s_newsletter_customers ADD CONSTRAINT s_newsletter_customers_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.spc OWNER TO segment; ALTER TABLE ONLY stage.spc ADD CONSTRAINT spc_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_appointment_services OWNER TO segment; ALTER TABLE ONLY stage.s_appointment_services ADD CONSTRAINT s_appointment_services_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_users OWNER TO segment; ALTER TABLE ONLY stage.s_users ADD CONSTRAINT s_users_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_charges OWNER TO segment; ALTER TABLE ONLY stage.s_charges ADD CONSTRAINT s_charges_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.spu OWNER TO segment; ALTER TABLE ONLY stage.spu ADD CONSTRAINT spu_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_merchant_profiles OWNER TO segment; ALTER TABLE ONLY stage.s_merchant_profiles ADD CONSTRAINT s_merchant_profiles_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_opportunity OWNER TO segment; ALTER TABLE ONLY stage.s_opportunity ADD CONSTRAINT s_opportunity_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_recordtype OWNER TO segment; ALTER TABLE ONLY stage.s_recordtype ADD CONSTRAINT s_recordtype_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_onb2__balance__c OWNER TO segment; ALTER TABLE ONLY stage.s_onb2__balance__c ADD CONSTRAINT s_onb2__balance__c_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_account OWNER TO segment; ALTER TABLE ONLY stage.s_account ADD CONSTRAINT s_account_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_customers OWNER TO segment; ALTER TABLE ONLY stage.s_customers ADD CONSTRAINT s_customers_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_newsletters_nwsl OWNER TO segment; ALTER TABLE ONLY stage.s_newsletters_nwsl ADD CONSTRAINT s_newsletters_nwsl_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_newsletters OWNER TO segment; ALTER TABLE ONLY stage.s_newsletters ADD CONSTRAINT s_newsletters_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_event_participants OWNER TO segment; ALTER TABLE ONLY stage.s_event_participants ADD CONSTRAINT s_event_participants_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_contact OWNER TO segment; ALTER TABLE ONLY stage.s_contact ADD CONSTRAINT s_contact_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.sf_cntrl_table_2 OWNER TO segment; ALTER TABLE ONLY stage.sf_cntrl_table_2 ADD CONSTRAINT sf_cntrl_table_2_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_events OWNER TO segment; ALTER TABLE ONLY stage.s_events ADD CONSTRAINT s_events_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_feedbacks OWNER TO segment; ALTER TABLE ONLY stage.s_feedbacks ADD CONSTRAINT s_feedbacks_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_onb2__dunning__c OWNER TO segment; ALTER TABLE ONLY stage.s_onb2__dunning__c ADD CONSTRAINT s_onb2__dunning__c_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_resources OWNER TO segment; ALTER TABLE ONLY stage.s_resources ADD CONSTRAINT s_resources_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_appointment_resources OWNER TO segment; ALTER TABLE ONLY stage.s_appointment_resources ADD CONSTRAINT s_appointment_resources_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_services OWNER TO segment; ALTER TABLE ONLY stage.s_services ADD CONSTRAINT s_services_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_shift_plan_templates OWNER TO segment; ALTER TABLE ONLY stage.s_shift_plan_templates ADD CONSTRAINT s_shift_plan_templates_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_shifts OWNER TO segment; ALTER TABLE ONLY stage.s_shifts ADD CONSTRAINT s_shifts_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_conversations OWNER TO segment; ALTER TABLE ONLY stage.s_conversations ADD CONSTRAINT s_conversations_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_group_senders OWNER TO segment; ALTER TABLE ONLY stage.s_group_senders ADD CONSTRAINT s_group_senders_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_merchant_senders OWNER TO segment; ALTER TABLE ONLY stage.s_merchant_senders ADD CONSTRAINT s_merchant_senders_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_messages OWNER TO segment; ALTER TABLE ONLY stage.s_messages ADD CONSTRAINT s_messages_pkey PRIMARY KEY(id);merchants
merchantsALTER TABLE stage.s_participants OWNER TO segment; ALTER TABLE ONLY stage.s_participants ADD CONSTRAINT s_participants_pkey PRIMARY KEY(id);merchants

