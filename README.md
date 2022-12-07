# eagle-telegraf
Simple script to query an Eagle 200 and use it in telegraf.

# Installation

## Install rfa-eagle-api to access your eagle

```
pip3 install rfa-eagle-api
```

## Test it locally

```
./eagle-to-telegraf.py --energy-monitor-hostname=hostname-of-eagle --client-id=client-id-on-underside-of-device --installation-id=-instalation-id-on-underside-of-device

energy,host=measure,meter="0x0013500100f56f8a" zigbee:Block1Threshold="None",zigbee:Block2Threshold="None",zigbee:Block3Threshold="None",zigbee:Block4Threshold="None",zigbee:Block5Threshold="None",zigbee:Block6Threshold="None",zigbee:Block7Threshold="None",zigbee:Block8Threshold="None",zigbee:BlockPeriodDuration=0,zigbee:BlockPeriodNumberOfBlocks=0,zigbee:CurrentBillingPeriodDuration=60529753,zigbee:CurrentBillingPeriodStart=1609866880,zigbee:CurrentBlockPeriodConsumptionDelivered=0,zigbee:CurrentSummationDelivered=38018.389,zigbee:CurrentSummationReceived=57.207,zigbee:Divisor=1000,zigbee:InstantaneousDemand=1.66,zigbee:Message="None",zigbee:MessageConfirmationRequired="false",zigbee:MessageConfirmed="false",zigbee:MessageDurationInMinutes="None",zigbee:MessageId="None",zigbee:MessagePriority="None",zigbee:MessageStartTime="None",zigbee:Multiplier=1,zigbee:NoTierBlock1Price="None",zigbee:NoTierBlock2Price="None",zigbee:NoTierBlock3Price="None",zigbee:NoTierBlock4Price="None",zigbee:NoTierBlock5Price="None",zigbee:NoTierBlock6Price="None",zigbee:NoTierBlock7Price="None",zigbee:NoTierBlock8Price="None",zigbee:Price="invalid",zigbee:PriceCurrency="USD",zigbee:PriceDuration=0,zigbee:PriceRateLabel="None",zigbee:PriceStartTime=946684800,zigbee:PriceTier=0,zigbee:PriceTrailingDigits=255,zigbee:StartOfBlockPeriod=946684800,zigbee:ThresholdDivisor=1,zigbee:ThresholdMultiplier=1 
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

Look for lins like:

```
energy,host=measure,meter="0x0013500100f56f8a" zigbee:Block1Threshold="None",zigbee:Block2Threshold="None",zigbee:Block3Threshold="None",zigbee:Block4Threshold="None",zigbee:Block5Threshold="None",zigbee:Block6Threshold="None",zigbee:Block7Threshold="None",zigbee:Block8Threshold="None",zigbee:BlockPeriodDuration=0,zigbee:BlockPeriodNumberOfBlocks=0,zigbee:CurrentBillingPeriodDuration=60529753,zigbee:CurrentBillingPeriodStart=1609866880,zigbee:CurrentBlockPeriodConsumptionDelivered=0,zigbee:CurrentSummationDelivered=38018.389,zigbee:CurrentSummationReceived=57.207,zigbee:Divisor=1000,zigbee:InstantaneousDemand=1.66,zigbee:Message="None",zigbee:MessageConfirmationRequired="false",zigbee:MessageConfirmed="false",zigbee:MessageDurationInMinutes="None",zigbee:MessageId="None",zigbee:MessagePriority="None",zigbee:MessageStartTime="None",zigbee:Multiplier=1,zigbee:NoTierBlock1Price="None",zigbee:NoTierBlock2Price="None",zigbee:NoTierBlock3Price="None",zigbee:NoTierBlock4Price="None",zigbee:NoTierBlock5Price="None",zigbee:NoTierBlock6Price="None",zigbee:NoTierBlock7Price="None",zigbee:NoTierBlock8Price="None",zigbee:Price="invalid",zigbee:PriceCurrency="USD",zigbee:PriceDuration=0,zigbee:PriceRateLabel="None",zigbee:PriceStartTime=946684800,zigbee:PriceTier=0,zigbee:PriceTrailingDigits=255,zigbee:StartOfBlockPeriod=946684800,zigbee:ThresholdDivisor=1,zigbee:ThresholdMultiplier=1 
```

Note that you may find that this doesn't work as root. If so, you may need to install rfa-eagle-api as root (which telegraf runs as)


## Restart telegraf

```
systemctl restart telegraf
```
