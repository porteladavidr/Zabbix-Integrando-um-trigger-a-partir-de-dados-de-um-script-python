# Zabbix-Integrando-um-trigger-a-partir-de-dados-de-um-script-python
Passo-a-passo como realizar a integração da saída de um script python em uma trigger do Zabbix.

# Especificações:<br />
Python: Versão 3<br />
Zabbix: Versão 6.4.7<br />
Server: Ubuntu server 22.04.3 LTS<br />


# Criando o Python Script<br />
Neste laborário nosso script estará sendo executado direto no servidor do Zabbix. Para melhor organizar iremos inicialmente criar um diretório para armazenar os scripts que desejamos integrar com o Zabbix.<br />
No meu caso criei o diretório Zabbix na Home:<br />

<pre class="notranslate"><code class="notranslate">mkdir /home/zabbix/
</code></pre>

No nosso laboratório vamos criar um script que checa a conexão com determinado site e apreseta o retorno da mesma. Logo, com o diretório já criado iremos criar o arquivo do nosso script Python:<br />

Navegue até a pasta do arquivo:<br />
<pre class="notranslate"><code class="notranslate">cd /home/zabbix
</code></pre>
