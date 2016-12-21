# mycroft-youtube
A skill to play youtube

# Requirements 
* mplayer

# Install
    sudo apt-get install mplayer
    mkdir -p ~/.mycroft/third_party_skills/
    cd ~/.mycroft/third_party_skills/
    git clone https://github.com/augustnmonteiro/mycroft-youtube.git youtube
    source ~/.virtualenvs/mycroft/bin/activate
    pip install -r requirements.txt
    ./mycroft.sh restart

# Using
* Say `youtube guns 'n roses don't cry`
