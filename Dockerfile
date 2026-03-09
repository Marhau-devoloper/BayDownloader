FROM ubuntu:latest


RUN (apt update && apt install -y python3 python3-venv aria2 git)
RUN (git clone https://github.com/Marhau-devoloper/BayDownloader.git)
WORKDIR /BayDownloader
RUN (ls)
RUN (python3 -m venv venv)
RUN (venv/bin/pip install requests)
RUN (ls)
RUN echo '#!/bin/sh' > start.sh \
 && echo '. venv/bin/activate' >> start.sh \
 && echo 'python3 main.py' >> start.sh \
 && chmod +x start.sh
CMD ["./start.sh"]
