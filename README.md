# Zabbix-Integrando-um-trigger-a-partir-de-dados-de-um-script-python
Passo-a-passo como realizar a integração da saída de um script python em uma trigger do Zabbix.

# Especificações:<br />
Python: Versão 3<br />
Zabbix: Versão 6.4.7<br />
Server: Ubuntu server 22.04.3 LTS<br />


# Criando o Python Script<br />
Neste laborário nosso script estará sendo executado direto no servidor do Zabbix. Para melhor organizar iremos inicialmente criar um diretório para armazenar os scripts que desejamos integrar com o Zabbix.<br />
No meu caso criei o diretório Zabbix na Home:<br />

<code class="notranslate">mkdir /home/zabbix/</code>
