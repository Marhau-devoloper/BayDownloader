# BayDownloader
Download files fom Bay

Dependencies
requests
<p>pip install requests</p>

aria2
# Arch / Manjaro
sudo pacman -S aria2
# Ubuntu / Debian
sudo apt install aria2



# Build the Docker image (fresh build)
sudo docker build --no-cache -t BayDownload .

# Run the container interactively, mount Downloads, and open necessary ports
docker run -it \
  -v ~/Downloads:/BayDownloader/Downloads \
  -v ~/aria2-cache:/root/.cache/aria2 \
  -p 6894:6894/tcp \
  -p 6979:6979/udp \
  BayDownload
