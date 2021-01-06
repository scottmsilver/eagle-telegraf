#!/usr/bin/python3
import eagle
import sys
import getopt
from enum import Enum

class Type(Enum):
  NUMBER = 1,
  STRING = 2

fieldTypes = {
"zigbee:InstantaneousDemand": Type.NUMBER,
"zigbee:Multiplier": Type.NUMBER,
"zigbee:Divisor": Type.NUMBER,
"zigbee:CurrentSummationDelivered": Type.NUMBER,
"zigbee:CurrentSummationReceived": Type.NUMBER,
"zigbee:Price": Type.NUMBER,
"zigbee:PriceTrailingDigits": Type.NUMBER,
"zigbee:PriceRateLabel": Type.STRING,
"zigbee:PriceCurrency": Type.STRING,
"zigbee:PriceTier": Type.NUMBER,
"zigbee:PriceStartTime": Type.NUMBER,
"zigbee:PriceDuration": Type.NUMBER,
"zigbee:Message": Type.STRING,
"zigbee:MessageId": Type.STRING,
"zigbee:MessageStartTime": Type.NUMBER,
"zigbee:MessageDurationInMinutes": Type.NUMBER,
"zigbee:MessagePriority": Type.NUMBER,
"zigbee:MessageConfirmationRequired": Type.STRING,
"zigbee:MessageConfirmed": Type.STRING,
"zigbee:BlockPeriodType.NUMBEROfBlocks": Type.NUMBER,
"zigbee:CurrentBlockPeriodConsumptionDelivered": Type.NUMBER,
"zigbee:NoTierBlock1Price": Type.NUMBER,
"zigbee:NoTierBlock2Price": Type.NUMBER,
"zigbee:NoTierBlock3Price": Type.NUMBER,
"zigbee:NoTierBlock4Price": Type.NUMBER,
"zigbee:NoTierBlock5Price": Type.NUMBER,
"zigbee:NoTierBlock6Price": Type.NUMBER,
"zigbee:NoTierBlock7Price": Type.NUMBER,
"zigbee:NoTierBlock8Price": Type.NUMBER,
"zigbee:Block1Threshold": Type.NUMBER,
"zigbee:Block2Threshold": Type.NUMBER,
"zigbee:Block3Threshold": Type.NUMBER,
"zigbee:Block4Threshold": Type.NUMBER,
"zigbee:Block5Threshold": Type.NUMBER,
"zigbee:Block6Threshold": Type.NUMBER,
"zigbee:Block7Threshold": Type.NUMBER,
"zigbee:Block8Threshold": Type.NUMBER,
"zigbee:StartOfBlockPeriod": Type.NUMBER,
"zigbee:BlockPeriodDuration": Type.NUMBER,
"zigbee:ThresholdMultiplier": Type.NUMBER,
"zigbee:ThresholdDivisor": Type.NUMBER,
"zigbee:CurrentBillingPeriodStart": Type.NUMBER,
"zigbee:CurrentBillingPeriodDuration": Type.NUMBER
}
  
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False
  except TypeError:
    return False
      
def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hci", ["energy-monitor-hostname=", "client-id=", "installation-id="])
  except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  
    sys.exit(2)

  hostname = None
  clientId = None
  installationId = None

  for option, attribute in opts:
    if option in ("-h", "--energy-monitor-hostname"):
      hostname = attribute
    elif option in ("-c", "--client-id"):
      clientId = attribute
    elif option in ("-i", "--installation-id"):
      installationId = attribute
    else:
      assert False, "unhandled option"

  assert hostname and clientId and installationId, "You must sepply all command line options."
  
  client = eagle.LocalApi(host=hostname,
                        username=clientId, password=installationId)

  for meter in eagle.Meter.get_meters(client):
    meter.update()
    print("energy,meter=\"%s\" " % meter.device.hardware_address, end='')
    measures = []
    foos = []
    for variable in meter.device.get_all_variables()['Main']:
      value = variable.value
      
      if value != None and variable.name in fieldTypes:
        fieldType = fieldTypes[variable.name]
        if fieldType == Type.STRING:
          value = "\"%s\"" % value

        measures.append("%s=%s" % (variable.name, value))
    
    
    print("%s=%s," % (variable.name, value), end='')
    print(",".join(measures))

if __name__ == "__main__":
    main()


