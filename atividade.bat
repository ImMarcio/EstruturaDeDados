
 
@echo off
setlocal enabledelayedexpansion

:menu
cls
echo Escolha um comando:
echo 1. Este comando lista todos os computadores na rede, incluindo
seus nomes, grupos de trabalho e compartilhamentos.
echo 2. Este comando lista todos os computadores na rede
echo 3. Este comando exibe a tabela ARP.
echo 4. Exibir informações do sistema
echo 5. Este comando lista todos os compartilhamentos no computador atual.
echo 6. Ping um site
echo 7. exibir informações sobre as conexões de rede ativas, portas abertas e processos 
echo 8. Mostrar informações de rede
echo 9. Encerrar o programa
echo 0. Limpar a tela
set /p escolha=Digite o número do comando desejado: 



if "%escolha%"=="9" (
    goto :eof
)

if "%escolha%" NEQ "" (
    set comando=!escolha!
    set conceito=
    
    if "%escolha%"=="1" (
        echo exibe informações sobre os perfis de rede sem fio
        netsh wlan show profile feito
        set conceito=exibe informações sobre os perfis de rede sem fio
    ) else if "%escolha%"=="2" (
        echo Este comando exibe uma lista de todos os processos que estão em execução no sistema.
        tasklist 
        set conceito=Este comando exibe uma lista de todos os processos que estão em execução no sistema.
    ) else if "%escolha%"=="3" (
        echo Este comando exibe a tabela ARP.
        arp -a feito
        set conceito=Este comando exibe a tabela ARP.
    ) else if "%escolha%"=="4" (
        echo Este comando exibe uma lista de todos os usuários no sistema.
        net users    feito
        set conceito=Este comando exibe uma lista de todos os usuários no sistema.
    ) else if "%escolha%"=="5" (
        net share
        set conceito=Este comando lista todos os compartilhamentos no computador atual.
    ) else if "%escolha%"=="6" (
        set /p site=Digite o site para fazer ping: 
        ping %site%
        set conceito=Ping um site
    ) else if "%escolha%"=="7" (
        netstat -ano
        set conceito=exibir informações sobre as conexões de rede ativas, portas abertas e processos 
    ) else if "%escolha%"=="8" (
        ipconfig /all
        set conceito=Mostrar informações de rede
    ) else if "%escolha%"=="0" (
        cls
        set conceito=Limpar a tela
    ) else (
        set conceito=Comando inválido
    )
    set data=%date:~6,4%%date:~3,2%%date:~0,2%
    set nome_arquivo=varredura_%data%.txt
    echo Número do Comando: !comando! >> !nome_arquivo!
    echo Conceito do Comando: !conceito! >> !nome_arquivo!
)

pause
goto menu
