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




settings={'dbuser': 'app', 'dbname': 'microfin', 'dbpassword': 'Vostro1310', 'dbhost': 'localhost', 'dbport': '3308'}
settings['program_name']='Migracion_SAFI'
def task(requests):
    db=Connector(**settings)
    result=db.get(requests)
    return [result.data]

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
    parameters=[1004,0]
    lista_creditos=Request.Generic('MIGCREPAGCRELIST',parameters)
    results=[]
    data=safi.get(lista_creditos)    
    
    filas=len(data.data)
    print(data.data)
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

                                                                                       
                request_list=Request.GenericBulk('simulador',data_block,repository.migracion).map(CreditoID='CreditoID',
                                                                                                Monto='Monto',
                                                                                                MontoCuota='MontoCuota',
                                                                                                Tasa='Tasa',
                                                                                                Frecu='Frecu',
                                                                                                PagoCuota='PagoCuota',
                                                                                                PagoFinalAni='PagoFinAni',
                                                                                                DiaMes='DiaMesCap',
                                                                                                FechaInicio='FechaInicio',
                                                                                                NumeroCuotas='NumeroCuotas',
                                                                                                ProdCredito='ProducCredito',
                                                                                                ClienteID='ClienteID',
                                                                                                DiaHabilSig='DiaHabilSig',
                                                                                                AjustaFecAmo='AjustaFecAmo',
                                                                                                AjusFecExiVen='AjusFecExiVen',
                                                                                                ComAper='ComAper',
                                                                                                MontoGL='MontoGL',
                                                                                                CobraSeguroCuota='CobraSeguroCuota',
                                                                                                CobraIVASeguroCuota='CobraIVASeguroCuota',
                                                                                                MontoSeguroCupota='MontoSeguroCuota',
                                                                                                ComAnualLin='ComAnualLin',
                                                                                                FechaVenPrimAmo='NumTransaccion');


                                                                                                

                                                                                                
                #request_list=Request.Bulk('deposito',data_block).map(CuentaAhoID='CuentaID', CantidadMov='Pago',Par_Fecha='FechaEmision',Par_FechaAplicacion='FechaEmision')


                with Pool(NUM_THREADS) as pool:
                    n= n + len(request_list)
                    results.append(pool.map_async(task, request_list,chunksize=5, callback=progress(n)))
                    pool.close() # for async
                    pool.join() # for async 
            
            for res in results:
                 for r in res:
                      print(r)
            print('Registros:' + str(data.rowcount)) 
            print(f'Loops procesados: { item } ')
            print(f'items procesados: { r } ')
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
