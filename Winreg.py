import winreg
Keys =[]
access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
access_key = winreg.OpenKey(access_registry,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
i = 0
while True:
    try:
        result = winreg.EnumKey(access_key,i)
        Keys.append(result)
        i = i + 1
    except:
        break

for subkeys in Keys:
    try:
        path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"+"\\"+subkeys
        key = winreg.OpenKey(access_registry,path)
        try:
            name = winreg.QueryValueEx(key,'DisplayName')
            version = winreg.QueryValueEx(key,'DisplayVersion')
            print("Name: {0}  Version: {1}".format(name[0] ,version[0]))
            print('*'*45)
        except:
            continue
    except:

        continue
