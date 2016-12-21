# mycroft-youtube
A skill to play youtube

# Requirements 
* mplayer

# Install
mkdir -p ~/.mycroft/third_party_skills/
cd ~/.mycroft/third_party_skills/
git clone https://github.com/augustnmonteiro/mycroft-youtube.git youtube
source ~/.virtualenvs/mycroft/bin/activate
pip install -r requirements.txt
# restart the skills service
./mycroft.sh restart

# Usage
* youtube <search>
