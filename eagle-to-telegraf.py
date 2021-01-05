#!/usr/bin/python3
import eagle
import sys
import getopt

def isPrimitive(thing):
  return isinstance(thing, (property, ))

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
    for variable in meter.device.get_all_variables()['Main']:
      print("%s=%s," % (variable.name, variable.value), end='')
    print()
        
if __name__ == "__main__":
    main()


