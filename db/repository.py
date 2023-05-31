from datetime import datetime
from decimal import Decimal

migracion=[
	{'routine':'MIGCREPAGCRECAMORTERTPRO',
		'keyword':'simulador',
		'output':'message',
		'parameters':[{  'order':1, 'name':'CreditoID', 'type': int, 'default':0, 'required':True     },
					{  'order':2, 'name':'Monto', 'type':datetime, 'default':"1900-01-01", 'required':True     },
					{  'order':3, 'name':'MontoCuota', 'type':datetime, 'default':"1900-01-01", 'required':True     },
					{  'order':3, 'name':'Tasa', 'type':Decimal, 'default':True, 'required':True },
					{  'order':4, 'name':'Frecu', 'type':str, 'default':"N",   'required':False      },
                              {  'order':5, 'name':'PagoCuota', 'type':str, 'default':"N",   'required':False      },
                              {  'order':6, 'name':'PagoFinAni', 'type':str, 'default':"N",   'required':False      },
                              {  'order':7, 'name':'DiaMes', 'type':str, 'default':"N",   'required':False      },
                              {  'order':8, 'name':'FechaInicio', 'type':str, 'default':"N",   'required':False      },
                              {  'order':9, 'name':'NumeroCuotas', 'type':str, 'default':"N",   'required':False      },
                              {  'order':10, 'name':'ProdCredito', 'type':str, 'default':"N",   'required':False      },
                              {  'order':11, 'name':'ClienteID', 'type':str, 'default':"N",   'required':False      },
                              {  'order':12, 'name':'DiaHabilSig', 'type':str, 'default':"N",   'required':False      },
                              {  'order':13, 'name':'AjustaFecAmo', 'type':str, 'default':"N",   'required':False      },
                              {  'order':14, 'name':'AjusFecExiVen', 'type':str, 'default':"N",   'required':False      },
                              {  'order':15, 'name':'ComAper', 'type':str, 'default':"N",   'required':False      },
                              {  'order':17, 'name':'MontoGL', 'type':str, 'default':"N",   'required':False      },
                              {  'order':18, 'name':'CobraSeguroCuota', 'type':str, 'default':"N",   'required':False      },
                              {  'order':19, 'name':'CobraIVASeguroCuota', 'type':str, 'default':"N",   'required':False      },
                              {  'order':20, 'name':'MontoSeguroCuota', 'type':str, 'default':"N",   'required':False      },
                              {  'order':21, 'name':'ComAnualLin', 'type':str, 'default':"N",   'required':False      },
                              {  'order':22, 'name':'FechaVenPrimAmortiCap', 'type':str, 'default':"N",   'required':False      },
                              {  'order':23, 'name':'Salida', 'type':str, 'default':"S",   'required':False      },
                              {  'order':24, 'name':'EmpresaID', 'type':str, 'default':1,   'required':False      },
                              {  'order':25, 'name':'Usuario', 'type':str, 'default':1,   'required':False      },
                              {  'order':26, 'name':'FechaActual', 'type':str, 'default':'1900-01-01',   'required':False      },
                              {  'order':27, 'name':'DireccionIP', 'type':str, 'default':'127.0.0.1',   'required':False      },
                              {  'order':28, 'name':'ProgramaID', 'type':str, 'default':"migracion",   'required':False      },
                              {  'order':29, 'name':'Sucursal', 'type':str, 'default':0,              'required':False      },
                              {  'order':30, 'name':'NumTransaccion', 'type':str, 'default':0,   'required':False      },
                              
                              

                      
                      
				]
		},
            ]