from core_app.models import HistoryAlarmas, AlarmaReportada, Inmueble, Elemento, Evento, Sensor,Alarma as MyAlarm,AlarmaEstado,AlarmaAcceso,AlarmaHumo
import getpass
import datetime
from MySmartHome.settings import NAME_DB, USER_DB, HOST_DB, PWD_DB
import psycopg2
from core_app.correo import  correo

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



    def consul_sensores(self, user_id, tipo_sensor):
        result = []

        inmbs = Inmueble.objects.all().filter(user = user_id)
        
        for im in inmbs:
            result.extend(list(self.consul_sensores_inmb(inmueb_id = im.id, tipo_sensor = tipo_sensor)))

        
        return result 

    def consul_sensores_inmb(self, inmueb_id, tipo_sensor ): 
        result = []

        elems = Elemento.objects.all().filter(inmueble = inmueb_id)
        if (elems.__len__() > 0):           
            for e in elems:
                result.extend(list(self.consul_elementos_sensor(elem_id = e.id,  tipo_sensor = tipo_sensor)))
#        else:
#            if (sw == '1'):
#                eventos = "Inmueble sin elementos"
#                result.append(eventos)      
        return result

    def consul_elementos_sensor(self, elem_id, tipo_sensor):
        result  = []
        
        
        for x in list(Sensor.objects.all().filter(activo__id = elem_id, tipo_sensor__id = tipo_sensor
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
            print('paso 3')
            for x in list(HistoryAlarmas.objects.all().filter(sensor__activo__id = elem_id, fecha__gte = fech_1
                        ).select_related('alarmaReportada__alarma__sensor__activo__inmueble', 'alarmaReportada__alarma__sensor__tiposensor'
                                ).values( 'fecha_hora', 'alarma__sensor__tipo_sensor__nombre', 
                                         'alarma__sensor__activo__inmueble__nombre', 'alarma__sensor__activo__nombre', 'alarma__sensor__nombre'
                                ).order_by('-fecha_hora')[:20]):
                        #'prioridad', 
                result.append(x)
                                                         
        else:
            print('paso 4')
            if (fech_2 != None and fech_1 != None):
                print('paso 5')
                for x in list(AlarmaReportada.objects.all().filter(alarma__sensor__activo__id = elem_id, fecha_hora__range = [fech_1, fech_2]
                            ).select_related('alarmaReportada__alarma__sensor__activo__inmueble', 'alarmaReportada__alarma__sensor__tiposensor'
                                ).values( 'fecha_hora', 'alarma__nivel_alarma', 'alarma__nombre', 'alarma__descripcion', 'alarma__sensor__tipo_sensor__nombre', 
                                         'alarma__sensor__activo__inmueble__nombre', 'alarma__sensor__activo__nombre', 'alarma__sensor__nombre'
                                ).order_by('-fecha_hora')[:20]):
                
                    print('paso 6')
                    result.append(x)
            
            else:
                print('paso 7')
                if (fech_1 == None and fech_2 != None):
                    print('paso 8')
                    for x in list(AlarmaReportada.objects.all().filter(alarma__sensor__activo__id = elem_id, fecha_hora__lte = fech_2
                                ).select_related('alarmaReportada__alarma__sensor__activo__inmueble', 'alarmaReportada__alarma__sensor__tiposensor'
                                ).values( 'fecha_hora', 'alarma__nivel_alarma', 'alarma__nombre', 'alarma__descripcion', 'alarma__sensor__tipo_sensor__nombre', 
                                         'alarma__sensor__activo__inmueble__nombre', 'alarma__sensor__activo__nombre', 'alarma__sensor__nombre'
                                ).order_by('-fecha_hora')[:20]):
                    #Evento.objects.get(Q(question__startswith='Who'), Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))
                        print('paso 9')
                        result.append(x)
                
                else:
                    print('paso A')
                    for x in list(AlarmaReportada.objects.all().filter(alarma__sensor__activo__id = elem_id
                                ).select_related('alarmaReportada__alarma__sensor__activo__inmueble', 'alarmaReportada__alarma__sensor__tiposensor'
                                ).values( 'fecha_hora', 'alarma__nivel_alarma', 'alarma__nombre', 'alarma__descripcion', 'alarma__sensor__tipo_sensor__nombre', 
                                         'alarma__sensor__activo__inmueble__nombre', 'alarma__sensor__activo__nombre', 'alarma__sensor__nombre'
                                ).order_by('-fecha_hora')[:20]):
                        print('paso B')
                        result.append(x)
                        #'fecha', 'sensor__tipo_sensor__nombre', 
                        #                 'sensor__activo__inmueble__nombre', 'sensor__activo__nombre', 'sensor__nombre'

        return result

    def validaHorarios(self,alarma,alarmaEstado,evento):
        ret = False
        print('id alarma '+ str(alarma.sensor.tipo_sensor.id))
        print('hora alarma '+ str(alarmaEstado.hora_inicio))
        print('hora fin alarma '+ str(alarmaEstado.hora_fin))
        print('hora evento '+ str(evento.fecha_hora_evento))

        segMax = self.getSec(s='23:59:59')
        segIni = self.getSec(s=str(alarmaEstado.hora_inicio))
        segFin = self.getSec(s=str(alarmaEstado.hora_fin))
        segEve = self.getSec(s=str(str(evento.fecha_hora_evento.hour)+':'+str(evento.fecha_hora_evento.minute)+':'+str(evento.fecha_hora_evento.second)))

        print('seg max '+ str(segMax))
        print('seg ini '+ str(segIni))
        print('seg fin '+ str(segFin))
        print('seg act '+ str(segEve))

        if segIni > segFin:
            if (segEve>=segIni and segEve<=segMax):
                print('entra a horario noche')
                ret = True
            elif (segEve>=0 and segEve<=segFin):
                print('entra a horario nocturno')
                ret = True
        elif segIni < segFin:
            if (segEve>=segIni and segEve<=segFin):
                print('entra a horario diurno')
                ret = True
        elif segIni == segFin:
            if (segEve==segIni):
                print('entra a horario fijo')
                ret = True

        return ret




    def GeneraAlarma(self,alarma,evento,user):
        print('genera alarma ')
        ##Otras clases
        if alarma.activa == False or alarma.activa == 0 or alarma.activa == '0':
            print('alarma inactiva')
            return 0;

        registro = AlarmaReportada(
            fecha_hora     = evento.fecha_hora_evento,
            #user      = models.ForeignKey(User)
            #elemento  = alarma.sensor.activo ,
            #inmueble  = alarma.sensor.activo.inmueble,
            #sensor   = alarma.sensor,
            alarma   = alarma,
            nivel_alerta = alarma.nivel_alarma,
            descripcion = evento.nombre)
        registro.save()
        if alarma.notifica == 1 or alarma.notifica == '1' or alarma.notifica == True:
            c = correo.myCorreo()
            c.enviarGmail(tipo_alarma=alarma.nivel_alarma,
                          destinatario=user.email,activo=alarma.sensor.activo.nombre)
            #    actualización de estado
            elem = Elemento.objects.all().filter(sensor__id = evento.sensor).select_related('sensor__activo__elemento')
            elem.set_estado(1)
            #    actualización de estado
        print('ya genero alarma '+str(registro))

        return 0

    def getSec(self,s):
        
        l = s.split(':')
        return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

    def validarAlarma(self,evento,user):
        result  = []
        print('entra a validar alarma '+str(evento.sensor))

        alarms = MyAlarm.objects.all().filter(sensor__id = evento.sensor.id)
        for alarma in alarms:
            tipo_alarma = int(alarma.sensor.tipo_sensor.id)


            if tipo_alarma == 1:
                print('id alarma humo '+ str(alarma.sensor.tipo_sensor.id))
                self.GeneraAlarma(alarma,evento,user)
            elif tipo_alarma == 2:
                alarmaEstado = AlarmaEstado.objects.get(pk = alarma.id)
                ret = self.validaHorarios(alarma=alarma,alarmaEstado=alarmaEstado,evento=evento)
                if ret == True :
                    if int(evento.codigo) == int(alarmaEstado.estado_sensor):
                        self.GeneraAlarma(alarma,evento,user)

            elif tipo_alarma == 3:
                print('id alarma ingreso '+ str(alarma.sensor.tipo_sensor.id))
                alarmaAcceso = AlarmaAcceso.objects.get(pk = alarma.id)
                ret =  self.validaHorarios(alarma=alarma,alarmaEstado=alarmaAcceso,evento=evento)
                if ret == True :
                        self.GeneraAlarma(alarma,evento,user)
            elif tipo_alarma == 4:
                print('id alarma estado '+ str(alarma.sensor.tipo_sensor.id))
                alarmaEstado = AlarmaEstado.objects.get(pk = alarma.id)
                ret = self.validaHorarios(alarma=alarma,alarmaEstado=alarmaEstado,evento=evento)
                if ret == True :
                    print('id alarma estado '+ str(evento.codigo)+'--'+str(alarmaEstado.estado_sensor))
                    if int(evento.codigo) == int(alarmaEstado.estado_sensor):
                        self.GeneraAlarma(alarma,evento,user)


                print('alarma '+ str(alarma))
                print('id alarma '+ str(alarma.sensor.tipo_sensor.id))
        
        return result

    #metodo que verifica el estado de la notificacion si ya fue leida o no
    def hayNuevasNotificaciones(self,userId):

        numAlarma = AlarmaReportada.objects.all().filter(
                    alarma__sensor__activo__user_id=userId)

        if(numAlarma.__len__() > 0):
            numAlarma = AlarmaReportada.objects.all().filter(
                    alarma__sensor__activo__user_id=userId,
                    leida=0)
            if(numAlarma.__len__() > 0):
                res = True
            else:
                res = False
        else:
            res = False
        return res

    def contarNuevasNotificaciones(self,userId):
        numAlarma = AlarmaReportada.objects.all().filter(
                    alarma__sensor__activo__user_id=userId,
                    leida=0)

        if(numAlarma.__len__() > 0):
            res = numAlarma.__len__()
        else:
            res = 0
        return res
