#Packan mini game example

1. Installeer Raspberry Pi OS (Lite of Desktop)
2. Update systeem:
   sudo apt update && sudo apt upgrade

3. Installeer pygame:
   sudo apt install python3-pygame

4. Plaats project:
   mkdir pacman && cd pacman
   (plaats alle .py bestanden hier)

5. Start spel:
   python3 main.py

6. (OPTIONEEL) Autostart bij boot:
   nano ~/.bashrc
   Voeg toe onderaan:
   cd /home/pi/pacman && python3 main.py

7. Performance tips:
   - Gebruik Raspberry Pi 3/4
   - Sluit HDMI af bij headless gebruik
   - Verlaag FPS indien nodig
