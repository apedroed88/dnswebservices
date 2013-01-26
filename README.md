dnswebservices
==============

Windows DNS RESTful Web Service (wrapper for dnscmd.exe command-line)

Como este eh um wrapper do dnscmd.exe voce pode dar uma olhada na [1]documentacao oficial da Microsoft.

Entretando, as funções implementadas nesse momento  são:

   /ZoneList = Lista as zonas (EnumZones)
   /ZonePrint = Lista uma determinada zona
   /RecordAddForm = Formulario para adicionar um novo registro
   /RecordDeleteForm = Formulario para remover um registro
   /RecordAdd = Funcao para adicionar um registro
   /RecordDelete = Funcao para remover um registro
   /help = Imprime este help

Exemplos:

# Listar registros de uma zona (GET): home.infra
curl http://192.168.0.254:8080/ZonePrint/home.infra

# Listar todas as zonas do DNS (GET)
curl http://192.168.0.254:8080/ZoneList/all

# Criar um novo registro (POST): mypc.home.infra A 10.20.30.1
curl -d "ZoneName=home.infra&RecordName=mypc&TypeRecord=A&IP=10.20.30.1" http://192.168.0.254:8080/RecordAdd

# Remover um registro (POST): mypc.home.infra A 10.20.30.1
curl -d "ZoneName=home.infra&RecordName=mypc&TypeRecord=A&IP=10.20.30.1" http://192.168.0.254:8080/RecordDelete

Caso você não queira utilizar a linha de comando com uma API, também existe um formuário bem básico via web.
