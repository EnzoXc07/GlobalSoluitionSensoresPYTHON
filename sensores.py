import random
import time

# Simulação de sensores com IoT
def ler_sensores_iot():
    temperatura = random.uniform(20, 50)
    umidade = random.uniform(0, 100)

    agua_parada = random.uniform(0, 10)
    lixo_acumulado = random.uniform(0, 10)

    print("[IoT] Dados recebidos do sensor...")
    time.sleep(1)
    
    return temperatura, umidade, agua_parada, lixo_acumulado
# Análise de risco de queimada e simulação de IoT
def analisar_risco_queimada_iot(temperatura, umidade):
    if temperatura > 35 and umidade < 20:
        return "ALTO"
    elif temperatura > 30 and umidade < 30:
        return "MODERADO"
    else:
        return "BAIXO"

# Ação remota via IoT (ex: drone ou irrigador)
def acionar_dispositivo_iot(nivel_risco):
    if nivel_risco == "ALTO":
        print("[IoT] 🚨 Risco alto detectado!")
        print("[IoT] Acionando drone de resfriamento...")
        time.sleep(2)
        print("[IoT] 🛸 Drone enviado para borrifar água no local!")
    elif nivel_risco == "MODERADO":
        print("[IoT] ⚠️ Risco moderado. Sistema de irrigação local será ativado.")
        time.sleep(1.5)
        print("[IoT] 💦 Irrigadores ativados.")
    else:
        print("[IoT] ✅ Ambiente seguro. Nenhuma ação necessária.")

# Simulação de risco de dengue
def risco_dengue(agua_parada, lixo_acumulado):
 
    if agua_parada >= 5 and lixo_acumulado >= 5:
        return "ALTO"
    elif agua_parada > 5 and lixo_acumulado < 5:
        return "MODERADO"
    elif agua_parada < 5 and lixo_acumulado > 5:
        return "MODERADO"
    else:
        return "BAIXO"

# Alerta de saúde pública via IoT
def notificar_saude_publica(risco):
    if risco == "ALTO":
        print("[IoT] 🚨 Enviando alerta urgente à vigilância sanitária!")
    elif risco == "MODERADO":
        print("[IoT] ⚠️ Enviando notificação preventiva aos órgãos locais.")
    else:
        print("[IoT] ✅ Nenhuma notificação necessária.")

# Função principal
def executar_monitoramento():
    print("===== MONITORAMENTO IoT - CLIMA E SAÚDE =====")
    
    temperatura, umidade, agua_parada, lixo_acumulado = ler_sensores_iot()
    print(f"\n🌡️ Temperatura: {temperatura:.2f}°C")
    print(f"💧 Umidade: {umidade:.2f}%")
    
    risco = analisar_risco_queimada_iot(temperatura, umidade)
    acionar_dispositivo_iot(risco)

    
    print("\n===== DETECÇÃO DE FOCO DE DENGUE =====")

    print(f"💧 Nível de água parada: {agua_parada: .2f}")
    print(f"🗑️ Quantidade de lixo acumulado: {lixo_acumulado: .2f}")

    risco_d = risco_dengue(agua_parada, lixo_acumulado)
    notificar_saude_publica(risco_d)

# Menu principal
def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1 - Executar Monitoramento com IoT")
        print("2 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            executar_monitoramento()
        elif escolha == '2':
            print("Encerrando o sistema IoT. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do programa
menu()
