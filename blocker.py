import psutil

def block_app(app_name):
    """ Kill all processess that match the app name """
    for proc in psutil.process_iter(['name']):
        try:
            if app_name.lower() in proc.info['name'].lower():
                proc.kill()
                print(f"Blocked {proc.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass