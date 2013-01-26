from bottle import route, run, template, error, get, post, request, abort
import os, time, sys, getpass, subprocess


HTML = """\
<html>
<head>
  <style type="text/css">
  body {
	font-family: Verdana, Geneva, Arial, Helvetica, sans-serif;
	font-size: 12px;
	color: black; }
  </style>

</head>
<body>
  <font class="Texto">
    {{ data }}
  </font>
</body>
</html>
"""

@route('/')
@route('/index.html')
def dns_index():
	return("<h3>Este eh um servico web para manipular o DNS do Windows, RESTFul. Acesse <a href='/help'> /help</a> para saber as formas de uso.</h3>")

@route('/help', methoed='GET')
def dns_help(name='help'):
    return """Windows DNS RESTful Web Service<br><br>Como este eh um wrapper do dnscmd.exe voce pode dar uma olhada na <a href='http://technet.microsoft.com/en-us/library/cc772069%28v=ws.10%29.aspx' target='_blank'>documentacao oficial da Microsoft.</a><br>
	Entretando, as funcoes implementadas nesse momento(e voce pode fazer um fork e contribuir) sao:<br>
	/ZoneList = Lista as zonas (EnumZones)<br>
	/ZonePrint/<nome da zona> = Lista uma determinada zona<br>
	/RecordAddForm = Formulario para adicionar um novo registro<br>
	/RecordDeleteForm = Formulario para remover um registro<br>
	/RecordAdd = Funcao para adicionar um registro<br>
	/RecordDelete = Funcao para remover um registro<br>
	/help = Imprime este help<br><br>"""

@route('/ZoneList/<name>', method='GET')
def dns_zonelist(name='ZoneList'):
	
	output = subprocess.Popen('"c:\Program Files\Support Tools\dnscmd.exe" /EnumZones', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = output.communicate()
	return ("<pre>saida %s</pre>" % (out))


@route('/ZonePrint/<name>', method='GET')
def dns_zoneprint( name="Print zone names" ):
	ZoneName = name
	output = subprocess.Popen('"c:\Program Files\Support Tools\dnscmd.exe" /ZonePrint %s' % ZoneName , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
	out, err = output.communicate()
	return ("<pre>saida %s</pre>" % (out))


@route('/test/<name>', method='GET')
def testes(name="testes"):
	var1=name
	return (var1)


@route('/RecordAddForm', method='GET')
def upload_view():
	return """
	<form action="/RecordAdd" method="post" enctype="multipart/form-data">
	ZoneName (ex: contoso.com):<input type="text" name="ZoneName" /><br>
	RecordName (ex:mypc):<input type="text" name="RecordName" /><br>
	TypeRecord (ex: A):<input type="text" name="TypeRecord" /><br>
	IP (ex: 10.20.3.1): <input type="text" name="IP" /><br>
	<input type="submit" name="submit" value="Adicionar" />
	</form>
	"""

@route('/RecordDeleteForm', method='GET')
def upload_view():
	return """
	<form action="/RecordDelete" method="post" enctype="multipart/form-data">
	ZoneName (ex: contoso.com):<input type="text" name="ZoneName" /><br>
	RecordName (ex:mypc):<input type="text" name="RecordName" /><br>
	TypeRecord (ex: A):<input type="text" name="TypeRecord" /><br>
	IP (ex: 10.20.3.1): <input type="text" name="IP" /><br>
	<input type="submit" name="submit" value="!!!REMOVER!!!" />
	</form>
	"""

@route('/RecordAdd', method='POST')
def dns_recordadd():
	ZoneName = request.forms.get('ZoneName')
	RecordName = request.forms.get('RecordName')
	TypeRecord = request.forms.get('TypeRecord')
	IP = request.forms.get('IP')
	if ZoneName is not None and RecordName is not None and TypeRecord is not None and IP is not None:
		msg="dnscmd /RecordAdd %s %s %s %s" % (ZoneName,RecordName,TypeRecord,IP)

		output = subprocess.Popen('"c:\Program Files\Support Tools\dnscmd.exe" /RecordAdd %s %s %s %s' % (ZoneName,RecordName,TypeRecord,IP) , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
		out, err = output.communicate()
		return ("<pre>saida %s %s</pre>" % (msg,out))
	return "You missed a field."

@route('/RecordDelete', method='POST')
def dns_recorddelete():
	ZoneName = request.forms.get('ZoneName')
	RecordName = request.forms.get('RecordName')
	TypeRecord = request.forms.get('TypeRecord')
	IP = request.forms.get('IP')
	if ZoneName is not None and RecordName is not None and TypeRecord is not None and IP is not None:
		msg="dnscmd /RecordDelete %s %s %s %s" % (ZoneName,RecordName,TypeRecord,IP)

		output = subprocess.Popen('"c:\Program Files\Support Tools\dnscmd.exe" /RecordDelete %s %s %s %s /f' % (ZoneName,RecordName,TypeRecord,IP) , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
		out, err = output.communicate()
		return ("<pre>saida %s %s</pre>" % (msg,out))
	return "You missed a field."

@error(404)
def error404(error):
    return '<h1>404 Not Found</h1>'

run(host='', port=8080, debug=True, reloader=True)