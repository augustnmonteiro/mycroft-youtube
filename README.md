# mycroft-youtube
A skill to play youtube

# Requirements 
* mplayer

# Install Using [MSM (Mycroft Skill Manager)](https://github.com/augustnmonteiro/msm)
    sudo msm install https://github.com/augustnmonteiro/mycroft-youtube.git

# Install Manualy
    sudo apt-get install mplayer
    sudo mkdir -p /opt/mycroft/skills
    cd /opt/mycroft/skills 
    sudo git clone https://github.com/augustnmonteiro/mycroft-youtube.git youtube 
    cd youtube 
    source ~/.virtualenvs/mycroft/bin/activate 
    pip install -r requirements.txt 
    ./mycroft.sh restart 

# Using
* Say `youtube guns 'n roses don't cry`
