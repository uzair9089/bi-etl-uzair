
"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: queries to select data from the sales force objects.
"""


onb2__invoice__c = """
select 
bESRExportDone__c	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
ESRExportDate__c	,
Id	,
IsDeleted	,
LastActivityDate	,
LastModifiedById	,
LastModifiedDate	,
Name	,
ONB2__Account__c	,
ONB2__AccountName__c	,
ONB2__Balance__c	,
ONB2__BalanceDifference__c	,
ONB2__BankAccount__c	,
ONB2__BankAccountOwner__c	,
ONB2__BankCode__c	,
ONB2__BillingAddress__c	,
ONB2__BillingCity__c	,
ONB2__BillingCountry__c	,
ONB2__BillingPostalCode__c	,
ONB2__BillingState__c	,
ONB2__BillingStreet__c	,
ONB2__CancelationReason__c	,
ONB2__CanceledWith__c	,
ONB2__Class__c	,
ONB2__Contact__c	,
ONB2__ConversionRate__c	,
ONB2__Date__c	,
ONB2__DaysOverdue__c	,
ONB2__DirectDebitMandateGranted__c	,
ONB2__DirectDebitMandateReference__c	,
ONB2__DirectDebitSequenceType__c	,
ONB2__DiscountAmount__c	,
ONB2__DiscountedNextPaymentDue__c	,
ONB2__DiscountedTotalGross__c	,
ONB2__DiscountMessage__c	,
ONB2__DiscountPaymentDue__c	,
ONB2__DiscountPaymentDueDate__c	,
ONB2__DiscountRate__c	,
ONB2__DisplayTransactionTables__c	,
ONB2__DisplayType__c	,
ONB2__DunningLevel__c	,
ONB2__Email__c	,
ONB2__EmailBCC__c	,
ONB2__EmailContact__c	,
ONB2__EmailError__c	,
ONB2__EmailFirstName__c	,
ONB2__EmailInvoice__c	,
ONB2__EmailInvoiceCc__c	,
ONB2__EmailLastName__c	,
ONB2__EmailSalutation__c	,
ONB2__EmailStatus__c	,
ONB2__Exported__c	,
ONB2__Footer__c	,
ONB2__GrandTotal__c	,
ONB2__GrossInvoice__c	,
ONB2__Header__c	,
ONB2__InfoLeft__c	,
ONB2__InfoRight__c	,
ONB2__Installment__c	,
ONB2__InvoiceRun__c	,
ONB2__LastDunningDate__c	,
ONB2__MailingCity__c	,
ONB2__MailingCountry__c	,
ONB2__MailingFirstName__c	,
ONB2__MailingLastName__c	,
ONB2__MailingPostalCode__c	,
ONB2__MailingSalutation__c	,
ONB2__MailingState__c	,
ONB2__MailingStreet__c	,
ONB2__NextPaymentDue__c	,
ONB2__NextPaymentDueDate__c	,
ONB2__OutstandingInvoicesText__c	,
ONB2__PageHeader__c	,
ONB2__PaymentCyclePeriod__c	,
ONB2__PaymentCycles__c	,
ONB2__PaymentDate__c	,
ONB2__PaymentDue__c	,
ONB2__PaymentDueDate__c	,
ONB2__PaymentInfo__c	,
ONB2__PaymentMethod__c	,
ONB2__PDF__c	,
ONB2__PrintContact__c	,
ONB2__PrintInvoice__c	,
ONB2__RecipientAddress__c	,
ONB2__RelatedInvoice__c	,
ONB2__Review__c	,
ONB2__SenderAddress__c	,
ONB2__SepaPaymentError__c	,
ONB2__ServicePeriodEnd__c	,
ONB2__ServicePeriodStart__c	,
ONB2__ShippingCity__c	,
ONB2__ShippingCountry__c	,
ONB2__ShippingPostalCode__c	,
ONB2__ShippingState__c	,
ONB2__ShippingStreet__c	,
ONB2__Status__c	,
ONB2__Subscription__c	,
ONB2__Template__c	,
ONB2__Tenant__c	,
ONB2__Text1__c	,
ONB2__Text2__c	,
ONB2__Text3__c	,
ONB2__TotalNet__c	,
ONB2__TotalTax__c	,
ONB2__Type__c	,
ONB2__UUID__c	,
OwnerId	,
SystemModstamp
from onb2__invoice__c  
"""



onb2__item__c = """ 
select 
bIsBundle__c	,
bIsHardware__c	,
bIsModule__c	,
bIsRecurring__c	,
bIsTrialItem__c	,
bRenewItem__c	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
fmlActiveMRR__c	,
fmlChannel__c	,
fmlDiscountedMRR__c	,
convertCurrency(fmlDiscountedMRR__c) to_euro_fmlDiscountedMRR__c,
fmlItemPriceDiscounted__c	,
fmlNextInvoiceValue__c	,
fmlNextRevenue__c	,
fmlTerm__c	,
Id	,
IsDeleted	,
LastModifiedById	,
LastModifiedDate	,
Name	,
ONB2__Active__c	,
ONB2__AdditionalDescription__c	,
ONB2__AdditionalTitle__c	,
ONB2__AggregateIndividualPriced__c	,
ONB2__BillingPeriod__c	,
ONB2__BillingType__c	,
ONB2__BillingUnit__c	,
ONB2__ChargeModel__c	,
ONB2__Commission__c	,
ONB2__ContractValue__c	,
ONB2__ContractValueCorrection__c	,
ONB2__ContractValueInvoiced__c	,
ONB2__ContractValueRemaining__c	,
ONB2__DecimalPlacesForQuantity__c	,
ONB2__DecimalPlacesForUnitPrice__c	,
ONB2__Description__c	,
ONB2__Discount__c	,
ONB2__DisplaySubtotalAfter__c	,
ONB2__EndDate__c	,
ONB2__GlobalMonthlyMinimum__c	,
ONB2__IgnoreCriterion__c	,
ONB2__InvoiceLineItemType__c	,
ONB2__NextInvoice__c	,
ONB2__Price__c	,
ONB2__PriceType__c	,
ONB2__ProductGroup__c	,
ONB2__Quantity__c	,
ONB2__Sequence__c	,
ONB2__StartDate__c	,
ONB2__Subscription__c	,
ONB2__SyncWith__c	,
ONB2__Title__c	,
ONB2__TransactionPriceField__c	,
ONB2__TransactionPriceTierQuantityField__c	,
ONB2__TransactionQuantityField__c	,
ONB2__TransactionType__c	,
ONB2__Unit__c	,
OwnerId	,
plChannelCountryCode__c	,
plChannelSalesType__c	,
plChannelUserRole__c	,
plFinancialReporting_ProductClass__c	,
refContract__c	,
refOpportunity__c	,
refParentItem__c	,
refProduct2__c	,
ruItemPrice__c	,
SalesMRR__c	,
strFinancialReporting_SalesChannel__c	,
strOpportunityProductId__c	,
strParentOpportunityProductId__c	,
SystemModstamp	from onb2__item__c 
"""


onb2__subscription__c = """ 
select 
bOpenPaymentCase__c	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
fmlChannel__c	,
Id	,
IsDeleted	,
LastActivityDate	,
LastModifiedById	,
LastModifiedDate	,
Name	,
ON_Type__c	,
ONB2__Account__c	,
ONB2__AggregationPeriod__c	,
ONB2__AutoRenewal__c	,
ONB2__BankAccount__c	,
ONB2__BankAccountOwner__c	,
ONB2__BankCode__c	,
ONB2__BillingPeriod__c	,
ONB2__CancelationDate__c	,
ONB2__CancelationTerm__c	,
ONB2__Contact__c	,
ONB2__DirectDebitMandateGranted__c	,
ONB2__DirectDebitMandateReference__c	,
ONB2__DirectDebitSequenceType__c	,
ONB2__DiscountPaymentDue__c	,
ONB2__DiscountRate__c	,
ONB2__DisplayTransactionTables__c	,
ONB2__EmailBCC__c	,
ONB2__EmailInvoice__c	,
ONB2__EmailInvoiceActive__c	,
ONB2__EmailInvoiceCc__c	,
ONB2__EndDate__c	,
ONB2__InvoicePaymentMethod__c	,
ONB2__LastError__c	,
ONB2__LastInvoiceRun__c	,
ONB2__LegalAccountName__c	,
ONB2__LegalCity__c	,
ONB2__LegalCountry__c	,
ONB2__LegalPostalCode__c	,
ONB2__LegalState__c	,
ONB2__LegalStreet__c	,
ONB2__NextInvoice__c	,
ONB2__PaymentCyclePeriod__c	,
ONB2__PaymentCycles__c	,
ONB2__PaymentDue__c	,
ONB2__PreferredInvoiceDate__c	,
ONB2__PriceIncrease__c	,
ONB2__PriceIncreaseDate__c	,
ONB2__PrintInvoice__c	,
ONB2__PrintInvoiceContact__c	,
ONB2__RenewalDate__c	,
ONB2__ReviewInvoice__c	,
ONB2__StartDate__c	,
ONB2__Status__c	,
ONB2__Template__c	,
ONB2__Tenant__c	,
OwnerId	,
plChannelCountryCode__c	,
plChannelSalesType__c	,
plChannelUserRole__c	,
refContract__c	,
SystemModstamp	from onb2__subscription__c 
"""




onb2__dunning__c = """ 
select 
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
ESRExportDate__c	,
Id	,
IsDeleted	,
LastActivityDate	,
LastModifiedById	,
LastModifiedDate	,
Name	,
ONB2__Account__c	,
ONB2__AccountName__c	,
ONB2__BillingAddress__c	,
ONB2__BillingCity__c	,
ONB2__BillingCountry__c	,
ONB2__BillingPostalCode__c	,
ONB2__BillingState__c	,
ONB2__BillingStreet__c	,
ONB2__Contact__c	,
ONB2__Date__c	,
ONB2__DisplayType__c	,
ONB2__DunningRun__c	,
ONB2__Email__c	,
ONB2__EmailBCC__c	,
ONB2__EmailCC__c	,
ONB2__EmailContact__c	,
ONB2__EmailDunning__c	,
ONB2__EmailError__c	,
ONB2__EmailFirstName__c	,
ONB2__EmailLastName__c	,
ONB2__EmailSalutation__c	,
ONB2__EmailStatus__c	,
ONB2__FlatFee__c	,
ONB2__Footer__c	,
ONB2__GrandTotal__c	,
ONB2__Header__c	,
ONB2__InfoLeft__c	,
ONB2__InfoRight__c	,
ONB2__LateFee__c	,
ONB2__Level__c	,
ONB2__MailingCity__c	,
ONB2__MailingContact__c	,
ONB2__MailingCountry__c	,
ONB2__MailingFirstName__c	,
ONB2__MailingLastName__c	,
ONB2__MailingPostalCode__c	,
ONB2__MailingSalutation__c	,
ONB2__MailingState__c	,
ONB2__MailingStreet__c	,
ONB2__MaxSequence__c	,
ONB2__PageHeader__c	,
ONB2__PaymentDue__c	,
ONB2__PaymentDueDate__c	,
ONB2__PDF__c	,
ONB2__PrintDunning__c	,
ONB2__RecipientAddress__c	,
ONB2__SenderAddress__c	,
ONB2__Status__c	,
ONB2__Template__c	,
ONB2__Tenant__c	,
ONB2__Text1__c	,
ONB2__Text2__c	,
ONB2__Text3__c	,
ONB2__Type__c	,
ONB2__UUID__c	,
OwnerId	,
strESRParticipantNumber__c	,
strESRReferenceNumber__c	,
SystemModstamp	 from onb2__dunning__c  
"""



onb2__dunningdetail__c = """ 
select 
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
Id	,
IsDeleted	,
LastModifiedById	,
LastModifiedDate	,
Name	,
ONB2__Amount__c	,
ONB2__BalanceDifference__c	,
ONB2__DaysOverdue__c	,
ONB2__Description__c	,
ONB2__Dunning__c	,
ONB2__DunningAmount__c	,
ONB2__GrandTotal__c	,
ONB2__Invoice__c	,
ONB2__LateFee__c	,
ONB2__PaymentDue__c	,
ONB2__PaymentDueDate__c	,
ONB2__PreviousFees__c	,
ONB2__Rate__c	,
ONB2__Sequence__c	,
ONB2__Title__c	,
ONB2__Type__c	,
SystemModstamp	 from onb2__dunningdetail__c 
"""


lead = """ 
select 
AnnualRevenue	,
bBelongsToChain__c	,
bDemoSetByOwner__c	,
bGotReferred__c	,
bOnlineBookingAvailable__c	,
bRejectLead__c	,
bSendEmailConfirmation__c	,
BSendInfoMaterial__c	,
bStarLead__c	,
City	,
Company	,
ConvertedAccountId	,
ConvertedContactId	,
ConvertedDate	,
ConvertedOpportunityId	,
Country	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
dNumberOfOutlets__c	,
Email	,
FirstName	,
Id	,
Industry	,
IsConverted	,
IsDeleted	,
IsUnreadByOwner	,
LastActivityDate	,
LastModifiedById	,
LastModifiedDate	,
LastName	,
LastTransferDate	,
LeadSource	,
MobilePhone	,
Name	,
NumberOfEmployees	,
OwnerId	,
Phone	,
plTemplateLanguage__c	,
plType__c	,
PostalCode	,
Rating	,
RecordTypeId	,
refAssignedTo__c	,
Salutation	,
State	,
Status	,
strCompetitorSystem__c	,
Street	,
SystemModstamp	,
Title	,
urlFacebookProfile__c	,
Website	 from Lead 
"""


user = """ 
select
AboutMe	,
AccountId	,
Alias	,
bDisplayProfilePictureCompUserSignature__c	,
CallCenterId	,
City	,
CommunityNickname	,
CompanyName	,
ContactId	,
Country	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
DefaultCurrencyIsoCode	,
DelegatedApproverId	,
Department	,
dGMTOffset__c	,
DigestFrequency	,
Division	,
Email	,
EmailEncodingKey	,
EmployeeNumber	,
Extension	,
Fax	,
FederationIdentifier	,
FirstName	,
ForecastEnabled	,
FullPhotoUrl	,
Id	,
IsActive	,
IsPortalEnabled	,
LanguageLocaleKey	,
LastLoginDate	,
LastModifiedById	,
LastModifiedDate	,
LastName	,
LastPasswordChangeDate	,
LocaleSidKey	,
ManagerId	,
MobilePhone	,
Name	,
OfflinePdaTrialExpirationDate	,
OfflineTrialExpirationDate	,
Phone	,
plFinancialReporting_SalesChannel__c	,
plGender__c	,
PortalRole	,
PostalCode	,
ProfileId	,
ReceivesAdminInfoEmails	,
ReceivesInfoEmails	,
SmallPhotoUrl	,
State	,
Street	,
strManagerMail__c	,
strOrganisationNumber__c	,
SystemModstamp	,
Team__c	,
TimeZoneSidKey	,
Title	,
urlZoomLink__c	,
Username	,
UserRoleId	,
UserType	 from user 
"""


contract = """ 
select 
AccountId	,
ActivatedById	,
ActivatedDate	,
bBonusOnHold__c	,
bEdgeCase__c	,
BillingCity	,
BillingCountry	,
BillingPostalCode	,
BillingState	,
BillingStreet	,
CompanySignedDate	,
CompanySignedId	,
ContractNumber	,
ContractTerm	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
CustomerSignedDate	,
CustomerSignedId	,
CustomerSignedTitle	,
dateCancellationPeriod__c	,
convertCurrency(dAverageSalesMRR__c),
dGuaranteedBookings__c	,
dYearlyDiscount__c	,
EndDate	,
Id	,
IsDeleted	,
LastActivityDate	,
LastApprovedDate	,
LastModifiedById	,
LastModifiedDate	,
Name	,
OwnerId	,
plEdgeCaseCategory__c	,
plMoneyBack__c	,
plPaymentCycle__c	,
plSpecialRightOfCancellation__c	,
plTrial__c	,
Pricebook2Id	,
RecordTypeId	,
refAccountmanager__c	,
refAccountmanagerCash__c	,
refBusinessOwner__c	,
refContactPerson__c	,
refOpportunity__c	,
refSubscription__c	,
ShippingCity	,
ShippingCountry	,
ShippingPostalCode	,
ShippingState	,
ShippingStreet	,
SpecialTerms	,
StartDate	,
Status	,
StatusCode	,
strFinancialReporting_SalesChannel__c	,
strPaymentMethod__c	,
SystemModstamp	from contract 
"""


recordtype = """ 
select 
BusinessProcessId	,
CreatedById	,
CreatedDate	,
Description	,
DeveloperName	,
Id	,
IsActive	,
LastModifiedById	,
LastModifiedDate	,
Name	,
NamespacePrefix	,
SobjectType	,
SystemModstamp	from recordtype 
"""



onb2__balance__c = """ 
select 
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
Id	,
IsDeleted	,
LastActivityDate	,
LastModifiedById	,
LastModifiedDate	,
Name	,
ONB2__Account__c	,
ONB2__Amount__c	,
ONB2__Date__c	,
ONB2__Dunning__c	,
ONB2__Invoice__c	,
ONB2__NoAutoAssignment__c	,
ONB2__PaymentMethod__c	,
ONB2__PaymentProvider__c	,
ONB2__Reference__c	,
ONB2__RelatedInvoice__c	,
ONB2__Subscription__c	,
ONB2__TransactionNo__c	,
ONB2__Type__c	,
SystemModstamp	from onb2__balance__c 
"""


contact = """ 
select
AccountId	,
Birthdate	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
Department	,
Email	,
FirstName	,
HomePhone	,
Id	,
IsDeleted	,
LastActivityDate	,
LastModifiedById	,
LastModifiedDate	,
LastName	,
LeadSource	,
MailingCity	,
MailingCountry	,
MailingPostalCode	,
MailingState	,
MailingStreet	,
MobilePhone	,
Name	,
OwnerId	,
Phone	,
RecordTypeId	,
ReportsToId	,
Salutation	,
SystemModstamp	,
Title	from contact 
"""


account = """ 
select 
bAccountRisk__c	,
bActive__c	,
BillingCity	,
BillingCountry	,
BillingPostalCode	,
BillingState	,
BillingStreet	,
bIsPartner__c	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
curMRR__c,
dateDateCustomerImport__c	,
dateDebtCollectionInitiated__c	,
dateInternalUse__c	,
dateScall__c	,
dateTrialEnd__c	,
dateTrialStart__c	,
dateWidgetIn__c	,
dCRMScore__c	,
dCustomerScore__c	,

