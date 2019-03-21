#!/usr/local/bin/fish
set price (curl -s 'CB-version: 2015-04-08' https://api.coinbase.com/v2/prices/ETH-USD/spot | sed 's/warnings.*//g' | sed 's/[a-zA-Z:{},]//g' | sed 's/"//g')
# set earlier (curl -s https://api.gdax.com/products/ETH-USD/stats | jq -S '[.open][0]' | sed 's/"//g')
set earlier (jq -S '."ETH-USD"' /Users/yiws/.cryptoprice.json)
set change \"(echo (echo "(10000*$price)/($earlier) - 10000" | bc) "/100" | bc -l)\"
# echo $change
set fchange (echo "from re import match; m = match(r'(-?\d*\.\d\d).*', $change); num = m.groups(1)[0]; num = '0' + num if float(num) < 1. and float(num) > 0 else num; num = '+' + num if float(num) >= 0. else num; print(num)" | python3)
set screensaver_str "'Ethereum - \$$price \($fchange\%\)'"
defaults -currentHost WRITE com.apple.screensaver.Basic MESSAGE $screensaver_str
killall cfprefsd
# echo $screensaver_str
