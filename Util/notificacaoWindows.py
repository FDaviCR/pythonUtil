from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast(
    "Notificação",
    "Olá Windows :/",
    threaded=True,
    icon_path=None,
    duration=5
)