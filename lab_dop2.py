import wave
import struct


def delete_frame(file_orig, numb_frame):  # Объявляем функцию по поиску удалению фреймов из аудиофайла.
    """WIP."""
    try:
        src = wave.open(f"{(file_orig)}.wav", mode="rb")  # Открываем наш изначальный файл.
        summ = wave.open(f"{str(file_orig)}_tuned.wav", mode="wb")  # Создаем новый аудио-файл.
        summ.setparams(src.getparams())
        frames = src.getnframes()
        datapack = src.readframes(frames)
        datapack = struct.unpack(f"<{str(frames*2)}h", datapack)
        new_datapack = list(datapack)
        del new_datapack[::numb_frame]
        new_frames = struct.pack(f"<{str(len(new_datapack))}h", *new_datapack)
        summ.writeframes(new_frames)
        src.close()
        summ.close()
        return True
    except FileNotFoundError:
        print(f"Well, i didn't find a file named {file_orig}.wav, sorry.")
        return False


file = str(input('Write the audio file you want to edit: '))   # Запрашиваем название .wav файла.
numb = int(input('Write the number of the frames that you want to edit(2-5): '))  # Уточняем как сильно будем ускорять аудио файл.
if numb in range(2, 6):
    ending = delete_frame(file, numb)

if ending:
    print("Success, audio file is edited.")
    


