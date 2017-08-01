from sqlalchemy import create_engine
from threading import Thread, Lock
from param import param
from etl_delta_load import delta_query
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import pandas as pd
import psycopg2
import os
import json
import sys
import csv
#reload(sys)
#sys.setdefaultencoding('utf8')

class SubscriptionParser:

	def parser(self, collection_name):

		try:
			tag_lst = ('uuid', 'state', 'unit_amount_in_cents', 'currency', 'quantity', 'activated_at', 'canceled_at', 'expires_at', 'updated_at', 'total_billing_cycles', 'remaining_billing_cycles')
			tag_sub_lst = ('plan', 'subscription_add_ons')
			xml_list = []
			lst = (collection_name.getchildren()) # get subscription
			i = 0
			while i < len(lst): 
				sub_lst = lst[i].getchildren() # get subscription.children == account, uuid, etc.
				j = 0
				inner_xml_dict = {}
				while j < len(sub_lst): 
					if sub_lst[j].tag in tag_lst:
						inner_xml_dict[sub_lst[j].tag] = sub_lst[j].text # add account, uuid, etc. with value to dict
					
					# additional if clause for plan, because it has a nested xml
					if sub_lst[j].tag == 'plan': #in tag_sub_lst:
						sub_sub_lst = sub_lst[j].getchildren() # get children of plan
						k = 0
						while k < len(sub_sub_lst):
							inner_xml_dict[sub_lst[j].tag + '_' + sub_sub_lst[k].tag] = sub_sub_lst[k].text # add plan childs to dict
							k += 1
					
					# additional if clause for subscription_add_ons, because it has a nested xml
					if sub_lst[j].tag == 'subscription_add_ons':
						sub_sub_lst = sub_lst[j].getchildren() # get subscription_add_on
						k = 0
						add_ons_dict = {}
						subscription_add_ons_list = {}
						while k < len(sub_sub_lst): # iterate over all subscription_add_ons
							l = 0
							add_on_dict = {} #  create new help dict
							sub_sub_sub_lst = sub_sub_lst[k].getchildren()
							while l < len(sub_sub_sub_lst): # get childs within subscription add on
								add_on_dict[sub_sub_sub_lst[l].tag] = sub_sub_sub_lst[l].text
								if sub_sub_sub_lst[l].tag in ('unit_amount_in_cents', 'quantity'	):
									add_on_dict[sub_sub_sub_lst[l].tag] = int(sub_sub_sub_lst[l].text)
								else:
									add_on_dict[sub_sub_sub_lst[l].tag] = sub_sub_sub_lst[l].text
								l += 1
							k += 1
							subscription_add_ons_list['sub_add_on_'+str(k)] = add_on_dict # put all addons in a list
						inner_xml_dict['subscription_add_ons'] = subscription_add_ons_list # add the list to the dictionary
						inner_xml_dict['subscription_add_ons'] = json.dumps(inner_xml_dict['subscription_add_ons'])
					j += 1
				i += 1
				xml_list.append(inner_xml_dict)

			df = pd.DataFrame(xml_list)
			df['unit_amount_in_cents'] = df['unit_amount_in_cents'].astype(int)
			df['activated_at'] = pd.to_datetime(df['activated_at'], format= '%Y-%m-%dT%H:%M:%SZ')
			df['updated_at'] = pd.to_datetime(df['updated_at'], format= '%Y-%m-%dT%H:%M:%SZ')
			df['expires_at'] = pd.to_datetime(df['expires_at'], format= '%Y-%m-%dT%H:%M:%SZ')
			df['canceled_at'] = pd.to_datetime(df['canceled_at'], format= '%Y-%m-%dT%H:%M:%SZ')

			df = df.reindex(columns=['uuid', 'state', 'unit_amount_in_cents', 'currency', 'quantity', 'activated_at', 'canceled_at', 'expires_at', 'updated_at', 'total_billing_cycles', 'remaining_billing_cycles', 'plan_name', 'plan_plan_code', 'subscription_add_ons'])
			df.to_csv(param.newpath+collection_name.tag +'.csv',sep=',' ,index= False, header=False)

		except Exception as e:
			print('Failed to parse the Subscription XML')
