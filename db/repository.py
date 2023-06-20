from datetime import datetime
from decimal import Decimal

migracion=[
	{'routine':'MIGT_PLANDEPAGOSPRO',
		'keyword':'tabla_pagos',
		'output':'message',
		'parameters':[{'order':1, 'name':'CreditoID', 'type': int, 'default':0, 'required':True     },
                          {'order':2, 'name':'FechaCorte', 'type': str, 'default':0, 'required':True     },
                          {'order':3, 'name':'Salida', 'type': str, 'default':'S', 'required':True     },
                          {'order':1, 'name':'NumTransaccion', 'type': int, 'default':0, 'required':True     }
                      
				]
		},
            ]