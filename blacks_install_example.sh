# ssh onto the raspberry pi
ssh pi@raspberrypi.local

# Make working directories
mkdir logs
mkdir code
cd code

# Clone repo
git clone https://github.com/elliotaplant/surf-poster.git
cd surf-poster

# Test the script
python just_get_conditions.py blacks

# Install dependencies if the above didn't work
sudo apt install python-requests python-RPI.GPIO

# Edit crontab and paste following lines
crontab -e
0 * * * * cd /home/pi/code/surf-poster && python main.py blacks >> /home/pi/logs/surf-poster.log 2>&1
1 0 1 * * mv /home/pi/logs/surf-poster.log /home/pi/logs/surf-poster.log.bak && echo -n > /home/pi/logs/surf-poster.log 2>&1

# Edit the pi configuration
sudo raspi-config
  - System options
    - set hostname to something memorable (blacks-surf-poster)
  - System options
    - password

# Shutdown the pi
sudo shutdown -h now

# Delete the raspberry pi entry from your known_hosts to prevent man-in-the-middle warning
vim ~/.ssh/known_hosts