dInventoryScore__c	,
dKeyAccountId__c	,
dShopId__c	,
dtActivationDate__c	,
dtCRNumberOfCustomersImported__c	,
dtOnboardingDate__c	,
dTotalEngagementScore__c	,
dTractionScore__c	,
fmlSubscriptionStatus__c,
Id	,
Industry	,
IsDeleted	,
LastActivityDate	,
LastModifiedById	,
LastModifiedDate	,
Merchant_Happiness__c	,
Name	,
NumberOfEmployees	,
OwnerId	,
ParentId	,
Phone	,
plCreditworthiness__c	,
plCustomerDataInfo__c	,
plSubcategory__c	,
Rating	,
RecordTypeId	,
refActiveSubscription__c	,
strCreditScore__c	,
strMerchantUUID__c	,
Type	,
urlLinkToSuccessStory__c	,
Website,
SystemModstamp,
dGoogleAnalyticsID__c	from Account 
"""

opportunity = """ 
select 
AccountId,
Amount,
bDemoSetByOwner__c,
bOnlineBookingAvailable__c,
bTrialClosed__c,
CloseDate,
CreatedById,
CreatedDate,
convertcurrency(curIncrementalMRR__c),
CurrencyIsoCode,
dateTrialCloseDate__c,
dateTrialEndDate__c,
dateTrialStartDate__c,
fmlChannel__c,
fmlChannelCountryCode__c,
fmlChannelSalesType__c,
fmlChannelUserRole__c,
HasOpportunityLineItem,
Id,
IsClosed,
IsDeleted,
IsWon,
LastActivityDate,
LastModifiedById,
LastModifiedDate,
LeadSource,
Name,
NextStep,
OwnerId,
Pricebook2Id,
Probability,
RecordTypeId,
StageName,
strCompetitorSystem__c,
SystemModstamp,
TotalOpportunityQuantity,
Type from opportunity
"""



asset = """ 
select AccountId,
ContactId,
CreatedById,
CreatedDate,
CurrencyIsoCode,
dateUsageStartDate__c,
Description,
Id,
InstallDate,
IsCompetitorProduct,
IsDeleted,
LastModifiedById,
LastModifiedDate,
LastReferencedDate,
LastViewedDate,
Name,
Price,
Product2Id,
PurchaseDate,
Quantity,
refCompanySignedBy__c,
refContract__c,
refSubscriptionItem__c,
refSubscription__c,
SerialNumber,
Status,
SystemModstamp,
UsageEndDate
from Asset
"""

onb2__dunningrun__c = """ 
select
CreatedById,
CreatedDate,
CurrencyIsoCode,
Id,
IsDeleted,
LastActivityDate,
LastModifiedById,
LastModifiedDate,
LastReferencedDate,
LastViewedDate,
Name,
ONB2__DunningDate__c,
ONB2__DunningLevel__c,
ONB2__Duration__c,
OwnerId,
SystemModstamp
from ONB2__DunningRun__c
"""

onb2__invoicelineitem__c = """
select 
CreatedById,
CreatedDate,
CurrencyIsoCode,
Id,
IsDeleted,
LastModifiedById,
LastModifiedDate,
Name,
ONB2__AppliedTaxRule__c,
ONB2__BaseQuantity__c,
ONB2__BilledOpportunityObject__c,
ONB2__BilledOpportunity__c,
ONB2__BillingFactor__c,
ONB2__BillingUnit__c,
ONB2__CalculatedBillingFactor__c,
ONB2__CalculatedCommission__c,
ONB2__Center__c,
ONB2__Commission__c,
ONB2__DecimalPlacesForQuantity__c,
ONB2__DecimalPlacesForUnitPrice__c,
ONB2__Description__c,
ONB2__DiscountAmount__c,
ONB2__Discount__c,
ONB2__DisplayQuantity__c,
ONB2__DisplaySubtotalAfter__c,
ONB2__FactorizedUnitPrice__c,
ONB2__Factor__c,
ONB2__GLAccount__c,
ONB2__GrossInvoice__c,
ONB2__Invoice__c,
ONB2__IsDiscountEmpty__c,
ONB2__IsFinal__c,
ONB2__Item__c,
ONB2__PosTotalGross__c,
ONB2__PosTotalNet__c,
ONB2__PosTotalTax__c,
ONB2__PriceTierQuantity__c,
ONB2__ProductCode__c,
ONB2__ProductGroup__c,
ONB2__Quantity__c,
ONB2__RelatedInvoice__c,
ONB2__RelatedLineItem__c,
ONB2__Sequence__c,
ONB2__SerializedTransaction__c,
ONB2__ServicePeriodEnd__c,
ONB2__ServicePeriodStart__c,
ONB2__TaxRate__c,
ONB2__Title__c,
ONB2__TransactionCriterion__c,
ONB2__Type__c,
ONB2__UnitPriceGross__c,
ONB2__UnitPriceNet__c,
ONB2__UnitPriceTax__c,
ONB2__UnitPrice__c,
ONB2__Unit__c,
SystemModstamp 
from ONB2__InvoiceLineItem__c
"""


onb2__invoicerun__c = """
select 
CreatedById,
CreatedDate,
CurrencyIsoCode,
Id,
IsDeleted,
LastActivityDate,
LastModifiedById,
LastModifiedDate,
LastReferencedDate,
LastViewedDate,
Name,ONB2__Duration__c,
ONB2__Filter__c,
ONB2__InvoiceDate__c,
ONB2__NumInvoices__c,
ONB2__NumNegativeInvoices__c,
ONB2__NumPositiveInvoices__c,
ONB2__OpportunityFilter__c,
ONB2__PeriodEndDate__c,
ONB2__PeriodStartDate__c,
ONB2__TotalInvoicedAmountNet__c,
ONB2__TotalNegativeInvoicedAmountNet__c,
ONB2__TotalPositiveInvoicedAmountNet__c,
ONB2__TransactionFilter__c,
OwnerId,
SystemModstamp 
from ONB2__InvoiceRun__c
"""

order = """
select 
AccountId,
ActivatedById,
ActivatedDate,
BillingAddress,
BillingCity,
BillingCountry,
BillingCountryCode,
BillingPostalCode,
BillingState,
BillingStateCode,
BillingStreet,
ContractId,
CreatedById,
CreatedDate,
CurrencyIsoCode,
EffectiveDate,
EndDate,
Id,
IsDeleted,
IsReductionOrder,
LastModifiedById,
LastModifiedDate,
LastReferencedDate,
LastViewedDate,
OpportunityId,
OrderNumber,
OriginalOrderId,
OwnerId,
Pricebook2Id,
RecordTypeId,
ShippingAddress,
ShippingCity,
ShippingCountry,
ShippingCountryCode,
ShippingLongitude,
ShippingPostalCode,
ShippingState,
ShippingStateCode,
ShippingStreet,
Status,
StatusCode,
SystemModstamp,
TotalAmount,
Type 
from Order
"""


leadhistory= """
select
CreatedById,
CreatedDate,
Field,
Id,
IsDeleted,
LeadId,
NewValue,
OldValue 
from LeadHistory
"""


specs__c= """
select
bChurnRelevant__c,
CreatedById,
CreatedDate,
curAfflictedMRR__c,
CurrencyIsoCode,
Id,
IsDeleted,
LastActivityDate,
LastModifiedById,
LastModifiedDate,
LastReferencedDate,
LastViewedDate,
Name,
OwnerId,
plDepartments__c,
plFeatureScope__c,
plPriority__c,
plProduct__c,
plSquad__c,
plStatus__c,
RecordTypeId,
strDescription__c,
strDueDate__c,
strExpectedBehaviour__c,
strITComment__c,
strSeenBehaviour__c,
SystemModstamp,
Vorraussichtlich_abgeschlossen_am__c 
from Specs__c
"""

case_churn = """
select AccountId	,
bChurnSavedByShortenedContractTerm__c	,
bOnHold__c	,
ClosedDate	,
CreatedById	,
CreatedDate	,
curDiscountgranted__c	,
curDowngradedModulesMRRValue__c	,
curFeatureMRRValue__c	,
curModulesMRRValue__c	,
curMonthsforfreeMRRValue__c	,
CurrencyIsoCode	,
curShortenedContractTermMRRValue__c	,
dateOnHoldUntil__c	,
Description	,
Id	,
IsClosed	,
IsDeleted	,
IsEscalated	,
LastModifiedById	,
LastModifiedDate	,
LastReferencedDate	,
LastViewedDate	,
Origin	,
OwnerId	,
ParentId	,
plCaseCategory__c	,
plCaseReasonOnHold__c	,
plChurnSaved__c	,
plChurnSource__c	,
plDowngradedModules__c	,
plFeatureusedtosaveChurn__c	,
plMerchantHappiness__c	,
plModulesUsedToSaveChurn__c	,
plOutcome__c	,
plSubcategoriesChurnCaseReasons__c	,
Priority	,
Reason	,
RecordTypeId	,
refChurnProcessedBy__c	,
refSpec__c	,
Status	,
strClosingComment__c   ,
Subject	,
SystemModstamp	,
Type 
from case
"""



case_success = """
select AccountId	,
bCustomerImport__c	,
bLicenceUpgrade__c	,
bMerchantAppUsage__c	,
bNoCustomerData__c	,
bOnHold__c	,
bSendNewsletterWithMerchant__c	,
bShoreService__c	,
ClosedDate	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
dateCustomerImport__c	,
Description	,
dNumberOfAppDownloads__c	,
Id	,
IsClosed	,
IsDeleted	,
IsEscalated	,
LastModifiedById	,
LastModifiedDate	,
LastReferencedDate	,
LastViewedDate	,
Origin	,
OwnerId	,
ParentId	,
plCaseRisk__c	,
plMerchantHappiness__c	,
plMissingFeatures__c	,
plReactivationStatus__c	,
plUpsellingPotential__c	,
Priority	,
Reason	,
RecordTypeId	,
refUserUpselling__c	,
Status	,
strClosingComment__c	,
strUpsellingInfo__c	,
Subject	,
SystemModstamp	,
Type	
from case
"""


case_onboarding = """
select AccountId	,
bCustomerImport__c	,
bFacebookWidget__c	,
bInternalUse__c	,
bLoginDataAtONB__c	,
bNewsletterSent__c	,
bOnHold__c	,
bShoreApp__c	,
bShoreCash__c	,
bShoreNetwork__c	,
bShoreNetworkSynced__c	,
bShoreWebsite__c	,
bWidgetIn__c	,
ClosedDate	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
dateCustomerImport__c	,
dateDateWidgetIn__c	,
DateImplementationDate__c	,
dateInternalUseSet__c	,
dateNextPossibleCancellation__c	,
Description	,
dNumberOfCustomersImported__c	,
Id	,
IsClosed	,
IsDeleted	,
IsEscalated	,
LastModifiedById	,
LastModifiedDate	,
LastReferencedDate	,
LastViewedDate	,
Origin	,
OwnerId	,
ParentId	,
plCaseReasonOnHold__c	,
plCaseRisk__c	,
plMerchantHappiness__c	,
plMissingFeatures__c	,
plQualityOfInternalUse__c	,
plReasonFailed__c	,
plWidgetVisibility__c	,
Priority	,
Reason	,
RecordTypeId	,
Status	,
strClosingComment__c	,
strContractCompanySigned__c	,
Subject	,
SystemModstamp	,
Type	,
urlWidgetURL__c	
from case
"""


case_shoreapp = """
select AccountId	,
bInAppStore__c	,
bInGooglePlay__c	,
bOnHold__c	,
ClosedDate	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
dateDateDummyAppCreated__c	,
dateOnHoldUntil__c	,
dateSubmittedToAppStoreDate__c	,
Description	,
Id	,
intNumberOfModules__c	,
IsClosed	,
IsDeleted	,
IsEscalated	,
LastModifiedById	,
LastModifiedDate	,
LastReferencedDate	,
LastViewedDate	,
Origin	,
OwnerId	,
ParentId	,
plCaseReasonOnHold__c	,
plDummyApp__c	,
plMerchantHappiness__c	,
plPicturesOrigin__c	,
plReasonFailed__c	,
Priority	,
Reason	,
RecordTypeId	,
Status	,
strClosingComment__c	,
Subject	,
SystemModstamp	,
Type	,
urlAppLink__c	,
urlAppStoreLink__c	,
urlGooglePlayLink__c	 
from case
"""


case_website = """
select AccountId	,
bConsistency__c	,
bOnHold__c	,
bWidgetIn__c	,
ClosedDate	,
CreatedById	,
CreatedDate	,
CurrencyIsoCode	,
dateDateDummyWebsiteCreated__c	,
dateDateWebsiteCall__c	,
dateDateWidgetIn__c	,
dateOnHoldUntil__c	,
dBeautyScore__c	,
Description	,
dGoogleAnalyticsID__c	,
dSEOScore__c	,
Id	,
IsClosed	,
IsDeleted	,
IsEscalated	,
LastModifiedById	,
LastModifiedDate	,
LastReferencedDate	,
LastViewedDate	,
Origin	,
OwnerId	,
ParentId	,
plCaseReasonOnHold__c	,
plDataPrivacy__c	,
plDomainBy__c	,
plDummyWebsite__c	,
plMerchantHappiness__c	,
plPicturesOrigin__c	,
plWidgetVisibility__c	,
Priority	,
Reason	,
RecordTypeId	,
Status	,
strClosingComment__c	,
Subject	,
SystemModstamp	,
Type	,
urlWidgetURL__c	
from case
"""



