import colorama
from colorama import Fore, Style

def print_banner():
    colorama.init(autoreset=True)
    banner = f"""{Fore.RED}
     oooooo   oooooo     oooo  o8o  ooooooooo.   oooooooooooo             
 `888.    `888.     .8'   `"'  `888   `Y88. `888'     `8             
  `888.   .8888.   .8'   oooo   888   .d88'  888         oooo    ooo 
   `888  .8'`888. .8'    `888   888ooo88P'   888oooo8     `88b..8P'  
    `888.8'  `888.8'      888   888          888    "       Y888'    
     `888'    `888'       888   888          888       o  .o8"'88b   
      `8'      `8'       o888o o888o        o888ooooood8 o88'   888o 
                                                                     
                                 {Style.RESET_ALL}
    """
    print(banner)

if __name__ == "__main__":
    print_banner()
    
    
    
    
    
    
    
    
    
