#!/usr/bin/python3
import eagle
import sys
import getopt

def isPrimitive(thing):
    return isinstance(thing, (int, str, bool, float))

def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hci", ["energy-monitor-hostname=", "client-id=", "installation-id="])
  except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
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

  client = eagle.LocalApi(host=hostname,
                        username=clientId, password=installationId)

  for meter in eagle.Meter.get_meters(client):
    meter.update()

    for attr, value in meter.__dict__.items():
        if isPrimitive(value): 
          print(attr, value)

    print("energy,meter=\"%s\" instantaneous_demand=%f" %
          (meter.device.hardware_address, meter.instantaneous_demand))
        
if __name__ == "__main__":
    main()


