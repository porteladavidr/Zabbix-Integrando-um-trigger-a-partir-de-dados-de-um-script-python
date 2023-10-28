# Zabbix-Integrando-um-trigger-a-partir-de-dados-de-um-script-python
Passo-a-passo como realizar a integração da saída de um script python em uma trigger do Zabbix.

# Especificações:<br />
Python: Versão 3<br />
Zabbix: Versão 6.4.7<br />
Server: Ubuntu server 22.04.3 LTS<br />


# Criando o Python Script<br />
Neste laborário nosso script estará sendo executado direto no servidor do Zabbix. Para melhor organizar iremos inicialmente criar um diretório para armazenar os scripts que desejamos integrar com o Zabbix.<br />

- No meu caso criei o diretório Zabbix na Home:<br />
<pre class="notranslate"><code class="notranslate">mkdir /home/zabbix/
</code></pre>

No nosso laboratório vamos criar um script que checa a conexão com determinado site e apreseta o retorno da mesma. Logo, com o diretório já criado iremos criar o arquivo do nosso script Python:<br />

- Navegue até a pasta do arquivo:<br />
<pre class="notranslate"><code class="notranslate">cd /home/zabbix
</code></pre>

- Crie o arquivo do script (Chamei o meu de conexao):<br />
<pre class="notranslate"><code class="notranslate">sudo nano conexao.py
</code></pre>

- Cole o código do script:<br />
** Você pode copiar o código contido neste repositório do ghithub **

# Adicionando a execução do script Python no config do Zabbix Agent do servidor<br />
Neste passo iremos adicionar as configurações necessárias no Zabbix Agent para que o Script possa se comunicar com a ferramenta.

- Acesse o documento de configuração:<br />
<pre class="notranslate"><code class="notranslate">sudo nano /etc/zabbix/zabbix_agentd.conf
</code></pre>

Altere a seção ### Option: AllowKey adicionando após as linhas comentadas a seguinte configuração:<br />
<pre class="notranslate"><code class="notranslate">AllowKey=system.run[python3 /home/zabbix/conexao.py]
</code></pre>


# Criando um Item no Zabbix para receber a saída do script<br />
Neste passo iremos adicionar um item que irá receber a saída do nosso script e será usado na criação da nossa trigger.<br />
Observação: Este item deve ser adicionado a um Host que já esteja em conexão com o Servidor. Se o mesmo não existir você deverá criar.

** Configurações do Item **<br />
- Nome: Adicione um nome da sua escolha <br />
- Tipo: Zabbix Agent<br />
- Chave: system.run[python3 /home/zabbix/conexao.py]<br />
- Tipo de informação: Texto<br />
- Interface do Host: Interface em questão do servidor<br />
- Intervalo de atualização: 10s

# Criando o Trigger para gerar o Alerta<br />
Neste passo vamos para o alerta em questão, vamos vincular o Trigger as configurações anteriormente criadas

** Configuração do Trigger **<br />
- Nome: Adicione um nome a sua escolha<br />
- Expressão: last(/PythonServer/system.run[python3 /home/zabbix/conexao.py])="O site está online e acessível."

Observação: Na expressão você pode clicar em adicionar e ir seguindo os passos do autocomplete que a ferramenta fornece. Neste caso passei uma opção de alertar caso o site esteja acessível pois o teste já será apresentado como válido. Porém no mundo real o teste é ao contrário.

**Depois de fazer alterações na configuração, reinicie e verifique o status**
<pre class="notranslate"><code class="notranslate">sudo service zabbix-agent restart
</code></pre>
<pre class="notranslate"><code class="notranslate">sudo service zabbix-agent status
</code></pre>
