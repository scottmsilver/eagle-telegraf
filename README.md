# eagle-telegraf
Simple script to query an Eagle 200 and use it in telegraf.

# Installation

## Install rfa-eagle-api and to access your eagle and influx_line_protocol to print metrics

```
pip3 install rfa-eagle-api
pip3 install influx_line_protocol
```

## Test it locally

```
./eagle-to-telegraf.py --energy-monitor-hostname=hostname-of-eagle --client-id=client-id-on-underside-of-device --installation-id=-instalation-id-on-underside-of-device

energy,result=SUCCESS,meter=0x0013500100f56f8a zigbee:InstantaneousDemand=2.951,zigbee:Multiplier=1,zigbee:Divisor=1000,zigbee:CurrentSummationDelivered=79450,zigbee:CurrentSummationReceived=22500.9,zigbee:PriceTrailingDigits=255,zigbee:PriceCurrency="USD\",zigbee:PriceTier=0,zigbee:PriceStartTime=9.46685e+08,zigbee:PriceDuration=0,zigbee:MessageConfirmationRequired="false",zigbee:MessageConfirmed="false",zigbee:CurrentBlockPeriodConsumptionDelivered=0,zigbee:StartOfBlockPeriod=9.46685e+08,zigbee:BlockPeriodDuration=0,zigbee:ThresholdMultiplier=1,zigbee:ThresholdDivisor=1,zigbee:CurrentBillingPeriodStart=1.60987e+09,zigbee:CurrentBillingPeriodDuration=6.05298e+07
```

## Place it in your telegraf config

Edit /etc/telegraf/telegraf.conf

```
[[inputs.exec]]                                                                                                              
   ## Commands array                                                                                                        
   commands = [                                                                                                             
     "/home/pi/eagle-telegraf/eagle-to-telegraf.py --energy-monitor-hostname=hostname-of-eagle --client-id=client-id-on-underside-of-device --installation-id=-instalation-id-on-underside-of-device"        
   ]                                                                                                                          
                                                                                                                             
   ## Timeout for each command to complete.                                                                                 
   timeout = "10s"                                                                                                          
   interval = "1m"
```

## Test telegraf

```
telegraf --test
```

Look for lines like:

```
energy,result=SUCCESS,meter=0x0013500100f56f8a zigbee:InstantaneousDemand=2.951,zigbee:Multiplier=1,zigbee:Divisor=1000,zigbee:CurrentSummationDelivered=79450,zigbee:CurrentSummationReceived=22500.9,zigbee:PriceTrailingDigits=255,zigbee:PriceCurrency="USD\",zigbee:PriceTier=0,zigbee:PriceStartTime=9.46685e+08,zigbee:PriceDuration=0,zigbee:MessageConfirmationRequired="false",zigbee:MessageConfirmed="false",zigbee:CurrentBlockPeriodConsumptionDelivered=0,zigbee:StartOfBlockPeriod=9.46685e+08,zigbee:BlockPeriodDuration=0,zigbee:ThresholdMultiplier=1,zigbee:ThresholdDivisor=1,zigbee:CurrentBillingPeriodStart=1.60987e+09,zigbee:CurrentBillingPeriodDuration=6.05298e+07
```

Note that you may find that this doesn't work as root. If so, you may need to install rfa-eagle-api as root (which telegraf runs as)


## Restart telegraf

```
systemctl restart telegraf
```
