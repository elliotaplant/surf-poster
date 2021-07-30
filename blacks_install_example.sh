# ssh onto the raspberry pi
ssh pi@raspberrypi.local

# Make working directories
mkdir logs
mkdir code

# Install dependencies
sudo apt install python-requests python-RPI.GPIO

# Install the WiFi configurator
cd code
git clone https://github.com/elliotaplant/RaspiWiFi.git
# Run the setup (use the defaults, no passwords)
sudo python3 initial_setup.py

# Clone repo
git clone https://github.com/elliotaplant/surf-poster.git
cd surf-poster

# Test the script
python just_get_conditions.py blacks

# Edit crontab and paste following lines
crontab -e
# Runs the hourly update
0  * * * * cd /home/pi/code/surf-poster && python main.py blacks >> /home/pi/logs/surf-poster.log 2>&1
# Clears the logs every month
10 0 1 * * mv /home/pi/logs/surf-poster.log /home/pi/logs/surf-poster.log.bak && echo -n > /home/pi/logs/surf-poster.log 2>&1
# Pulls the latest version from git
30 4 * * * cd /home/pi/code/surf-poster && git pull;

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
