# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Sayonara-Userbot
# Sayonara

RUN git clone -b KONTOL-USERBOT https://github.com/ArmanGG01/KONTOL-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ArmanGG01/KONTOL-USERBOT/KONTOL-USERBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
