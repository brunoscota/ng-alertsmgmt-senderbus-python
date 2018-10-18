from azure.servicebus import ServiceBusService
from azure.servicebus import Message
from dotenv import load_dotenv
import argparse
import os
load_dotenv('./.env')


parser = argparse.ArgumentParser(description='Popule the message fields to send to an ServiceBus TOPIC in Azure')
parser.add_argument('-H','--hostname', type=str, required=True,
                   help='Set the Hostname')
parser.add_argument('-S','--service', type=str, required=True,
                   help='Set the service name')                   
parser.add_argument('-A','--address', type=str, required=True,
                   help='Set the IP Address')                   
parser.add_argument('-C','--state', type=str, required=True,
                   help='Set the service state')                   
parser.add_argument('-T','--summary', type=str, required=True,
                   help='Set the summary')                                      
parser.add_argument('-D','--datetime', type=str, required=True, 
                   help='Set the datetime')                                      

args = parser.parse_args()

sbs = ServiceBusService(os.getenv('SERVICE_NAMESPACE'),
                        shared_access_key_name=os.getenv('KEY_NAME'),
                        shared_access_key_value=os.getenv('KEY_VALUE'))

msg = Message(body="SQLGENERIC CRITICAL - 1", custom_properties={
    'hostname':args.hostname,
    'service':args.service,
    'address':args.address,
    'state':args.state,
    'summary':args.summary,
    'datetime':args.datetime})



sbs.send_topic_message(os.getenv('TOPIC'), msg)