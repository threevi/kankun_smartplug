#!/usr/bin/env bash

_ROOT_PASSWD="#3viSmartpluG3vi#"
_NETWORK_SSID="ntx101"
_NETWORK_PASSWD="turley123dyer"

#==============================================================================
#==============================================================================

_SCRIPT=$(cat << EOF
echo -e '$_ROOT_PASSWD\n$_ROOT_PASSWD\n' | passwd > /dev/null &&
sed -i '/config wifi-iface/q' /etc/config/wireless > /dev/null &&
echo -e '\toption device radio0\n'\
        '\toption network wwan\n' \
        '\toption ssid \"$_NETWORK_SSID\"\n' \
        '\toption mode sta\n' \
        '\toption encryption psk2\n' \
        '\toption key \"$_NETWORK_PASSWD\"\n' >> /etc/config/wireless &&
echo -e 'config interface \"wwan\"\n' \
        '\toption proto \"dhcp\"\n' >> /etc/config/network &&
echo -e 'ALL STEPS PASSED...REBOOTING...' &&
reboot
EOF
)

function _chkdeps() {
        which sshpass &> /dev/null
        if [ $? -ne 0 ]; then
                >&2 echo "[ FAIL ]: Missing sshpass utility. Please install."
                exit 1
        fi
}

function _main() {
	_chkdeps

	sshpass -p "p9z34c" \
	ssh -q -o "StrictHostKeyChecking=no" -o "UserKnownHostsFile=/dev/null" \
		root@192.168.10.253 "echo \"$_SCRIPT\" | ash -s"
}

_main
