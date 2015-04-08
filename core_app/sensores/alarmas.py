from core_app.models import HistoryAlarmas, AlarmaReportada, Inmueble, Elemento, Evento, Sensor,Alarma as MyAlarm
import getpass
import datetime
from MySmartHome.settings import NAME_DB, USER_DB, HOST_DB, PWD_DB
import psycopg2

class Alarma:        
    
    def reg_act_alarmas(self, id_estado, fech, id_inmb, id_elemen):
        
        ha = HistoryAlarmas(estado = id_estado, fecha = fech, user = self.request.user, inmueble  = id_inmb, 
                            elemento = id_elemen)
        ha.save()
        
    def consul_events(self, user_id, fech_1, fech_2):
        result = []

        inmbs = Inmueble.objects.all().filter(user = user_id)
        
        for im in inmbs:
            result.extend(list(self.consul_events_inmb(inmueb_id = im.id, fecha1 = fech_1, fecha2 = fech_2)))
        
        return result 
    
    def consul_events_inmb(self, inmueb_id, fecha1, fecha2): 
        result = []

        elems = Elemento.objects.all().filter(inmueble = inmueb_id)
        if (elems.__len__() > 0):           
            for e in elems:
                result.extend(list(self.consul_events_elem(elem_id = e.id , fech_1 = fecha1, fech_2 = fecha2)))                       
#        else:
#            if (sw == '1'):
#                eventos = "Inmueble sin elementos"
#                result.append(eventos)      
        return result
    
    def consul_events_elem(self, elem_id, fech_1, fech_2):
        result  = []
        
        if (fech_1 != None and fech_2 == None):            
            for x in list(Evento.objects.all().filter(sensor__activo__id = elem_id, fecha_hora_evento__gte = fech_1
                        ).select_related('evento__sensor__activo__inmueble', 'evento__sensor__tiposensor'
                        ).values('nombre', 'fecha_hora_evento', 'codigo', 'sensor__tipo_sensor__nombre', 
                                 'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'
                        ).order_by('-fecha_hora_evento')[:20]):
                        #'prioridad', 
                result.append(x)
                                                         
        else:
            if (fech_2 != None and fech_1 != None):
                for x in list(Evento.objects.all().filter(sensor__activo__id = elem_id, fecha_hora_evento__range = [fech_1, fech_2]
                            ).select_related('evento__sensor__activo__inmueble', 'evento__sensor__tiposensor'
                            ).values('nombre', 'fecha_hora_evento', 'codigo', 'sensor__tipo_sensor__nombre', 
                                     'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'
                            ).order_by('-fecha_hora_evento')[:20]):
                
                    result.append(x)
            
            else:
                if (fech_1 == None and fech_2 != None):
                    for x in list(Evento.objects.all().filter(sensor__activo__id = elem_id, fecha_hora_evento__lte = fech_2
                                ).select_related('evento__sensor__activo__inmueble', 'evento__sensor__tiposensor'
                                ).values('nombre', 'fecha_hora_evento', 'codigo', 'sensor__tipo_sensor__nombre', 
                                         'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'
                                ).order_by('-fecha_hora_evento')[:20]):
                    #Evento.objects.get(Q(question__startswith='Who'), Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))
                        result.append(x)
                
                else:
                    for x in list(Evento.objects.all().filter(sensor__activo__id = elem_id
                                ).select_related('evento__sensor__activo__inmueble', 'evento__sensor__tiposensor'
                                ).values('nombre', 'fecha_hora_evento', 'codigo', 'sensor__tipo_sensor__nombre', 
                                         'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'
                                ).order_by('-fecha_hora_evento')[:20]):
                        result.append(x)

        return result



    def consul_elementos_sensor(self, tipo_sensor):
        result  = []
        
        
        for x in list(Sensor.objects.all().filter(tipo_sensor__id = tipo_sensor
                    ).select_related('sensor__activo', 'sensor__tiposensor'
                    ).values().order_by('-id')[:20]):
            result.append(x)

        return result



    def consul_alarms(self, user_id,tipo_sensor_id):
        result = []

        inmbs = Inmueble.objects.all().filter(user = user_id)
        
        for im in inmbs:
            result.extend(list(self.consul_alarms_inmb(inmueb_id = im.id, tipo_sensor_id = tipo_sensor_id)))
        
        return result 
    
    def consul_alarms_inmb(self, inmueb_id,tipo_sensor_id): 
        result = []

        elems = Elemento.objects.all().filter(inmueble = inmueb_id)
        
        if (elems.__len__() > 0):           
            for e in elems:
                result.extend(list(self.consul_alarms_elem(elem_id = e.id,tipo_sensor_id=tipo_sensor_id )))

        return result

    def consul_alarms_elem(self, elem_id,tipo_sensor_id):

        result  = []
        if tipo_sensor_id != 0 and tipo_sensor_id != '' and tipo_sensor_id != '0':
            
            for x in list(MyAlarm.objects.all().filter(sensor__activo__id = elem_id, sensor__tipo_sensor__id= tipo_sensor_id
                    ).select_related('alarma__sensor__activo__inmueble', 'alarma__sensor__tiposensor'
                    ).values('id','nombre', 'descripcion', 'sensor__tipo_sensor__nombre', 'sensor__tipo_sensor_id'
                             'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre','nivel_alarma'
                    ).order_by('-id')[:20]):
                result.append(x)
        else:
            print('paso 5 '+str(elem_id))
            for x in list(MyAlarm.objects.all().filter(sensor__activo__id = elem_id
                    ).select_related('alarma__sensor__activo__inmueble', 'alarma__sensor__tiposensor'
                    ).values('id','nombre', 'descripcion', 'sensor__tipo_sensor__nombre', 
                             'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre','nivel_alarma'
                    ).order_by('-id')[:20]):
                result.append(x)
                print('paso 6 '+str(elem_id))



        return result


               
    def consul_history(self, user_id, fech_1, fech_2):
        result = []

        inmbs = Inmueble.objects.all().filter(user = user_id)

        print('paso 1' +str(inmbs))
        
        for im in inmbs:
            result.extend(list(self.consul_history_inmb(inmueb_id = im.id, fecha1 = fech_1, fecha2 = fech_2)))
        
        return result 
    
    def consul_history_inmb(self, inmueb_id, fecha1, fecha2): 
        result = []

        elems = Elemento.objects.all().filter(inmueble = inmueb_id)
        print('paso 2' +str(elems))
        if (elems.__len__() > 0):           
            for e in elems:
                result.extend(list(self.consul_history_elem(elem_id = e.id , fech_1 = fecha1, fech_2 = fecha2)))                       
