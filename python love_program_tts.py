import time
import sys
import os
import pyttsx3

# Inicializa a voz (Text-to-Speech)
tts = pyttsx3.init()
tts.setProperty('rate', 155)  # Velocidade da fala
tts.setProperty('volume', 1.0)  # Volume (0.0 a 1.0)

# Cores para o terminal
class Colors:
    RED = '\033[91m'
    PINK = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def speak(text):
    tts.say(text)
    tts.runAndWait()

def slow_print(text, delay=0.05, color=Colors.RESET, speak_text=False):
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()
    if speak_text:
        speak(text)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def heart_ascii():
    heart = f"""
{Colors.RED}       *****     *****     
    *********** ***********  
   ************************* 
  *************************** 
  *************************** 
   *************************  
    ***********************   
      *******************     
        ***************       
          ***********         
            *******           
              ***             
               *{Colors.RESET}
    """
    print(heart)

def nerd_poem():
    verses = [
        "Nos logs da minha vida, você é a única entrada que faz sentido.",
        "No Stack Overflow dos sentimentos, sua resposta é sempre aceita.",
        "Nos commits do destino, o meu favorito tem sua assinatura.",
        "Você é o push que faz meu coração dar merge com o seu.",
        "E mesmo nos conflitos, eu faria um rebase só pra te ter perto.",
        "",
        "Se um dia você forkou meu coração,",
        "hoje te convido a fazer parte da org chamada: nós."
    ]
    for line in verses:
        slow_print(line, delay=0.08, color=Colors.CYAN, speak_text=True)
        time.sleep(0.5)

def compatibility_test():
    score = 0
    questions = [
        {
            "q": "Se você fosse um algoritmo, qual seria? (bubble, merge ou quick)",
            "ideal": "quick"
        },
        {
            "q": "Você prefere amor com tipagem dinâmica ou estática?",
            "ideal": "dinamica"
        },
        {
            "q": "Qual desses é mais romântico? (git, terminal ou stack overflow)",
            "ideal": "git"
        }
    ]

    slow_print("\nIniciando teste de compatibilidade com base nos nossos dados 💾", color=Colors.BOLD, speak_text=True)
    time.sleep(1)
    for item in questions:
        slow_print(f"\n{item['q']}", color=Colors.PINK, speak_text=True)
        answer = input("👉 ").strip().lower()
        if answer == item["ideal"]:
            slow_print("✔️ Código aceito!", color=Colors.GREEN, speak_text=True)
            score += 1
        else:
            slow_print("⚠️ Hum... código com warnings 😅", color=Colors.YELLOW, speak_text=True)

    if score == 3:
        slow_print("\n🎉 Match perfeito! Você passou no CI do meu coração!", color=Colors.BOLD, speak_text=True)
    else:
        slow_print("\nTemos algumas diferenças, mas todo bom sistema se adapta.", color=Colors.BOLD, speak_text=True)

def pull_request_love():
    slow_print("\n📤 Pull Request: amor.py -> main", color=Colors.CYAN, speak_text=True)
    time.sleep(1)
    slow_print("Status: Esperando aprovação...", delay=0.07, color=Colors.YELLOW, speak_text=True)
    time.sleep(1.5)
    answer = input("\nAceita dar merge nos nossos sentimentos? (sim/não): ").strip().lower()
    if answer == "sim":
        slow_print("🔁 Merge realizado com sucesso! ❤️", color=Colors.RED, speak_text=True)
        heart_ascii()
        slow_print("Commit message: 'feat: relacionamento estável e feliz 😍'", color=Colors.GREEN, speak_text=True)
    else:
        slow_print("😢 Pull request rejeitado. Mas sempre há espaço para uma nova branch na vida...", color=Colors.YELLOW, speak_text=True)

def main():
    clear()
    slow_print("Carregando script romântico nerd com voz...", delay=0.05, color=Colors.BOLD)
    speak("Iniciando o script romântico nerd.")
    time.sleep(1)
    clear()
    heart_ascii()
    nerd_poem()
    compatibility_test()
    pull_request_love()

if __name__ == "__main__":
    main()
