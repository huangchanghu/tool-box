#! /usr/bin/bash

echo "preparing..."
# check env
if [ -z "`which wget`" ]; then
  yum install -y wget
fi
if [ -z "`which unzip`" ]; then
  yum install -y unzip
fi

VERSION="v1.1.1"
SNELL_SERVER_PKG="snell-server-${VERSION}-linux-amd64.zip"
URL="https://github.com/surge-networks/snell/releases/download/${VERSION}/${SNELL_SERVER_PKG}"
TEMP_DIR="./snell-temp"

[ -d ${TEMP_DIR} ] && rm -r ${TEMP_DIR}
 mkdir ${TEMP_DIR}

echo "Downloading ${SNELL_SERVER_PKG}"
wget $URL -O ${TEMP_DIR}/$SNELL_SERVER_PKG
cd ${TEMP_DIR}
unzip $SNELL_SERVER_PKG
./snell-server <<-EOF
y
\r
EOF

echo "Installing snell-server"
mv ./snell-server /usr/local/bin/snell-server
mv ./snell-server.conf /etc/snell-server.conf

echo "Creating systemd service"
cd ..
cp ./snell-server.service /lib/systemd/system/snell-server.service
systemctl enable snell-server
systemctl start snell-server
systemctl status snell-server

echo "firewall"
PORT="`cat /etc/snell-server.conf | grep listen | awk -F ':' '{print $2}'`"
firewall-cmd --zone=public --add-port=${PORT}/tcp --permanent
firewall-cmd --reload

echo "Snell proxy service has been setup successfully."
echo "========================================"
echo "Here are some paths:"
echo "Executable file: /usr/local/bin/snell-server"
echo "Snell config file: /etc/snell-server"
echo "Systemd service: /lib/systemd/system/snell-server.service"

echo "========================================"
echo "For configuring the proxy client, you may need these:"
cat /etc/snell-server.conf

rm -rf $TEMP_DIR
