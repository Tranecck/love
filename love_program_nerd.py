import time
import sys
import os

class Colors:
    RED = '\033[91m'
    PINK = '\033[95m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def slow_print(text, delay=0.05, color=Colors.RESET):
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

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
        "hoje te convido a fazer parte da org chamada: 'nós'."
    ]
    for line in verses:
        slow_print(line, delay=0.08, color=Colors.CYAN)
        time.sleep(0.5)

def compatibility_test():
    score = 0
    questions = [
        {
            "q": "Se você fosse um algoritmo, qual seria? (bubble/merge/quick)",
            "ideal": "quick"
        },
        {
            "q": "Você prefere amor com tipagem dinâmica ou estática? (dinamica/estatica)",
            "ideal": "dinamica"
        },
        {
            "q": "Qual desses é mais romântico? (git/terminal/stack overflow)",
            "ideal": "git"
        }
    ]

    slow_print("\nIniciando teste de compatibilidade com base nos nossos dados 💾", color=Colors.BOLD)
    time.sleep(1)
    for item in questions:
        slow_print(f"\n{item['q']}", color=Colors.PINK)
        answer = input("👉 ").strip().lower()
        if answer == item["ideal"]:
            slow_print("✔️ Código aceito!", color=Colors.GREEN)
            score += 1
        else:
            slow_print("⚠️ Hum... código com warnings 😅", color=Colors.YELLOW)

    if score == 3:
        slow_print("\n🎉 Match perfeito! Você passou no CI do meu coração! 💚", color=Colors.BOLD)
    else:
        slow_print("\nTemos algumas diferenças, mas todo bom sistema se adapta. 😉", color=Colors.BOLD)

def pull_request_love():
    slow_print("\n\n📤 Pull Request: amor.py -> main", color=Colors.CYAN)
    time.sleep(1)
    slow_print("Status: Esperando aprovação...", delay=0.07, color=Colors.YELLOW)
    time.sleep(1.5)
    answer = input("\nAceita dar merge nos nossos sentimentos? (sim/não): ").strip().lower()
    if answer == "sim":
        slow_print("🔁 Merge realizado com sucesso! ❤️", color=Colors.RED)
        heart_ascii()
        slow_print("Commit message: 'feat: relacionamento estável e feliz 😍'", color=Colors.GREEN)
    else:
        slow_print("😢 Pull request rejeitado. Mas sempre há espaço para uma nova branch na vida...", color=Colors.YELLOW)

def main():
    clear()
    slow_print("Carregando script romântico nerd para programadoras...", delay=0.05, color=Colors.BOLD)
    time.sleep(1)
    clear()
    heart_ascii()
    nerd_poem()
    compatibility_test()
    pull_request_love()

if __name__ == "__main__":
    main()
