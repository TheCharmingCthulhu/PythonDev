# IMPORT
import sys, os
import json

# VARIABLES
class WinAppJammerSettings():
    def __init__(self):
        self.load_config()

        if not hasattr(self, 'ENABLED'):
            self.ENABLED = False

        if not hasattr(self, 'WIN_SYSTEM_APPS_PATH'):
            self.WIN_SYSTEM_APPS_PATH = 'C:\Windows\SystemApps'

        if not hasattr(self, 'TERMINATION_FLAGGED_APPS'):
            self.TERMINATION_FLAGGED_APPS = ['Cortana.exe']

        if not hasattr(self, 'IGNORED_APPS'):
            self.IGNORED_APPS = ['AccountsControl', 'LockApp', 'ShellExperienceHost', 'ContentDeliveryManager']

    def save_config(self):
        waj_json = json.dumps(self.__dict__, indent=4)
        with open('settings.json', 'w') as f:
            f.write(waj_json)

    def load_config(self):
        if os.path.exists('settings.json'):
            with open('settings.json', 'r') as f:
                self.__dict__ = json.load(f)


# SCRIPT
if __name__ == '__main__':
    waj_settings = WinAppJammerSettings()
    waj_settings.save_config()

    for flagged_app in waj_settings.TERMINATION_FLAGGED_APPS:
        os.system('taskkill /im "{0}"'.format(flagged_app))

    app_dirs = os.listdir(waj_settings.WIN_SYSTEM_APPS_PATH)

    for ignored_app in waj_settings.IGNORED_APPS:
        for dir in app_dirs:
            if ignored_app in dir:
                app_dirs.remove(dir)

    for app in app_dirs:
        app_path = '{0}/{1}'.format(waj_settings.WIN_SYSTEM_APPS_PATH, app)

        if not waj_settings.ENABLED:
            if not 'DISABLED' in app:
                try:
                    os.rename(app_path, '{0}_{1}'.format(app_path, 'DISABLED'))
                    print '- Folder "{0}" has been disabled'.format(app)
                except Exception as e:
                    print '- Folder "{0}" could not be restored | Exception: "{1}"'.format(app, e.args[1])
            else:
                print '- Folder "{0}" has already been disabled'.format(app)
        else:
            if 'DISABLED' in app:
                app = app[:app.index('DISABLED')-1]
                try:
                    os.rename(app_path, '{0}/{1}'.format(waj_settings.WIN_SYSTEM_APPS_PATH, app))
                    print '- Folder "{0}" has been restored'.format(app)
                except Exception as e:
                    print '- Folder "{0}" could not be restored | Exception: "{1}"'.format(app, e.args[1])

    raw_input('Press any key to continue...')

