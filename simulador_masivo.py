import sys
from  safi.core import Connector,Request,Utils
from safi import keywords as key
#from  os import path
from datetime import datetime
from decimal import Decimal
from db import repository
import logging
from multiprocessing import Process,Pool
import asyncio
import time




settings={'dbuser': 'root', 'dbname': 'microfinTS', 'dbpassword': 'Vostro1310', 'dbhost': 'localhost', 'dbport': '3308'}
settings['program_name']='Migracion_SAFI'
def task(requests):
    db=Connector(**settings)
   # print(requests.parameters)
    default_error={'NUMERR':999,'ERRMEN':'OCURRIO UN ERROR'}
    output=[]
    try:
        result=db.get(requests)
    except Exception as e:
        output.append(default_error)
        return output
    
    return result.data

def progress(n):
    n=n+1
    print(n, end='\r', flush=True)
    #return n




def main():

    print(f'Hora de inicio:{datetime.now()}')
    inicio=datetime.now()
    POOL_SIZE=40
    NUM_THREADS=8
    #settings=Utils.load_settings('pgss.settings')
    #print(settings)

    safi=Connector(**settings)
    parameters=['2022-12-31']
    lista_creditos=Request.Generic('MIGT_CREDITOSLIST',parameters)
    async_results=[]
    data=safi.get(lista_creditos)    
    
    filas=len(data.data)
    #print(data.data)
    print('Creditos por Procesar:' + str(len(data.data)))   
  
  
    if(data):                       
            block_generator=Utils.paginate(data.data,POOL_SIZE)
            n=0
            r=0
            item=0
            request_list=[]
            for data_block in block_generator: 
                item=item+1 
                for datarow in data_block :
                    r=r+1

                                                                                       
                request_list=Request.GenericBulk('tabla_pagos',data_block,repository.migracion).map(CreditoID='CreditoID',FechaCorte='FechaCorte',Salida='Salida',NumTransaccion='NumTransaccion')


                with Pool(NUM_THREADS) as pool:
                    n= n + len(request_list)
                    async_results.append(pool.map_async(task, request_list,chunksize=4, callback=progress(n)))
                    pool.close() # for async
                    pool.join() # for async 
            
            exitosos=0
            fallidos=0
            for res in async_results:
                
                block_results= res.get( timeout=60)
                for result in block_results:
                    code=result[0]['NUMERR']
                    #print(result)
                    if code>0 :
                        fallidos+=1
                    else:
                        exitosos +=1
     
                          
            print('Registros:' + str(data.rowcount)) 
            print(f'Loops procesados: { item } ')
            print(f'items procesados: { r } ,  exitosos {exitosos }, fallidos { fallidos }')
            print(' \n.')
    
    fin=datetime.now()
    duracion=inicio-fin
    print('Duration: {}'.format(fin - inicio))



if __name__ == '__main__':
    main()

                


                

        #print(data)
        #print('done..')
 
#-------------------------------------------------------------------------
#  RUN !
#-------------------------------------------------------------------------
     


#--------------------------------------------------------------------------






#9:20


#14:18
#14:34

# primer ronda
#2023-02-14 14:44:17.106308
#2023-02-14 15:00:30.122035###
##
##
##

# 2023-02-14 16:45:12.332747
