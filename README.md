dnswebservices
==============

Windows DNS RESTful Web Service (wrapper for dnscmd.exe command-line)

Como este é um wrapper do dnscmd.exe você pode dar uma olhada na documentacao oficial da Microsoft [1].

Entretando, as funções implementadas nesse momento são:

   * /ZoneList = Lista as zonas (EnumZones)
   * /ZonePrint = Lista uma determinada zona
   * /RecordAddForm = Formulario para adicionar um novo registro
   * /RecordDeleteForm = Formulario para remover um registro
   * /RecordAdd = Funcao para adicionar um registro
   * /RecordDelete = Funcao para remover um registro
   * /help = Imprime este help

# Exemplos:

Listar registros de uma zona (GET): home.infra
============================
<pre>curl http://192.168.0.254:8080/ZonePrint/home.infra</pre>

Listar todas as zonas do DNS (GET)
============================
<pre>curl http://192.168.0.254:8080/ZoneList/all</pre>

Criar um novo registro (POST): mypc.home.infra A 10.20.30.1
============================
<pre>curl -d "ZoneName=home.infra&RecordName=mypc&TypeRecord=A&IP=10.20.30.1" http://192.168.0.254:8080/RecordAdd</pre>

Remover um registro (POST): mypc.home.infra A 10.20.30.1
============================
<pre>curl -d "ZoneName=home.infra&RecordName=mypc&TypeRecord=A&IP=10.20.30.1" http://192.168.0.254:8080/RecordDelete</pre>

Caso você não queira utilizar a linha de comando com uma API, também existe um formuário bem básico via web.

# INSTALAÇÃO

Este serviço deverá ser executado no seu servidor de DNS (Microsoft Windows 2003 ou 2008), para executar você precisará:

* Python 2.7 [2]
* Bottle [3]

[1]: http://technet.microsoft.com/en-us/library/cc772069%28v=ws.10%29.aspx
[2]: http://www.python.org/download/releases/2.7.3/
[3]: http://bottlepy.org/docs/dev/