#        else:
#            if (sw == '1'):
#                eventos = "Inmueble sin elementos"
#                result.append(eventos)      
        return result
    
    def consul_history_elem(self, elem_id, fech_1, fech_2):
        result  = []
        

        if (fech_1 != None and fech_2 == None):            
            for x in list(HistoryAlarmas.objects.all().filter(sensor__activo__id = elem_id, fecha__gte = fech_1
                        ).select_related('evento__sensor__activo__inmueble', 'evento__sensor__tiposensor'
                        ).values('nombre', 'fecha_hora_evento', 'codigo', 'sensor__tipo_sensor__nombre', 
                                 'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'
                        ).order_by('-fecha_hora_evento')[:20]):
                        #'prioridad', 
                result.append(x)
                                                         
        else:
            if (fech_2 != None and fech_1 != None):
                for x in list(HistoryAlarmas.objects.all().filter(sensor__activo__id = elem_id, fecha__range = [fech_1, fech_2]
                            ).select_related('evento__sensor__activo__inmueble', 'evento__sensor__tiposensor'
                            ).values('nombre', 'fecha_hora_evento', 'codigo', 'sensor__tipo_sensor__nombre', 
                                     'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'
                            ).order_by('-fecha_hora_evento')[:20]):
                
                    result.append(x)
            
            else:
                if (fech_1 == None and fech_2 != None):
                    for x in list(HistoryAlarmas.objects.all().filter(sensor__activo__id = elem_id, fecha__lte = fech_2
                                ).select_related('evento__sensor__activo__inmueble', 'evento__sensor__tiposensor'
                                ).values('nombre', 'fecha_hora_evento', 'codigo', 'sensor__tipo_sensor__nombre', 
                                         'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'
                                ).order_by('-fecha_hora_evento')[:20]):
                    #Evento.objects.get(Q(question__startswith='Who'), Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))
                        result.append(x)
                
                else:
                    print('paso 3 '+str(elem_id))
                    for x in list(AlarmaReportada.objects.all().filter(alarma__sensor__activo__id = elem_id
                                ).select_related('alarmaReportada__alarma__sensor__activo__inmueble', 'alarmaReportada__alarma__sensor__tiposensor'
                                ).values( 'fecha_hora', 'alarma__sensor__tipo_sensor__nombre', 
                                         'alarma__sensor__activo__inmueble__nombre', 'alarma__sensor__activo__nombre', 'alarma__sensor__nombre'
                                ).order_by('-fecha_hora')[:20]):
                        print('paso 4' +str(x))
                        result.append(x)
                        #'fecha', 'sensor__tipo_sensor__nombre', 
                        #                 'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'

        return result
